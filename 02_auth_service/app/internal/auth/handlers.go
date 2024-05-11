package auth

import (
	"fmt"

	auth_grpc "github.com/iriskin77/auth_grpc/app/internal/protos/genproto"
	"github.com/iriskin77/auth_grpc/app/pkg/jwt_auth"
	"golang.org/x/net/context"
	"google.golang.org/grpc"
)

type Auth interface {
	Register(ctx context.Context, dto *UserCreateDTO) (string, error)
	Login(ctx context.Context, dto *UserLoginDTO) (*jwt_auth.Tokens, error)
	RefreshTokens(ctx context.Context, refreshToken string) (*jwt_auth.Tokens, error)
	DeleteUser(ctx context.Context, userUUID string) (bool, error)
}

type serverAPI struct {
	auth_grpc.UnimplementedAuthServer
	auth Auth
}

// Обрабатывает запросы, которые приходят в gRPC сервер
func RegisterAuthGRPC(gRPC *grpc.Server, auth Auth) {
	auth_grpc.RegisterAuthServer(gRPC, &serverAPI{auth: auth})
}

func (s *serverAPI) Register(ctx context.Context, request *auth_grpc.RegisterRequest) (*auth_grpc.RegisterResponse, error) {

	dto, err := NewUserCreateDTO(request.Email, request.Password, request.RepeatedPassword)
	if err != nil {
		// TODO: apperror
		fmt.Println(err)
	}

	newUserUuid, err := s.auth.Register(ctx, dto)
	if err != nil {
		fmt.Println(err)
	}

	return &auth_grpc.RegisterResponse{UserUuid: newUserUuid}, nil
}

func (s *serverAPI) Login(ctx context.Context, request *auth_grpc.LoginRequest) (*auth_grpc.LoginResponse, error) {

	// user := User{
	// 	Password: request.Password,
	// 	Email:    request.Email,
	// }

	dto, err := NewUserLoginDTO(request.Email, request.Password)
	if err != nil {
		// TODO: apperror
		fmt.Println(err)
	}

	tokens, err := s.auth.Login(ctx, dto)

	if err != nil {
		fmt.Println(err)
	}

	return &auth_grpc.LoginResponse{AccessToken: tokens.AccessToken, RefreshToken: tokens.RefreshToken}, nil
}

func (s *serverAPI) RefreshTokens(ctx context.Context, request *auth_grpc.RefreshTokensRequest) (*auth_grpc.RefreshTokensResponse, error) {

	tokens, err := s.auth.RefreshTokens(ctx, request.RefreshToken)
	if err != nil {
		fmt.Println(err)
	}

	return &auth_grpc.RefreshTokensResponse{AccessToken: tokens.AccessToken, RefreshToken: tokens.RefreshToken}, nil

}

func (s *serverAPI) DeleteUser(ctx context.Context, request *auth_grpc.DeleteUserRequest) (*auth_grpc.DeleteUserResponse, error) {
	panic("implement me")
}
