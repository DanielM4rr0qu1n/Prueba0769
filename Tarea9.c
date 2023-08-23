#include <stdio.h>

int main() {
    int n;
    system("clear");

    printf("Ingrese un valor: \n");
    scanf("%d", &n);
    
    int fib[n];
    fib[0] = 0;
    fib[1] = 1;
    
    for (int i = 2; i <= n; i++) {
        fib[i] = fib[i - 1] + fib[i - 2];
        }
    
    printf("Los primeros %d terminos de la serie de Fibonacci son:\n", n);
    for (int i = 0; i < n; i++) {
        printf("%d ", fib[i]);
        }
    
    return 0;
}