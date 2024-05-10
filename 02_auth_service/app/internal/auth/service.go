package auth

import (
	"github.com/iriskin77/auth_grpc/app/pkg/jwt_auth"
	"github.com/iriskin77/auth_grpc/app/pkg/logger"
	"golang.org/x/net/context"
)

type Service interface {
	Login(ctx context.Context, user User) (*jwt_auth.Tokens, error)
}

type service struct {
	// создаем структуру, которая принимает репозиторий для работы с БД
	storage      Storage
	tokenManager jwt_auth.TokenManager
	redisdb      *RedisRepo
	logger       *logger.Logger
}

func NewService(
	repo *Repository,
	tokenManager jwt_auth.TokenManager,
	rd *RedisRepo,
	log *logger.Logger) *service {

	return &service{
		storage:      repo,
		tokenManager: tokenManager,
		redisdb:      rd,
		logger:       log,
	}
}

func (s *service) Login(ctx context.Context, user User) (*jwt_auth.Tokens, error) {
	return nil, nil
}
