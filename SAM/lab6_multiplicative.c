#include <stdio.h>
#include <stdlib.h>
int mixedCongruential(int n){
    int x0, a, m;
    printf("Enter x0: ");
    scanf("%d",&x0);
    printf("Enter a: ");
    scanf("%d",&a);
    printf("Enter m: ");
    scanf("%d",&m);
    int* Arr = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; i++)
    {
        x0 = (a*x0) % m;
        Arr[i] = x0;
    }
    printf("The random numbers using multiplicative congruential method are: \n");
    for (int i = 0; i < n; i++)
    {
        printf("%04d ",Arr[i]);
    }
    free(Arr);
}

int main(){
    int n;
    printf("Enter how many number you want? ");
    scanf("%d",&n);
    mixedCongruential(n);
    return 0;
}