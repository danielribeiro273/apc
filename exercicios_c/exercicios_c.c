#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stddef.h>

// --- EXERCÍCIO 1: Pilha de Chamadas ---
int mult(int a, int b) { return a * b; }
int soma_mult(int a, int b, int c) { return a + mult(b, c); }
void ex01(void) {
    printf("--- Ex 01 ---\n");
    printf("Resultado: %d\n", soma_mult(1, 5, 3));
}

// --- EXERCÍCIO 2: Tamanhos e Promoção ---
void ex02(void) {
    printf("\n--- Ex 02 ---\n");
    printf("int: %zu bytes | float: %zu bytes\n", sizeof(int), sizeof(float));
    printf("7 / 2 = %d | 7.0 / 2 = %.1f\n", 7 / 2, 7.0 / 2);
}

// --- EXERCÍCIO 3: Variáveis ---
void ex03(void) {
    printf("\n--- Ex 03 ---\n");
    int a = 42, b = a + 8;
    printf("a = %d, b = %d\n", a, b);
}

// --- EXERCÍCIO 4: Operadores e Bits ---
void ex04(void) {
    printf("\n--- Ex 04 ---\n");
    int a = 17, b = 5;
    printf("17 %% 5 = %d\n", a % b);
    unsigned char flags = 0;
    flags |= (1 << 2);
    printf("flags bit 2 ativo: %u\n", flags);
}

// --- EXERCÍCIO 5: Controle de Fluxo ---
void ex05(void) {
    printf("\n--- Ex 05 ---\n");
    int nota = 72;
    if (nota >= 70) printf("Nota C (Aprovado)\n");
}

// --- EXERCÍCIO 6: Funções e Recursão ---
int fatorial(int n) { return (n <= 1) ? 1 : n * fatorial(n - 1); }
void ex06(void) {
    printf("\n--- Ex 06 ---\n");
    printf("5! = %d\n", fatorial(5));
}

// --- EXERCÍCIO 7: Arrays e Matrizes ---
void ex07(void) {
    printf("\n--- Ex 07 ---\n");
    int v[5] = {10, 20, 30, 40, 50};
    printf("v[0] = %d\n", v[0]);
}

// --- EXERCÍCIO 8: Strings ---
void ex08(void) {
    printf("\n--- Ex 08 ---\n");
    char s[] = "Brasilia";
    printf("Comprimento de '%s': %zu\n", s, strlen(s));
}

// --- EXERCÍCIO 9: Ponteiros ---
void ex09(void) {
    printf("\n--- Ex 09 ---\n");
    int x = 10;
    int *p = &x;
    *p = 99;
    printf("x via ponteiro: %d\n", x);
}

// --- EXERCÍCIO 10: Alocação Dinâmica ---
void ex10(void) {
    printf("\n--- Ex 10 ---\n");
    int *v = calloc(4, sizeof(int));
    if (v) {
        v[0] = 100;
        printf("v[0] no Heap: %d\n", v[0]);
        free(v);
    }
}

// --- EXERCÍCIO 11: Structs ---
typedef struct { char nome[30]; int x, y; } Ponto;
void ex11(void) {
    printf("\n--- Ex 11 ---\n");
    Ponto p = {"Origem", 0, 0};
    printf("Struct: %s (%d,%d)\n", p.nome, p.x, p.y);
}

// --- EXERCÍCIO 12: Enums ---
typedef enum { DOM, SEG, TER, QUA, QUI, SEX, SAB } Dia;
void ex12(void) {
    printf("\n--- Ex 12 ---\n");
    Dia hoje = QUA;
    printf("Dia Enum: %d\n", hoje);
}

// --- EXERCÍCIO 13: E/S e Formatação ---
void ex13(void) {
    printf("\n--- Ex 13 ---\n");
    printf("Hexadecimal 255: %x\n", 255);
}

// --- EXERCÍCIO 14: Macros ---
#define QUADRADO(x) ((x)*(x))
void ex14(void) {
    printf("\n--- Ex 14 ---\n");
    printf("Quadrado de 5: %d\n", QUADRADO(5));
}

// --- EXERCÍCIO 15: Escopo Static ---
void contador(void) {
    static int n = 0;
    n++;
    printf("Contador static: %d\n", n);
}
void ex15(void) {
    printf("\n--- Ex 15 ---\n");
    contador(); contador();
}

// --- EXERCÍCIO 16: Buffer Seguro ---
void ex16(void) {
    printf("\n--- Ex 16 ---\n");
    char dest[8];
    strncpy(dest, "UnB-2026", sizeof(dest) - 1);
    dest[sizeof(dest) - 1] = '\0';
    printf("String segura: %s\n", dest);
}

// --- EXERCÍCIO 17: Callbacks e qsort ---
int cmp_asc(const void *a, const void *b) {
    return *(int*)a - *(int*)b;
}
void ex17(void) {
    printf("\n--- Ex 17 ---\n");
    int v[] = {40, 10, 30, 50, 20};
    qsort(v, 5, sizeof(int), cmp_asc);
    printf("Array ordenado: %d %d %d %d %d\n", v[0], v[1], v[2], v[3], v[4]);
}

// --- EXERCÍCIO 18: Lista Ligada ---
typedef struct No {
    int valor;
    struct No *proximo;
} No;
void ex18(void) {
    printf("\n--- Ex 18 ---\n");
    No n2 = {20, NULL};
    No n1 = {10, &n2};
    printf("Lista encadeada: %d -> %d -> NULL\n", n1.valor, n1.proximo->valor);
}

// --- FUNÇÃO MAIN ÚNICA QUE EXECUTA TUDO OS 18 ---
int main(void) {
    printf("=== EXERCÍCIOS DE LINGUAGEM C (1 a 18) ===\n");
    ex01(); ex02(); ex03(); ex04(); ex05();
    ex06(); ex07(); ex08(); ex09(); ex10();
    ex11(); ex12(); ex13(); ex14(); ex15(); 
    ex16(); ex17(); ex18();
    return 0;
}
