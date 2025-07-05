import pyperclip

def encode(message):
    secret = ""
    for char in message:
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            encoded = (ord(char) - base + 3) % 26 + base
            secret += chr(encoded)
        else:
            secret += char
    pyperclip.copy(secret)
    print("✅ Encoded Message:", secret)
    print("📋 Copied to clipboard.")

def decode(message):
    original = ""
    for char in message:
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            decoded = (ord(char) - base - 3) % 26 + base
            original += chr(decoded)
        else:
            original += char
    pyperclip.copy(original)
    print("✅ Decoded Message:", original)
    print("📋 Copied to clipboard.")

def main():
    while True:
        print("\n=== MESSAGE ENCODER & DECODER ===")
        print("1. Encode a message")
        print("2. Decode a message")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            msg = input("Enter your message to ENCODE: ")
            encode(msg)

        elif choice == '2':
            msg = input("Enter your message to DECODE: ")
            decode(msg)

        elif choice == '3':
            print("👋 Exiting. Goodbye!")
            break
        else:
            print("❌ Invalid option. Try again.")

if __name__ == "__main__":
    main()
