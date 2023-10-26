"""
Authors: Claire Wang
Purpose: Create an encode() and main() function that encodes a user input password
Date: 10/25/2023
"""

def encode(to_encode):
    encoded_value = ""
    for num in to_encode:
        num = int(num)
        new_value = num + 3
        encoded_value += str(new_value)
    return encoded_value


def main():
    runMenu = True
    while runMenu:
        print("Menu\n-------------")
        print("1. Encode\n2. Decode\n3. Quit")
        option = int(input("\nPlease enter an option: "))
        if option == 1:
            input_to_encode = input("Please enter your password to encode: ")
            encoded_password = encode(input_to_encode)
            print("Your password has been encoded and stored!\n")
        elif option == 2:
            print(f"The encoded password is {encoded_password}, and the original password is {decode(encoded_password)}.")
        elif option == 3:
            runMenu = False


if __name__ == "__main__":
    main()