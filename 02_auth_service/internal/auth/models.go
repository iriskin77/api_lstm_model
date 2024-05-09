package auth

type User struct {
	UUID     string
	Email    string
	Password []byte
}
