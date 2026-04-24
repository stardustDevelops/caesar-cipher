#Caesar_Cipher
#Encode or Decode a message
#Make sure to remember your shift number
#The shift number is your key

mode = input("Would you like to 'encode' or 'decode'? ").strip().lower()

while mode not in ['encode', 'decode']:
    print("Invalid Input")
    mode = input("Would you like to 'encode' or 'decode'? ").strip().lower()

if mode == "encode":
    message = input("What message would you like to encode? ")
else:
    message = input("What message would you like to decode? ")

while True:
    try:
        shift_amount = int(input("What number do you want to shift your letters with? "))
        break
    except ValueError:
        print("Invalid Input")

def encrypt(text, shift):
    shift = shift % 26
    cipher = ""
    for letter in text:
        if 'a' <= letter <= 'z':
            num = ord(letter) - ord("a")
            shifted_number = num + shift
            new_num = shifted_number % 26 + ord("a")
            cipher += chr(new_num)
        elif 'A' <= letter <= 'Z':
            num = ord(letter) - ord("A")
            shifted_number = num + shift
            new_num = shifted_number % 26 + ord("A")
            cipher += chr(new_num)
        else:
            cipher += letter
    return cipher

def decrypt(text, shift):
    return encrypt(text, -shift)

if mode == "encode":
    print(encrypt(message, shift_amount))
elif mode == "decode":
    print(decrypt(message, shift_amount))
