#include<stdio.h>
#include<conio.h>
int fibonacci(int n){
    if(n<=1){
        return n;
    }
    else{
        return fibonacci(n-1)+fibonacci(n-2);
    }

}
int main()
{
    int n;
    printf("\n********FIBONACCI SERIES********\n\n");
    printf("Enter the number of elements: ");
    scanf("%d",&n);
    for(int i = 1; i<=n;i++){
        printf("%d\t",fibonacci(i));
    }
    getch();
    return 0;
}
