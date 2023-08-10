#include <stdio.h> //Libreria para io
#include <stdlib.h> //Libreria para ejecutar instrucciones del SO
int main() {
    double num1, num2;
    system("clear");
    printf("Ingrese el primer numero:");
    if (scanf("%lf", &num1) !=1) {
        printf("Error: Ingrese un número real válido.\n");
        return 1;
        }

    printf("Ingrese el segundo numero: ");
    if (scanf("%lf", &num2) !=1) {
        printf("Error: Ingrese un número real válido.\n");
        return 1;
        }
    
    double suma = num1 + num2;
    double resta = num1 - num2;
    double multiplicacion = num1 * num2;
    if (num2 == 0) {
        printf("Error: No se puede dividir entre cero.\n");
        return 1;
        }
    double division = num1 / num2;

    printf("\nResultados:\n");
    printf("Suma: %.4lf\n", suma);
    printf("Resta: %.4lf\n", resta);
    printf("Multiplicacion: %.4lf\n", multiplicacion);
    printf("Division: %.4lf\n", division);

    return 0;
}
