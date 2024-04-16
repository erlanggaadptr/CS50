// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 500;

// Hash table
node *table[N];

int count = 0;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    int index = hash(word);
    node *cursor = table[index];
    while (cursor->next != NULL)
    {
        if (strcasecmp(word, cursor->word) == 0)
            return true;

        cursor = cursor->next;
    }

    if (strcasecmp(word, cursor->word) == 0)
        return true;
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    int sum = 0;
    for (int i = 0; i < strlen(word); i++)
        sum += (int) word[i] - word[i];
    return sum;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    // Open dictionary file
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
        return false;

    // Read strings from file one at a time
    char string[LENGTH + 1];
    int index;

    while (fscanf(file, "%s", string) != EOF)
    {
        // Create a new node for each word
        node *n = malloc(sizeof(node));

        if (n == NULL)
            return false;

        // Hash word to obtain a hash value
        index = hash(string);

        // Set the next pointer
        if (table[index] != NULL)
            n->next = table[index];
        else
            n->next = NULL;

        // Insert node into hash table at that location
        table[index] = n;

        // Copy word into node
        strcpy(n->word, string);
        count++;
    }
    fclose(file);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    if (count != 0)
        return count;
    else
        return 0;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    node *cursor;
    for (int i = 0; i < N; i++)
    {
        cursor = table[i];
        while (table[i] != NULL)
        {
            table[i] = cursor->next;
            free(cursor);
            cursor = table[i];
        }

        if (table[i] != NULL)
            return false;
    }
    return true;
}
