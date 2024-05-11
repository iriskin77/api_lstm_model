package auth

import (
	"fmt"
	"time"

	"github.com/iriskin77/auth_grpc/app/pkg/logger"
	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/bson/primitive"
	"go.mongodb.org/mongo-driver/mongo"
	"golang.org/x/net/context"
)

type Storage interface {
	CreateUser(ctx context.Context, user *User) (string, error)
	GetUserByEmail(ctx context.Context, email string) (*User, error)
	DeleteUser(ctx context.Context, userUUID string) (bool, error)
}

type Repository struct {
	collection *mongo.Collection
	logger     *logger.Logger
}

func NewRepository(db *mongo.Database, database string, logger *logger.Logger) *Repository {
	return &Repository{collection: db.Collection(database), logger: logger}
}

// Create user in MongoDB
func (r *Repository) CreateUser(ctx context.Context, user *User) (string, error) {

	nCtx, cancel := context.WithTimeout(ctx, 5*time.Second)
	defer cancel()

	newUser, err := r.collection.InsertOne(nCtx, user)
	if err != nil {
		return "", fmt.Errorf("failed to execute query. error: %w", err)
	}

	oid, ok := newUser.InsertedID.(primitive.ObjectID)
	if !ok {
		return "", fmt.Errorf("failed to convet objectid to hex")
	}

	return oid.Hex(), nil
}

func (r *Repository) GetUserByEmail(ctx context.Context, email string) (*User, error) {
	filter := bson.M{"email": email}

	u := &User{}

	ctx, cancel := context.WithTimeout(ctx, 5*time.Second)
	defer cancel()

	result := r.collection.FindOne(ctx, filter)

	if err := result.Decode(u); err != nil {
		return u, fmt.Errorf("failed to decode document. error: %w", err)
	}

	return u, nil
}

func (r *Repository) DeleteUser(ctx context.Context, userUUID string) (bool, error) {
	return true, nil
}
