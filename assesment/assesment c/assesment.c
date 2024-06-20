#include <stdio.h>
#include <string.h>
#include <ctype.h>

// Function to reverse a string
void reverseString(char str[]) 
{
    int length = strlen(str);
    for (int i = 0; i < length / 2; i++) 
    {
        char temp = str[i];
        str[i] = str[length - i - 1];
        str[length - i - 1] = temp;
    }
    printf("Reversed string: %s\n", str);
}

// Function to concatenate two strings
void concatenateStrings(char str1[], char str2[]) 
{
    strcat(str1, str2);
    printf("Concatenated string: %s\n", str1);
}

// Function to check if a string is a palindrome
int isPalindrome(char str[]) 
{
    int length = strlen(str);
    for (int i = 0; i < length / 2; i++) 
    {
        if (str[i] != str[length - i - 1]) 
        {
            return 0; // Not a palindrome
        }
    }
    return 1; // Palindrome
}

// Function to copy a string
void copyString(char destination[], char source[]) 
{
    strcpy(destination, source);
    printf("Copied string: %s\n", destination);
}

// Function to get the length of a string
int stringLength(char str[])
{
    return strlen(str);
}

// Function to count the frequency of each character in a string
void characterFrequency(char str[]) 
{
    int frequency[256] = {0};
    int length = strlen(str);

    for (int i = 0; i < length; i++) 
    {
        frequency[str[i]]++;
    }

    printf("Character frequency:\n");
    for (int i = 0; i < 256; i++) 
    {
        if (frequency[i] > 0)
        {
            printf("%c: %d\n", i, frequency[i]);
        }
    }
}

// Function to count the number of vowels and consonants in a string
void countVowelsConsonants(char str[])
{
    int vowels = 0, consonants = 0;
    int length = strlen(str);

    for (int i = 0; i < length; i++) 
    {
        char currentChar = tolower(str[i]);

        if (currentChar >= 'a' && currentChar <= 'z') 
        {
            if (currentChar == 'a' || currentChar == 'e' || currentChar == 'i' || currentChar == 'o' || currentChar == 'u')
            {
                vowels++;
            }
            else 
            {
                consonants++;
            }
        }
    }

    printf("Number of vowels: %d\n", vowels);
    printf("Number of consonants: %d\n", consonants);
}

// Function to count the number of blank spaces and digits in a string
void countSpacesDigits(char str[])
{
    int spaces = 0, digits = 0;
    int length = strlen(str);

    for (int i = 0; i < length; i++) 
    {
        if (isspace(str[i])) 
        {
            spaces++;
        } else if (isdigit(str[i])) 
        {
            digits++;
        }
    }   

    printf("Number of blank spaces: %d\n", spaces);
    printf("Number of digits: %d\n", digits);
}

int main() 
{
    char inputString[100];

    while (1) {
        printf("\nString Operations Menu:\n");
        printf("1. Reverse a string\n");
        printf("2. Concatenate strings\n");
        printf("3. Check palindrome\n");
        printf("4. Copy a string\n");
        printf("5. Length of the string\n");
        printf("6. Character frequency in the string\n");
        printf("7. Count vowels and consonants\n");
        printf("8. Count spaces and digits\n");
        printf("9. Exit\n");

        int choice;
        printf("Enter your choice (1-9): ");
        scanf("%d", &choice);

        switch (choice) 
        {
            case 1:
                printf("Enter the string: ");
                scanf("%s", inputString);
                reverseString(inputString);
                break;

            case 2:
                printf("Enter the first string: ");
                scanf("%s", inputString);
                char secondString[50];
                printf("Enter the second string: ");
                scanf("%s", secondString);
                concatenateStrings(inputString, secondString);
                break;

            case 3:
                printf("Enter the string: ");
                scanf("%s", inputString);
                if (isPalindrome(inputString)) {
                    printf("Is Palindrome: Yes\n");
                } else {
                    printf("Is Palindrome: No\n");
                }
                break;

            case 4:
                printf("Enter the string: ");
                scanf("%s", inputString);
                char copiedString[100];
                copyString(copiedString, inputString);
                break;

            case 5:
                printf("Enter the string: ");
                scanf("%s", inputString);
                printf("Length of the string: %d\n", stringLength(inputString));
                break;

            case 6:
                printf("Enter the string: ");
                scanf("%s", inputString);
                characterFrequency(inputString);
                break;

            case 7:
                printf("Enter the string: ");
                scanf("%s", inputString);
                countVowelsConsonants(inputString);
                break;

            case 8:
                printf("Enter the string: ");
                scanf("%s", inputString);
                countSpacesDigits(inputString);
                break;

            case 9:
                printf("Exiting the program. Goodbye!\n");
                return 0;

            default:
                printf("Invalid choice. Please enter a number between 1 and 9.\n");
        }

        char continueFlag[3];
        printf("Do you want to perform another operation? (yes/no): ");
        scanf("%s", continueFlag);
        if (strcmp(continueFlag, "no") == 0) 
        {
            printf("Exiting the program. Goodbye!\n");
            break;
        }
    }

    return 0;
}
