package main

import (
	"context"
	"fmt"
	"os"
	"time"

	"github.com/iriskin77/auth_grpc/app/internal/auth"
	"github.com/iriskin77/auth_grpc/app/internal/config"
	"github.com/iriskin77/auth_grpc/app/internal/server"
	"github.com/iriskin77/auth_grpc/app/pkg/jwt_auth"
	"github.com/iriskin77/auth_grpc/app/pkg/logger"
	"github.com/iriskin77/auth_grpc/app/pkg/storage/mongodb"
	"github.com/joho/godotenv"
)

func main() {

	// initializing logger

	logger.Init()
	logger := logger.GetLogger()
	logger.Println("logger initialized")

	// initializing config

	conf := config.LoadConfig("./app/config/config.yml")

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

	//fmt.Println(db)

	// initializing Redis

	// initializing jwt

	tokenManager, err := jwt_auth.NewManager(conf.JWTSecret, time.Duration(conf.AccessTokenTTL)*time.Minute, time.Duration(conf.RefreshTokenTTL)*time.Minute)
	if err != nil {
		logger.Fatal(err)
	}

	// fmt.Println(tokenManager)

	// initializing Repo

	repo := auth.NewRepository(db, &logger)

	// initializing Service

	// serv := auth.NewService(repo)

	// initializing Server

	application := server.NewApp(&logger, conf.GRPC.Port, repo, tokenManager)

	application.MustRun()

}
