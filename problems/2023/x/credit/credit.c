#include <cs50.h>
#include <stdio.h>

int main(void)
{
    long number = get_long("Number: ");
    if((number >= 340000000000000 && number <= 349999999999999) || (number >= 370000000000000 && number <= 379999999999999))
    {
        printf("AMEX\n");
    }
    else if(number >= 5100000000000000 && number <= 5599999999999999)
    {
        printf("MASTERCARD\n");
    }
    else if((number >= 4000000000000 && number <= 4999999999999) || (number >= 4000000000000000 && number <= 4999999999999999))
    {
        printf("VISA\n");
    }
    else
    {
        printf("INVALID\n");
    }
}
