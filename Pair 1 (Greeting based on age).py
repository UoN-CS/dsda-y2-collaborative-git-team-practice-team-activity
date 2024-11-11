name = input("What is your name?")
age = int(input(f"Nice name {name}! What is your age? "))
if age < 18:
    print(f"Hello {name}, you are not an adult")
elif age >= 18:
    print(f"Hello {name}, you are an adult")
