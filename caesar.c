#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    // checks for single argv
    if (argc == 1)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    // convert argv[1] to int
    int j = atoi(argv[1]);

    char *arg = argv[1];
    for (int k = 0; k < strlen(argv[1]); k++)

        if (isdigit(arg[k]))
        {
            continue;
        }
        else
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }

    if (argc == 2)
    {
        int change = atoi(argv[1]);
        // reduce key bellow 26
        change = change % 26;

        string phrase = get_string("plaintext: ");

        printf("\n");
        printf("ciphertext: ");

        for (int i = 0; i < strlen(phrase); i++)
        {
            char work = phrase[i];
            // leave spaces unchanged
            if (isspace(work))
            {
                printf("%c", phrase[i]);
            }

            else
            {
                // uppercase
                if (work < 91 && work > 64)
                {
                    if ((work + change) > 90)
                    {
                        work = work - 26;
                    }
                    printf("%c", work + change);
                }
                // lowercase
                else if (work < 123 && work > 96)
                {
                    if ((work + change) > 122)
                    {
                        work = work - 26;
                    }
                    printf("%c", work + change);
                }
                // punctuation
                else
                {
                    printf("%c", work);
                }
            }
        }
        printf("\n");
        return 0;
    }
    else
    {
        printf("Usage: ./caesar key\n");
        return 1;

    }

}
