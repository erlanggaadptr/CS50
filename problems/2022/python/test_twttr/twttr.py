VOWELS = [
    'A', 'I', 'U', 'E', 'O',
    'a', 'i', 'u', 'e', 'o'
    ]


def main():
    words = input("Input: ")
    print(f"Output: {shorten(words)}")


def shorten(words):
    return ''.join([word for word in words if word not in VOWELS])


if __name__ == "__main__":
    main()
