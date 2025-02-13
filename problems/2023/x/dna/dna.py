import csv
import sys


def main():
    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py data.csv sequence.txt")

    # TODO: Read database file into a variable
    database = []
    with open(sys.argv[1]) as database_file:
        database = list(csv.DictReader(database_file))

    # TODO: Read DNA sequence file into a variable
    sequence = ""
    with open(sys.argv[2]) as sequence_file:
        sequence = sequence_file.read().rstrip("\n")

    # TODO: Find longest match of each STR in DNA sequence
    subsequence = [key for key in database[0] if key != "name"]

    longest = []
    for i in range(len(subsequence)):
        longest.append(str(longest_match(sequence, subsequence[i])))

    # TODO: Check database for matching profiles
    check = []
    for person in range(len(database)):
        for tandem in range(len(subsequence)):
            check.append(database[person][subsequence[tandem]])
        if check == longest:
            print(database[person]["name"])
            return
        else:
            check.clear()
            continue
    print("No match")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):
        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:
            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
