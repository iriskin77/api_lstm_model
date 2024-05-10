package auth

import "github.com/google/uuid"

type User struct {
	UUID     string
	Email    string
	Password string
}

type CreateUserDTO struct {
	Email          string `json:"Email,omitempty"`
	Password       string `json:"Password,omitempty"`
	RepeatPassword string `json:"RepeatPassword,omitempty"`
}

func NewUser(dto CreateUserDTO) User {
	return User{
		UUID:     uuid.New().String(),
		Email:    dto.Email,
		Password: dto.Password,
	}
}

type LoginUserDTO struct {
	Email    string
	Password string
}

func LoginUser(dto LoginUserDTO) User {
	return User{
		Email:    dto.Email,
		Password: dto.Password,
	}
}
