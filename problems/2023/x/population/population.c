#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompting the user for a starting # of llamas
    int starting;
    do
    {
        starting = get_int("Starting # of llamas: ");
    }
    while (starting < 9);
    // Prompting them for an ending # of llamas
    int ending;
    do
    {
        ending = get_int("Ending # of llamas: ");
    }
    while (ending < starting);
    // Each year, n / 3 new llamas are born, and n / 4 llamas pass away
    // Calculate the number of years it takes to reach the goal number of llamas
    int years;
    for (years = 0; starting < ending; years++)
    {
        starting += (starting / 3) - (starting / 4);
    }
    printf("Years: %i\n", years);
}
