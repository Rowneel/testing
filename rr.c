#include <stdio.h>

int main() {
    int sum, i, wt = 0, tat = 0;
    float avgwt, avgtat;
    int temp[20], bt[] = {8, 2, 7, 3, 5};
    int count = sizeof(bt) / sizeof(bt[0]);
    int y = count;
    int q = 2;
    printf("\nProcess\t\tBT\t\tTAT\t\tWT\n");
    for (i = 0; i < count; i++) {
        temp[i] = bt[i];
    }
    
    for (sum = 0, i = 0; y != 0;) {
        if (temp[i] <= q && temp[i] > 0) {
            sum += temp[i];
            temp[i] = 0;
            y--;
            printf("\nP[%d]\t\t%d\t\t%d\t\t%d", i + 1, bt[i], sum, sum - bt[i]);
            wt += (sum - bt[i]);
            tat += sum;
        } else if (temp[i] > 0) {
            temp[i] -= q;
            sum += q;
        }
        if (i == count - 1) {
            i = 0;
        } else {
            i++;
        }
    }
    avgwt = (wt * 1.0) / count;
    avgtat = (tat * 1.0) / count;
    printf("\navgwt: %f", avgwt);
    printf("\navgtat: %f", avgtat);

    return 0;
}
