#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// void mixedCongruential(int n,int x0, int a, int c, int m, double Arr[]){
//     for (int i = 0; i < n; i++)
//     {
//         x0 = (a*x0 + c) % m;
//         Arr[i] = (double)x0/m;
//     }
// }

double* mixedCongruential(int n,int x0, int a, int c, int m){
    double* Arr = (double*)malloc(n * sizeof(double));
    for (int i = 0; i < n; i++)
    {
        x0 = (a*x0 + c) % m;
        Arr[i] = (double)x0/m;
    }
    return Arr;
}


int main() {
    int i, a = 1093, c = 18257, m = 86436 ,drops = 2000;
    double pi;
    double x0=66;   //seed for generating x-coordinates
    double y0=45;   //seed for generating y-coordinates
    double* xtemp = mixedCongruential(drops,x0,a,c,m);
    double* ytemp = mixedCongruential(drops,y0,a,c,m);

    int isInside=0;
    for(i=0;i<drops;i++){
        double s=pow(xtemp[i],2)+pow(ytemp[i],2);
        if(s<=1.0){
            isInside++;
        }
    }
    free(xtemp);
    free(ytemp);
    pi = 4*(double)isInside/drops;
    printf("The approximate value of PI with %d pin drops is %f\n", drops, pi);
    return 0;
}
