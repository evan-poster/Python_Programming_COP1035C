#!/usr/bin/env python3
# Week2/Ch4 Exercises/program1.py

"""
Caesar Cipher Encryption

Inputs:
  line: A string of plaintext to encrypt
  distance: The number of characters to shift the text
Output:
  An encrypted string
"""

def caesar_cipher(line, distance):
    """Encrypt a line of plaintext using a Caesar Cipher"""
    encrypted = ""
    for char in line:
        # Convert char to ASCII
        ascii_char = ord(char)
        # Shift ASCII
        if 32 <= ascii_char <= 126:  # All printable ASCII characters
            ascii_char = (ascii_char - 32 + distance) % 95 + 32
        # Convert back to char
        encrypted += chr(ascii_char)
    return encrypted


if __name__ == "__main__":
    line = input("Enter a line of plaintext: ")
    distance = int(input("Enter the distance: "))
    print("Encrypted:", caesar_cipher(line, distance))
