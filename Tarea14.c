#include <stdio.h>

int main() {
    int numFilas;
    
    printf("Ingrese el numero de filas: ");
    scanf("%d", &numFilas);
    
    for (int i = 1; i <= numFilas; i++) {
        for (int j = 1; j <= i; j++) {
            printf("*");
        }
        printf("\n");
    }
    
return 0;
}