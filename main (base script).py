# Saving to log.txt file
def log_to_file(greeting: str, number: float, square: float):
    with open("log.txt", "a") as file:
        file.write(f"{greeting}\n")
        file.write(f"The square of {number} is {square}\n")

def main():
    # name, age = get_user_info()
    # greeting = greet_user(name, age)
    # number, square = get_number_and_square()
    log_to_file("greeting", 1, 1)
 
if __name__ == "__main__":
    main()