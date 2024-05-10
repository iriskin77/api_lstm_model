package auth

import (
	"github.com/iriskin77/auth_grpc/app/pkg/logger"
	"go.mongodb.org/mongo-driver/mongo"
	"golang.org/x/net/context"
)

type Storage interface {
	Login(ctx context.Context, user User) (string, error)
}

type Repository struct {
	db     *mongo.Database
	logger *logger.Logger
}

func NewRepository(db *mongo.Database, logger *logger.Logger) *Repository {
	return &Repository{db: db, logger: logger}
}

func (r *Repository) Login(ctx context.Context, user User) (string, error) {
	return "", nil
}
