package auth

import (
	"fmt"
	"time"

	"github.com/iriskin77/auth_grpc/app/pkg/jwt_auth"
	"github.com/iriskin77/auth_grpc/app/pkg/logger"
	"golang.org/x/net/context"
)

type Service interface {
	Register(ctx context.Context, dto *UserCreateDTO) (string, error)
	Login(ctx context.Context, dto *UserLoginDTO) (*jwt_auth.Tokens, error)
	RefreshTokens(ctx context.Context, refreshToken string) (*jwt_auth.Tokens, error)
	DeleteUser(ctx context.Context, userUUID string) (bool, error)
}

type service struct {
	// создаем структуру, которая принимает репозиторий для работы с БД
	storage      Storage
	tokenManager *jwt_auth.Manager
	redisdb      *RedisRepo
	logger       *logger.Logger
}

func NewService(
	repo Storage,
	tokenManager *jwt_auth.Manager,
	rd *RedisRepo,
	log *logger.Logger) *service {

	return &service{
		storage:      repo,
		tokenManager: tokenManager,
		redisdb:      rd,
		logger:       log,
	}
}

// Register user
func (s *service) Register(ctx context.Context, dto *UserCreateDTO) (string, error) {

	if dto.Password != dto.RepeatedPassword {
		return "", fmt.Errorf("password does not match repeat password")
	}

	user, err := NewUser(dto)
	if err != nil {
		return "", fmt.Errorf("password does not match repeat password")
	}

	if err := user.GeneratePasswordHash(); err != nil {
		return "", fmt.Errorf(err.Error())
	}

	newUserUuid, err := s.storage.CreateUser(ctx, user)
	if err != nil {
		fmt.Println(err)
	}

	return newUserUuid, nil
}

// Login user giving him tokens
func (s *service) Login(ctx context.Context, dto *UserLoginDTO) (*jwt_auth.Tokens, error) {

	user, err := s.storage.GetUserByEmail(ctx, dto.Email)
	if err != nil {
		fmt.Println(user)
	}

	fmt.Println(user)

	if err := dto.CheckPassword(user.Password); err != nil {
		fmt.Println(err)
	}

	tokens, err := s.createSession(ctx, user.UUID)
	if err != nil {
		fmt.Println(err)
	}

	return &tokens, nil
}

func (s *service) createSession(ctx context.Context, userUUID string) (jwt_auth.Tokens, error) {

	var (
		tokens jwt_auth.Tokens
		err    error
	)

	tokens.AccessToken, err = s.tokenManager.NewJWT(userUUID)
	if err != nil {
		return tokens, err
	}

	tokens.RefreshToken, err = s.tokenManager.NewRefreshToken()
	if err != nil {
		return tokens, err
	}
	session := Session{
		UserUUID:  userUUID,
		ExpiresAt: time.Duration(s.tokenManager.RefreshTokenTTL) * time.Minute,
	}

	err = s.redisdb.SetSession(ctx, tokens.RefreshToken, session)

	return tokens, err
}

// Refresh tokens
func (s *service) RefreshTokens(ctx context.Context, refreshToken string) (*jwt_auth.Tokens, error) {

	uuid, err := s.getUuidFromSession(ctx, refreshToken)
	if err != nil {
		fmt.Println(err)
	}

	s.redisdb.DeleteSession(ctx, refreshToken)

	tokens, err := s.createSession(ctx, uuid)
	if err != nil {
		fmt.Println(err)
	}

	return &tokens, nil
}

func (s *service) getUuidFromSession(ctx context.Context, refreshToken string) (string, error) {
	sess, err := s.redisdb.GetSession(ctx, refreshToken)
	if err != nil {
		fmt.Println(err)
	}

	return sess.UserUUID, nil
}

// Delete user
func (s *service) DeleteUser(ctx context.Context, userUUID string) (bool, error) {
	return true, nil
}
