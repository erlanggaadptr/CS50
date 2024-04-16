def main():
    text = input("Text: ")
    L = 100 * (float(count_letters(text)) / float(count_words(text)))
    S = 100 * (float(count_sentences(text)) / float(count_words(text)))
    index = round(0.0588 * L - 0.296 * S - 15.8)

    if index < 1:
        print("Before Grade 1")
    elif index > 16:
        print("Grade 16+")
    else:
        print(f"Grade {index}")


def count_letters(text):
    count = 0
    for i in text:
        if i.isalpha():
            count += 1
    return count


def count_words(text):
    return len(text.split(" "))


def count_sentences(text):
    count = 0
    for i in text:
        if i == "." or i == "!" or i == "?":
            count += 1
    return count


if __name__ == "__main__":
    main()
