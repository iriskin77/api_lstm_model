# из папки protos
createproto:
	protoc -I proto proto/*.proto --go_out=./genproto --go_opt=paths=source_relative --go-grpc_out=./genproto --go-grpc_opt=paths=source_rel
ative

start:
	go run app/cmd/main.go --config=./app/config/config.yml