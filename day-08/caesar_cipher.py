# Program to emulate a simple Caesar Cipher
import caesar_alphabet

alphabet = caesar_alphabet.alphabet


def caesar(input_text, shift_amount, crypt_direction):
    output_text = ""
    if crypt_direction == "decode":
        shift_amount *= -1
    for char in input_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            output_text += alphabet[new_position]
        else:
            output_text += char
    print(f"\nThe {crypt_direction}d message is:\n{output_text}")


go_again = False

while not go_again:
    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("\nType your message:\n").lower()
    shift = int(input("\nEnter the shift number to apply to the message:\n"))
    shift = shift % 25

    caesar(input_text=text, shift_amount=shift, crypt_direction=direction)

    continue_prompt = input(
        "\nType 'yes' to encode/decode another message. Else type 'no'.\n"
    )
    if continue_prompt == "no":
        go_again = True
        print("\nGoodbye.")
