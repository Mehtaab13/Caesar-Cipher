# Caesar-Cipher

This Python script implements a classic Caesar cipher encryption and decryption tool. <br />
The Caesar cipher shifts each letter in a message by a fixed number of positions down or up the alphabet.

Features
Encryption: Encrypts a message by shifting each letter forward in the alphabet by a specified number of positions.
Decryption: Decrypts an encrypted message by shifting each letter backward in the alphabet by the same number of positions used for encryption.
User Interaction: Simple command-line interface (CLI) that allows users to choose between encoding and decoding messages interactively.
Case Handling: Preserves the case of letters (uppercase remains uppercase, lowercase remains lowercase).
Alphabet Wrapping: Handles wrapping around the alphabet so that shifting beyond 'z' or 'Z' loops back to 'a' or 'A' respectively.
Input Validation: Basic input validation for shift amount (ensuring it is an integer) and message input.
