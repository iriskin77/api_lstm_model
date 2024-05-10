package main

import (
	"context"
	"fmt"
	"os"

	"github.com/iriskin77/auth_grpc/app/pkg/logger"
	"github.com/iriskin77/auth_grpc/app/pkg/mongodb"
	"github.com/joho/godotenv"
)

func main() {

	// initializing logger

	logger.Init()
	logger := logger.GetLogger()
	logger.Println("logger initialized")

	// load .env variables

	if err := godotenv.Load("/home/abc/Рабочий стол/file/02_auth_service/.env"); err != nil {
		logger.Fatal(err)
	}

	// initializing MongoDB

	mongoClient, err := mongodb.NewClientMongo(
		context.Background(),
		os.Getenv("MONGO_HOST"),
		os.Getenv("MONGO_PORT"),
		os.Getenv("MONGO_USER"),
		os.Getenv("MONGO_PASSWORD"),
		os.Getenv("SSLMODE"),
	)

	if err != nil {
		fmt.Println(err.Error())
	}

	db := mongodb.NewMongoDB(mongoClient, "users")

	fmt.Println(db)

	// initializing Redis

	// initializing Server

}

func RunServer() {

	// initializing TokenManager

	// initializing Repo

	// initializing Service

	// initializing Handler

}
