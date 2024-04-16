VOWELS = [
    'A', 'I', 'U', 'E', 'O',
    'a', 'i', 'u', 'e', 'o'
    ]

input = input("Input: ")
output = ''.join([char for char in input if char not in VOWELS])

print(f"Output: {output}")
