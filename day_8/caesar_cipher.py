# Ceasar Cipher
import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

spec_char = ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/', ' ', '0','1', '2' , '3', '4', '5', '6', '7', '8', '9']

def encode_decode_message(text, shift, direction):
    '''
        Function to enncode with shift
    '''
    
    encrypt_decrypt_word =''

    if shift > 26:
        shift = shift % 26

    if direction == 'e' or direction == 'd':
        
        for letters in  text:
            # Check for Special Characters 
            if letters in spec_char:
                new_letter = letters
            else:
                # Find the letter position
                letter_position = alphabet.index(letters)
                
                # Logic for Encoding
                if direction == 'e':
                    if letter_position + shift < 26:
                        new_letter = alphabet[letter_position + shift]
                    else:
                        new_letter = alphabet[letter_position + shift - 26]      
                
                # Logic for Decoding
                else:
                    if letter_position - shift >= 0:
                        new_letter = alphabet[letter_position - shift ]
                    else:
                        new_letter = alphabet[letter_position - shift + 26 ]                             
            
            encrypt_decrypt_word += new_letter
        return encrypt_decrypt_word
    else:
        return 'Incorrect Choice'
    

if __name__ == '__main__':
    ''' Main Function '''
    print(art.logo)
    usr_option = 'yes'
    while usr_option != 'no':
        direction = input("Type 'encode (e) ' to encrypt, type 'decode (d) ' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        print(f'You choose {direction}. Result - {encode_decode_message(text, shift, direction)}')
        usr_option = input('Want to try again(yes/no). Type no to exit : ').lower()
    print('Thank you for trying the Caesar Cipher!')