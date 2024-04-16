#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

const int BLOCK_SIZE = 512;
typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }

    char *infile = argv[1];
    FILE *input = fopen(infile, "r");
    if (input == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    BYTE buffer[BLOCK_SIZE];

    int hundreds, tens, ones;
    hundreds = tens = ones = 0;

    FILE *output = NULL;

    bool insideFile = false;

    while (fread(buffer, 1, BLOCK_SIZE, input) == BLOCK_SIZE)
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] >= 0xe0 && buffer[3] <= 0xef))
        {
            if (output != NULL)
            {
                fclose(output);

                ones++;
                if (ones > 9)
                {
                    ones = 0;
                    tens++;
                }
            }

            char fileName[8];
            sprintf(fileName, "%d%d%d.jpg", hundreds, tens, ones);

            char *outfile = fileName;

            output = fopen(outfile, "a");
            if (output == NULL)
            {
                printf("Could not create file.\n");
                return 1;
            }
        }

        if (output != NULL)
            fwrite(buffer, 1, BLOCK_SIZE, output);
    }

    fclose(input);
    fclose(output);
}
