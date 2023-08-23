#include <stdio.h>
int main () {
    int op, n;
    system("clear");
    do{
        printf(" ¿Que desea hacer? \n");
        printf(" 1) Sumar. \n");
        printf(" 2) Multiplicar. \n");
        printf(" 3) Salir.\n");
        scanf("%d", &op);

        switch (op){
        case 1:
            printf("\tSuma\n");
            printf("Ingrese la cantidad de valores a sumar: \n");
            scanf("%d", &n);

            int suma = 0;

            for (int i = 0; i < n; ++i) {
                int valor;
                printf("ingrese el valor de %d: ", i + 1);
                scanf("%d", &valor);
                suma += valor;
            }
            printf("La suma de los valores es: %d\n", suma);

            break;
        case 2:
            printf("\tMultipliacion\n");
            printf("Ingrese la cantidad de valores a multiplicar: \n");
            scanf("%d", &n);

            int multiplicacion = 1;

            for (int i = 0; i < n; ++i) {
                int valor;
                printf("ingrese el valor de %d: ", i + 1);
                scanf("%d", &valor);
                multiplicacion *= valor;
            }
            printf("La multipliacion de los valores es: %d\n", multiplicacion);

            break;
        case 3:
            printf("\tSalir\n");
            break;
        default:
            printf("Opcion Invalida\n");
        }
    } while (op != 3);
    
    return 0;
}