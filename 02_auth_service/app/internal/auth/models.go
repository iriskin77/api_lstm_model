package auth

import (
	"fmt"

	"golang.org/x/crypto/bcrypt"
)

// User structs and methods

type User struct {
	UUID     string
	Email    string
	Password string
}

func (u *User) GeneratePasswordHash() error {
	pwd, err := generatePasswordHash(u.Password)
	if err != nil {
		return err
	}
	u.Password = pwd
	return nil
}

func generatePasswordHash(password string) (string, error) {
	hash, err := bcrypt.GenerateFromPassword([]byte(password), bcrypt.MinCost)
	if err != nil {
		return "", fmt.Errorf("failed to hash password due to error %w", err)
	}
	return string(hash), nil
}

// UserCreateDTO structs and methods

type UserCreateDTO struct {
	Email            string
	Password         string
	RepeatedPassword string
}

func NewUserCreateDTO(email, password, repeatedPassword string) (*UserCreateDTO, error) {
	return &UserCreateDTO{
		Email:            email,
		Password:         password,
		RepeatedPassword: repeatedPassword,
	}, nil
}

func NewUser(dto *UserCreateDTO) (*User, error) {

	return &User{
		Email:    dto.Email,
		Password: dto.Password,
	}, nil
}

type UserLoginDTO struct {
	Email    string
	Password string
}

func NewUserLoginDTO(email, password string) (*UserLoginDTO, error) {
	return &UserLoginDTO{
		Email:    email,
		Password: password,
	}, nil
}

func (dto *UserLoginDTO) CheckPassword(inputPassword string) error {
	err := bcrypt.CompareHashAndPassword([]byte(inputPassword), []byte(dto.Password))
	if err != nil {
		return fmt.Errorf("password does not match")
	}
	return nil
}
