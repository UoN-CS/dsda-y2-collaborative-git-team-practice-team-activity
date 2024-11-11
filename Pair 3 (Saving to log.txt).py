def save_to_log(name, age, square):
    """Saves user data to a log file."""
    with open("log.txt", "a") as log_file:
        log_file.write(f"{name} (age {age}): Square of {square}\n")

if __name__ == "__main__":
    # ... (use the functions from Pair 1 and Pair 2)
    save_to_log(user_name, user_age, result)
