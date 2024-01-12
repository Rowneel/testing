#include<stdio.h>
#include<conio.h>
int main(){
    int a[]={25,57,48,37,12,92,86,33};
    int x,i,j,n=8;
    printf("\n*********INSERTION SORT********\n\n");
    printf("The array elements are: \n");
    for(i=0;i<n;i++){
        printf("%d\t",a[i]);
    }
    printf("\n\nThe sorted array elements are: \n");
    for(i=1;i<n;i++){
        x = a[i];
        j = i-1;
        while(j>=0&&a[j]>x){
            a[j+1] = a[j];
            j = j-1;
        }
        a[j+1] = x;
    }
    for(i=0;i<n;i++){
        printf("%d\t",a[i]);
    }
    getch();
    return 0;
}
