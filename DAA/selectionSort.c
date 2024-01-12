#include<stdio.h>
#include<conio.h>
int main(){
    int a[]={7,4,10,8,3,1};
    int min,i,j,n=6;
    printf("\n*********SELECTION SORT********\n\n");
    printf("The array elements are: \n");
    for(i=0;i<n;i++){
        printf("%d\t",a[i]);
    }
    printf("\n\nThe sorted array elements are: \n");
    for(i=0;i<n-1;i++){
        min = i;
        for(j = i+1; j<n;j++){
            if(a[j]<a[min]){
                min = j;
            }
        }
        if(min!=i){
            int temp = a[i];
            a[i] = a[min];
            a[min] = temp;
        }
    }
    for(i=0;i<n;i++){
        printf("%d\t",a[i]);
    }
    getch();
    return 0;
}

