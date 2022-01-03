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







//Prime number 1 to N
// Sieve of Eratosthenes


// #include<stdio.h>
// #include<stdlib.h>

// int main()
// {
//     int N;
//     scanf("%d", &N);
    
//     int prime[N+1];
    
//     for(int i=2; i<=N; i++)
//     {
//         prime[i] = 1;
//     }
    
//     for(int i=2; i*i<=N; i++)
//     {
//         if(prime[i]==1)
//         {
//             for(int j = i*i; j<=N; j=j+i)
//             {
//                 prime[j] = 0;
//             }
//         }
//     }
    
//     for(int i=2; i<=N; i++)
//     {
//         if(prime[i]==1)
//         {
//             printf("%d ", i);
//         }
//     }

// }

// Time complexity: O(n*log(log(n)))







//GCD or HCF - Euclidian algorithm

// #include <stdio.h>
// #include<stdlib.h>
// #define ULL unsigned long long int

// ULL hcf(ULL a, ULL b)
// {
//     if(b==0)
//     {
//         return a;
//     }
//     else
//     {
//         hcf(b, a%b);
//     }
// }

// int main()
// {
//     int n;
//     scanf("%d", &n);
    
//     ULL ans, current;
//     scanf("%llu", &ans);
    
//     for(int i=2; i<=n; i++)
//     {
//         scanf("%llu", &current);
//         ans = hcf(ans, current);
//     }
//     printf("%llu", ans);
// }