# из ./01_api_gateway/app/internal/clients/file_service/protos
createproto_fileservice:
	protoc -I proto proto/*.proto --go_out=./genproto --go_opt=paths=source_relative --go-grpc_out=./genproto --go-grpc_opt=paths=source_relative --experimental_allow_proto3_optional


# флаг --experimental_allow_proto3_optional нужен, чтобы устанавливать опциональные поля

# из ./01_api_gateway/app/internal/clients/auth_service/protos
createproto_authservice:
	protoc -I proto proto/*.proto --go_out=./genproto --go_opt=paths=source_relative --go-grpc_out=./genproto --go-grpc_opt=paths=source_relative --experimental_allow_proto3_optional


start:
	go run app/cmd/main.go --config=./app/config/config.yml