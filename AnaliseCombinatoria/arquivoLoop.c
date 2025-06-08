#include <stdio.h>
#include <time.h>

int main() {
    FILE *fp;
    int i;
    clock_t start, end;
    double cpu_time_used;

    start = clock();
    for (i = 0; i < 10000; i++) {
        fp = fopen("arquivo.dat", "r");
        if (fp == NULL) {
            printf("Erro ao abrir o arquivo na iteração %d\n", i);
            return 1;
        }
        // Aqui você pode adicionar operações com o arquivo, se necessário
        fclose(fp);
    }
    end = clock();
    cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;

    printf("Arquivo aberto e fechado 1000 vezes com sucesso.\n");
    printf("Tempo gasto: %.6f segundos\n", cpu_time_used);
    return 0;
}