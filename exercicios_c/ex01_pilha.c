#include <stdio.h>

int mult(int a, int b) {
    return a * b;
}

int soma_mult(int a, int b, int c) {
    return a + mult(b, c);
}

int main(void) {
    int resultado = soma_mult(1, 5, 3);
    printf("%d\n", resultado);   /* Imprime 16 */
    return 0;
}
