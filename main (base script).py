def greet_user(name):
    """Greets the user by name."""
    print(f"Hello, {name}!")

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    greet_user(user_name)
