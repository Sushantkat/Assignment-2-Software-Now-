def separate_and_convert(s):
    # Separating into number and letter substrings
    number_substring = ''.join(c for c in s if c.isdigit())
    letter_substring = ''.join(c for c in s if c.isalpha())

    # Converting even numbers in the number substring to ASCII Code Decimal values
    even_numbers = [int(n) for n in number_substring if int(n) % 2 == 0]
    even_numbers_ascii = [ord(str(num)) for num in even_numbers]

    # Converting upper-case letters in the letter substring to ASCII Code Decimal values
    upper_case_letters = [c for c in letter_substring if c.isupper()]
    upper_case_letters_ascii = [ord(letter) for letter in upper_case_letters]

    return ''.join(map(str, even_numbers)), even_numbers_ascii, ''.join(upper_case_letters), upper_case_letters_ascii

input_string = '56aAww1984sktr23527@aymn145ss785fsq31D0'
number_string, even_numbers_ascii, letter_string, upper_case_letters_ascii = separate_and_convert(input_string)

print(f'Number Substring: {number_string}')
print(f'Even Numbers ASCII: {even_numbers_ascii}')
print(f'Letter Substring: {letter_string}')
print(f'Upper-case Letters ASCII: {upper_case_letters_ascii}')

#next
def decrypt(ciphertext, shift):
    decrypted_text = ''
    for char in ciphertext:
        if char.isalpha():
            # Determining if the character is uppercase or lowercase
            is_upper = char.isupper()
            
            # Applying the shift and wrap around if needed
            decrypted_char = chr((ord(char) - shift - ord('A' if is_upper else 'a')) % 26 + ord('A' if is_upper else 'a'))
            
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    
    return decrypted_text

def find_shift_key(ciphertext):
    # Trying different shift values and print the decrypted text
    for shift in range(1, 26):
        decrypted_text = decrypt(ciphertext, shift)
        print(f"Shift {shift}: {decrypted_text}")

# Given cryptogram
cryptogram = "VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR ZVFGNXRF V NZ BHG BS PBAGEBY NAQNG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF URYYQBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR"

# Finding the shift key
find_shift_key(cryptogram)
