from KeyGen import RSAKeyGenerator
while(True):
    print("Type 'exit' to exit the program")
    print("Type 'generate' to generate a new RSA key pair")
    option = input("Enter an option: ")
    if option == 'exit':
        break
    elif option == 'generate':
        pin = input("Enter a pin: ")
        if not pin.isdigit():
            print("The pin must only contain numbers and be longer than 0 digits")
            continue
        key_gen = RSAKeyGenerator(pin)
        key_gen.generate_keys()
        key_gen.save_keys()
        print("Keys generated successfully")
    else:
        print("Invalid option")