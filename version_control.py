#Alejandra Reyes Medina
def encode(password): #Takes user password and encodes it by adding three to each digit. Returns encoded password.
    new_password = ""
    for digit in password:
        if int(digit) >= 7:
            new_password += str((int(digit) % 7 + 3) - 10)
        else:
            new_password += str(int(digit) + 3)
    return new_password

def decode(password):
    pass

if __name__ == '__main__':
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Exit\n")

        menu_option = int(input("Please enter an option: "))
        if menu_option == 1:
            user_password = input("Please enter your password to encode: ")
            encoded_password = encode(user_password)
            print("Your password has been encoded and stored!")
        elif menu_option == 2:
            original_password = decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {original_password}.")
        elif menu_option == 3:
            break
