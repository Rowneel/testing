#include <stdio.h>

void star()
{
    printf("\n************************************\n");
}

void printMat(int M[][4],int r,int c)
{
    int i,j;
    star();
    printf("Pid\tBT\tWT\tTAT\n");
    for (i = 0; i < r; i++) {
      for (j = 0; j < c; j++) {
         printf("%d\t", M[i][j]);
      }
      printf("\n");
   }
   star();
}

int main()
{
    int M[50][4],n,i,j,index,temp,total,avg_WT,avg_TAT;

    printf("Enter number of rows: ");
    scanf("%d",&n);
    star();
    for (i = 0; i < n; i++)
    {
        printf("P%d: ",i+1);
        scanf("%d",&M[i][1]);
        M[i][0] = i+1;
    }
    
    printMat(M,n,2);

   for (i = 0; i < n; i++) {
        index = i;
        for (j = i + 1; j < n; j++)
            if (M[j][1] < M[index][1])
                index = j;
        temp = M[i][1];
        M[i][1] = M[index][1];
        M[index][1] = temp;
 
        temp = M[i][0];
        M[i][0] = M[index][0];
        M[index][0] = temp;
    }

    printMat(M,n,2);

    M[0][2] = 0;
    for(i = 1;i<n;i++){
        M[i][2]=0;
        for(j = 0;j<i;j++){
            M[i][2] += M[j][1];
            total += M[i][2];
        }
    }
    printMat(M,n,3);
    avg_WT = (float)total/n;
    total = 0;

    for (i = 0; i < n; i++) {
        M[i][3] = M[i][1] + M[i][2];
        total += M[i][3];
    }
    avg_TAT = (float)total / n;
    printMat(M,n,4);
   return 0;
}