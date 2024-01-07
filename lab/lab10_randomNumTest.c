#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double* mixedCongruential(int n) {
    int x0, a, c, m;
    printf("Enter Seed Multiplier x0: ");
    scanf("%d", &x0);
    printf("Enter Constant Multiplier a: ");
    scanf("%d", &a);
    printf("Enter increment c: ");
    scanf("%d", &c);
    printf("Enter modulus m: ");
    scanf("%d", &m);
    double* Arr = (double*)malloc(n * sizeof(double));
    for (int i = 0; i < n; i++) {
        x0 = (a * x0 + c) % m;
        Arr[i] = (double)x0/m;
    }
    return Arr;
}

void KS_sampleOver50(double D, int N) {
    if (D < 1.36 / sqrt(N)) {
        printf("The random Numbers are uniformly distributed.\n");
    } else {
        printf("The random Numbers are not uniformly distributed.\n");
    }
}

void calculate_Kolmogorov_Smirnov(double* Ri, int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (Ri[j] > Ri[j + 1]) {
                double temp = Ri[j];
                Ri[j] = Ri[j + 1];
                Ri[j + 1] = temp;
            }
        }
    }
    double* Dplus = (double*)malloc(n * sizeof(double));
    double* Dminus = (double*)malloc(n * sizeof(double));
    for (int i = 0; i < n; i++) {
        Dplus[i] = (i + 1) / (double)n - Ri[i];
        Dminus[i] = Ri[i] - i / (double)n;
    }
    double DP = Dplus[0];
    double DM = Dminus[0];
    for (int i = 1; i < n; i++) {
        if (Dplus[i] > DP) {
            DP = Dplus[i];
        }
        if (Dminus[i] > DM) {
            DM = Dminus[i];
        }
    }
    double D = DP > DM ? DP : DM;
    if (n > 50) {
        KS_sampleOver50(D, n);
    } else {
        printf("Calculated value of D is %lf\n", D);
        printf("If %lf is less than critical value D from table we accept that it is Uniform. Otherwise it is not uniform. For sample greater than 50 tabulated D value is 1.36/sqrt(N)\n", D);
    }
    free(Dplus);
    free(Dminus);
}

void autoCorrelation(int i, int m, double* R, int n) {
    int M = (n - m - i) / m;
    double sumation = 0;
    for (int k = 0; k <= M; k++) {
        sumation += R[(i + k * m) - 1] * R[(i + (k + 1) * m) - 1];
    }
    double rho = (1 / (double)(M + 1)) * sumation - 0.25;
    double sigma = sqrt((13 * M + 7)) / (12 * (M + 1));
    double z = rho / sigma;
    if (z < 1.96) {
        printf("z calculated %lf < z tabulated 1.96. So, The numbers are independent.\n", z);
    } else {
        printf("The numbers are not independent\n");
    }
}

int main() {
    int quantity = 56;
    double* randomNum = mixedCongruential(quantity);
    printf("The Random Numbers are: \n");
    for (int i = 0; i < quantity; i++) {
        printf("%f ", randomNum[i]);
    }
    printf("\n");
    printf("Kolmogorov Smirov Test for uniformity: \n");
    calculate_Kolmogorov_Smirnov(randomNum, quantity);
    printf("Auto Correlation Test for independence: \n");
    autoCorrelation(2, 5, randomNum, quantity);
    free(randomNum);
    return 0;
}