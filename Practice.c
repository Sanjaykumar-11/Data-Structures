// Alphabet count

// #include<stdio.h>
// #include<stdlib.h>
// #include<string.h>
// int main()
// {
//     char S[100000];
//     scanf("%[^\n]", S);
    
//     int arr[128] = {0};
    
//     for(int i=0; i<strlen(S);  i++)
//     {
//         arr[S[i]]++;   
//     }
    
//     for(char ch='A'; ch<='z'; ch++)
//     {
//         if(arr[ch]>0)
//         {
//             printf("%c%d", ch, arr[ch]);
//         }
//     }
// }




//String First Repeating Character

// #include<stdio.h>
// #include<stdlib.h>
// #include<string.h>

// int main()
// {
//     char S[100000];
//     scanf("%s", S);
    
//     int arr[128] = {0};
    
//     for(int i=0; S[i]; i++)
//     {
//         arr[S[i]]++;
//         if(arr[S[i]]>1)
//         {
//             printf("%c", S[i]);
//             break;
//         }
//     }
// }





//Decimal to Binary - Recursive

// #include <stdio.h>
// void toBinary(int val)
// {
//     if(val==0)
//     {
//         return;
//     }
//     toBinary(val/2);
//     printf("%d", val%2);
// }
// int main()
// {
//     int N;
//     scanf("%d", &N);
//     toBinary(N);
//     return 0;
// }



//reverse the string using recursion

// #include <stdio.h>

// void reverse(char str[], int index)
// {
//     if(str[index] != '\0')
//     {
//         reverse(str, index+1); //note that here we use index+1
//         printf("%c", str[index]);
//     }
// }
// int main()
// {
//     char str[1000];
//     scanf("%s", str);
//     reverse(str, 0);
//     return 0;
// }
