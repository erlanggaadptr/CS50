#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

bool only_digits(string arg);

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    if (!only_digits(argv[1]))
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    int key = atoi(argv[1]);
    string plaintext = get_string("plaintext: ");
    printf("ciphertext: ");

    for (int i = 0; i < strlen(plaintext); i++)
    {
        if (isupper(plaintext[i]))
        {
            printf("%c", (plaintext[i] - 65 + key) % 26 + 65);
        }
        else if (islower(plaintext[i]))
        {
            printf("%c", (plaintext[i] - 97 + key) % 26 + 97);
        }
        else
        {
            printf("%c", (plaintext[i]));
        }
    }
    printf("\n");
}

bool only_digits(string arg)
{
    for (int i = 0; i < strlen(arg); i++)
    {
        if (!isdigit(arg[i]))
        {
            return false;
        }
    }
    return true;
}

// char rotate(char c, int n)
// {
//     for (int i = 0; i < strlen(plaintext); i++)
//     {
//         if (isupper(plaintext[i]))
//         {
//             printf("%c", (plaintext[i] - 65 + key) % 26 + 65);
//         }
//         else if (islower(plaintext[i]))
//         {
//             printf("%c", (plaintext[i] - 97 + key) % 26 + 97);
//         }
//         else {
//             printf("%c", (plaintext[i]);
//         }
//     }
//     printf("\n");
// }
