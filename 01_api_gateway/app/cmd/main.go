package main

import (
	"fmt"

	"github.com/iriskin77/api_gateway/app/internal/config"
)

func main() {

	config := config.LoadConfig()

	fmt.Println(config)

}
