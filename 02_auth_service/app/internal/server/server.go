package server

import (
	"fmt"
	"net"

	"github.com/iriskin77/auth_grpc/app/internal/auth"
	"github.com/iriskin77/auth_grpc/app/pkg/jwt_auth"
	"github.com/iriskin77/auth_grpc/app/pkg/logger"
	"google.golang.org/grpc"
)

type App struct {
	logger     *logger.Logger
	gRPCServer *grpc.Server
	port       int
}

// create new grpc server
func NewApp(log *logger.Logger, port int, db *auth.Repository, rdb *auth.RedisRepo, tokenManager jwt_auth.TokenManager) *App {

	gRPCServer := grpc.NewServer()

	service := auth.NewService(db, tokenManager, rdb, log)

	auth.RegisterAuthGRPC(gRPCServer, service)

	return &App{
		logger:     log,
		gRPCServer: gRPCServer,
		port:       port,
	}
}

func (a *App) MustRun() {
	if err := a.Run(); err != nil {
		panic(err)
	}
}

func (a *App) Run() error {

	const op = "server.Run"

	l, err := net.Listen("tcp", fmt.Sprintf(":%d", a.port))
	if err != nil {
		return fmt.Errorf("%s: %w", op, err)
	}

	if err := a.gRPCServer.Serve(l); err != nil {
		return fmt.Errorf("%s: %w", op, err)
	}

	return nil
}

func (a *App) Stop() {

	a.gRPCServer.GracefulStop()
}
