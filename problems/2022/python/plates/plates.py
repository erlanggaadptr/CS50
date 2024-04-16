# “All vanity plates must start with at least two letters.”
# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
# “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
# “No periods, spaces, or punctuation marks are allowed.”

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    check = [False, False, False, False]

    # Requirement #1
    try:
        if s[0].isalpha() and s[1].isalpha():
            check[0] = True
    except IndexError:
        pass

    # Requirement #2
    if 2 <= len(s) <= 6:
        check[1] = True

    # Requirement #3
    if s[int(len(s) / 2)].isdigit():
        if s[len(s) - 1].isdigit():
            for c in s[int(len(s) / 2):]:
                if c.isdigit():
                    if c != '0':
                        check[2] = True
                        break
                    else:
                        break
    else:
        check[2] = True

    # Requirement #4
    if s.isalnum():
        check[3] = True

    if all(check):
        return True
    else:
        return False

main()
