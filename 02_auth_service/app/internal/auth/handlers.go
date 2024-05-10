package auth

import (
	auth_grpc "github.com/iriskin77/auth_grpc/app/internal/protos/genproto"
	"github.com/iriskin77/auth_grpc/app/pkg/jwt_auth"
	"golang.org/x/net/context"
	"google.golang.org/grpc"
)

type Auth interface {
	Login(ctx context.Context, user User) (*jwt_auth.Tokens, error)
}

type serverAPI struct {
	auth_grpc.UnimplementedAuthServer
	auth Auth
}

// Обрабатывает запросы, которые приходят в gRPC сервер
func RegisterAuthGRPC(gRPC *grpc.Server, auth Auth) {
	auth_grpc.RegisterAuthServer(gRPC, &serverAPI{auth: auth})
}

func (s *serverAPI) Login(ctx context.Context, request *auth_grpc.LoginRequest) (*auth_grpc.LoginResponse, error) {
	panic("implement me")
}
