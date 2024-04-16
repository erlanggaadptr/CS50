from validator_collection import validators, errors


def main():
    try:
        email_address = validators.email(input("What's your email address? "))

    except errors.InvalidEmailError:
        print("Invalid")

    else:
        print("Valid")


if __name__ == "__main__":
    main()
