# App that encodes a password given by the user, and also returns the decoded form of the password

# App done by:
# Gustavo Rincon UF ID: 84657241
# Kyle Partridge
# Group 40 

#global variable
encoded_password = ""

#encoder function done by Gustavo
def encoder(og_password):
    
    #reset the encoded password variable
    encoded_password = ""

    # loop over the password provided, and shift the numbers up by 3. 0-9
    for digit in og_password:

        if int(digit) == 9:
            encoded_password += "2"
        elif int(digit) == 8:
            encoded_password += "1"
        elif int(digit) == 7:
            encoded_password += "0"
        else:
            encoded_password += str(int(digit)+3)
    
    return encoded_password


#deceoder function done bu Kyle
def decoder(encoded_password):
    pass


def main():

    # loops that prints menue and also controls the program's function of encoder and decoder
    while True:
        
        # Menu to the user
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        
        selection = int(input("Please enter an option:"))

        # if user selects 1, then ask user for a password to encode
        if selection == 1:
            
            #asking used for the password to encode, then make the type be a string, then pass to the encoder function
            encoded_password = encoder(str(input("Please enter your password to encode:")))
            
            #print back the confirmation to the user
            print("Your password has been encoded and stored!\n") 

            # jump to the next loop
            continue

        # if user selects 2, then print the encoded and decoded password
        elif selection == 2:
            
            # prints back to the user the encoded password and the decoded password
            print(f"The encoded password is {encoded_password}, and the original password is {decoder(encoded_password)}.\n")

        
        # if user selects 3, exit program entirely
        elif selection == 3:
            exit()



if __name__ == "__main__":
    main()