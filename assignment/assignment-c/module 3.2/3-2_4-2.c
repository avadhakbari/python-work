
#include <stdio.h>

int main()
{
    char ch;
    
    printf("enter the character :-");
    scanf("%c", &ch);
    
     switch (ch)
    {
        case 'a':
        case 'A':
        case 'e':
        case 'E':
        case 'i':
        case 'I':
        case 'o':
        case 'O':
        case 'u':
        case 'U':
        
        printf("%c this character is vowel", ch);
        break;
        
        default :
        printf("%c this character is consonant", ch);
        break;
        
    }
    
    
    return 0;
}
