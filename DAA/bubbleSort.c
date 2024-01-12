#include<stdio.h>
#include<conio.h>
int main()
{
    int a[]= {7,4,10,8,3,1};
    int i,j,n=6;
    printf("\n*********BUBBLE SORT********\n\n");
    printf("The array elements are: \n");
    for(i=0; i<n; i++)
    {
        printf("%d\t",a[i]);
    }
    printf("\n\nThe sorted array elements are: \n");
    for(i=0; i<n-1; i++)
    {
        for(j=0; j<n-i-1; j++)
        {
            if(a[j]>a[j+1])
            {
                int temp = a[j];
                a[j] = a[j+1];
                a[j+1] = temp;
            }
        }
    }
    for(i=0; i<n; i++)
    {
        printf("%d\t",a[i]);
    }
    getch();
    return 0;
}


