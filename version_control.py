#Alejandra Reyes Medina
def encode(password): #Takes user password and encodes it by adding three to each digit. Returns encoded password.
    new_password = ""
    for digit in password:
        if int(digit) >= 7:
            new_password += str((int(digit) + 3) - 10)
        else:
            new_password += str(int(digit) + 3)
    return new_password

def decode(password):
    decoded_password = ''
    for item in password:
        if 3 <= int(item) <= 9:
            decoded_password += str(int(item) - 3)
        elif item == '0':
            decoded_password += '7'
        elif item == '1':
            decoded_password += '8'
        elif item == '2':
            decoded_password += '9'
    return decoded_password

if __name__ == '__main__':
    while True: #Prints and executes menu until user chooses to exit.
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
