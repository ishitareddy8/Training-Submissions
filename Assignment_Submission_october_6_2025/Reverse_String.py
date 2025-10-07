def reverse_string(s: str) -> str:
    return s[::-1]

if __name__ == "__main__":
    text = input("Enter a string to reverse: ")
    print("Reversed string:", reverse_string(text))
