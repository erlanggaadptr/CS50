#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j].rgbtRed = image[i][j].rgbtGreen = image[i][j].rgbtBlue =
                round((float) (image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue) / 3);
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    float sepiaRed, sepiaGreen, sepiaBlue;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            sepiaRed = round(.393 * image[i][j].rgbtRed + .769 * image[i][j].rgbtGreen + .189 * image[i][j].rgbtBlue);
            sepiaGreen = round(.349 * image[i][j].rgbtRed + .686 * image[i][j].rgbtGreen + .168 * image[i][j].rgbtBlue);
            sepiaBlue = round(.272 * image[i][j].rgbtRed + .534 * image[i][j].rgbtGreen + .131 * image[i][j].rgbtBlue);

            if (sepiaRed > 255)
                sepiaRed = 255;

            if (sepiaGreen > 255)
                sepiaGreen = 255;

            if (sepiaBlue > 255)
                sepiaBlue = 255;

            image[i][j].rgbtRed = sepiaRed;
            image[i][j].rgbtGreen = sepiaGreen;
            image[i][j].rgbtBlue = sepiaBlue;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE tempPixel;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0, k = width - 1; j < k; j++, k--)
        {
            tempPixel = image[i][j];
            image[i][j] = image[i][k];
            image[i][k] = tempPixel;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copy[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
            copy[i][j] = image[i][j];
    }

    float totalRed, totalGreen, totalBlue, totalPixel;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            totalRed = totalGreen = totalBlue = totalPixel = 0;
            for (int k = i - 1; k <= i + 1; k++)
            {
                for (int l = j - 1; l <= j + 1; l++)
                {
                    if ((k >= 0 && l >= 0) && (k < height && l < width))
                    {
                        totalRed += copy[k][l].rgbtRed;
                        totalGreen += copy[k][l].rgbtGreen;
                        totalBlue += copy[k][l].rgbtBlue;
                        totalPixel++;
                    }
                    else
                        continue;
                }
            }
            image[i][j].rgbtRed = round(totalRed / totalPixel);
            image[i][j].rgbtGreen = round(totalGreen / totalPixel);
            image[i][j].rgbtBlue = round(totalBlue / totalPixel);
        }
    }
    return;
}
