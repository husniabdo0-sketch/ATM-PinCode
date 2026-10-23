correct_pin = "1342"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    pin = input("Enter your PIN: ")
    attempts += 1

    if pin == correct_pin:
        print("PIN accepted. Welcome!")
        break

    print("Incorrect PIN.")
    remaining = max_attempts - attempts

    if remaining > 0:
        print("Attempts remaining:", remaining)
else:
    print("Game Over!")