#include <stdio.h>

// Função para calcular o coeficiente binomial (n choose k)
int binomial(int n, int k) {
    int res = 1;
    if (k > n - k)
        k = n - k;
    for (int i = 0; i < k; ++i) {
        res *= (n - i);
        res /= (i + 1);
    }
    return res;
}

int main() {
    int n = 4;
    printf("Desenvolvimento de (x + a)^4:\n");
    for (int k = 0; k <= n; ++k) {
        int coef = binomial(n, k);
        int exp_x = n - k;
        int exp_a = k;

        printf("%s", (k == 0) ? "" : " + ");
        if (coef > 1)
            printf("%d*", coef);
        if (exp_x > 0)
            printf("x");
        if (exp_x > 1)
            printf("^%d", exp_x);
        if (exp_x > 0 && exp_a > 0)
            printf("*");
        if (exp_a > 0)
            printf("a");
        if (exp_a > 1)
            printf("^%d", exp_a);
    }
    printf("\n");
    return 0;
}