# Ceasar Cipher

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

spec_char = ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/', ' ']

def encode_message(text, shift):
    '''
        Function to enncode letters with shift
    '''
    
    encrypted_word =''

    for letters in  text:
        if letters in spec_char:
            new_letter = letters
        else:
            letter_position = alphabet.index(letters)
            
            if letter_position + shift <= 26:
                new_letter = alphabet[letter_position + shift]
            else:
                new_letter = alphabet[letter_position + shift - 26]                                
         
        encrypted_word += new_letter
    
    return encrypted_word



if __name__ == '__main__':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == 'encode':
        print(f'Encrpted Message is : {encode_message(text, shift)}')