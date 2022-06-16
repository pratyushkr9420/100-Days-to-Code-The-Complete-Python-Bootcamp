logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

def caesar(start_text,shift_amount,cipher_direction):
    end_text = ""
    if cipher_direction == 'encode':
        for char in start_text:
            if char in alphabet:
                position = alphabet.index(char)
                end_text += alphabet[position + shift_amount]
            else:
                end_text += char
    elif cipher_direction == 'decode':
        for char in start_text:
            if char in alphabet:
                position = alphabet.index(char)
                end_text += alphabet[position -shift_amount]
            else:
                end_text += char

    print(f"The {cipher_direction}d word is {end_text}")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                'q', 'r', 's', 't', 'u', 'v','w', 'x', 'y', 'z']

# TODO-0: Original list of a-z was doubled in order to ensure there is no error when a word has letters like x, y , z
# TODO-0: (continued) so that when you shift during enryption you don't run out of indices in the alphabet list.

status=True

print(logo)

while status:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(start_text=text,shift_amount=shift,cipher_direction=direction)
    result = input("Type 'Yes' if you want to continue or 'No' if you want to exit\n").lower()
    if result == 'yes':
        pass
    elif result == 'no':
        status = False
