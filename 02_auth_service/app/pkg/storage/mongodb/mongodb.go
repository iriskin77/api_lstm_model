package mongodb

import (
	"context"
	"fmt"

	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
)

func NewClientMongo(ctx context.Context, host, port, username, password, authDB string) (mongoClient *mongo.Client, err error) {

	var mongoDBURL string
	//var isAuth bool

	if username == "" && password == "" {
		mongoDBURL = fmt.Sprintf("mongodb://%s:%s", host, port)
	} else {
		//isAuth = true
		mongoDBURL = fmt.Sprintf("mongodb://%s:%s@%s:%s", username, password, host, port)
	}

	fmt.Println(mongoDBURL)
	// "mongodb://localhost:27017/lms?ssl=false&authSource=admin"
	clientOptions := options.Client().ApplyURI("mongodb://localhost:27017/")

	client, err := mongo.Connect(ctx, clientOptions)
	if err != nil {
		return nil, fmt.Errorf("failed to connect to mongoDB due to error: %v", err)
	}

	if err = client.Ping(ctx, nil); err != nil {
		return nil, fmt.Errorf("failed to ping mongoDB due to error: %v", err)
	}

	fmt.Println(1111)

	return client, nil

}

// TODO: This func should be in repository package
func NewMongoDB(mongoClient *mongo.Client, database string) *mongo.Database {
	return mongoClient.Database(database)
}
