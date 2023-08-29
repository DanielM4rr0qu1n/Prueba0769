#include <stdio.h>
#include <stdlib.h>
#include <math.h>


float calcularMedia(int calificaciones[], int n) {
    int suma = 0;
    for (int i = 0; i < n; i++) {
        suma += calificaciones[i];
    }
    return (float)suma / n;
} //Media

float calcularMediana(int calificaciones[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (calificaciones[j] > calificaciones[j + 1]) {
                int temp = calificaciones[j];
                calificaciones[j] = calificaciones[j + 1];
                calificaciones[j + 1] = temp;
            }
        }
    }

    if (n % 2 == 0) {
        return (float)(calificaciones[n / 2 - 1] + calificaciones[n / 2]) / 2;
    } else {
        return calificaciones[n / 2];
    }
} //Mediana

int calcularRango(int calificaciones[], int n) {
    int max = calificaciones[0];
    int min = calificaciones[0];

    for (int i = 1; i < n; i++) {
        if (calificaciones[i] > max) {
            max = calificaciones[i];
        }
        if (calificaciones[i] < min) {
            min = calificaciones[i];
        }
    }

    return max - min;
} //Rango

int main() {
    int n = 5;
    int calificaciones[n];
    system("clear");

    for (int i = 0; i < n; i++) {
        printf("Ingrese la calificacion %d: ", i + 1);
        scanf("%d", &calificaciones[i]);
    }// Agregamos las calificaciones

    float media = calcularMedia(calificaciones, n);
    float mediana = calcularMediana(calificaciones, n);
    int rango = calcularRango(calificaciones, n);

    printf("Media: %.2f\n", media);
    printf("Mediana: %.2f\n", mediana);
    printf("Rango: %d\n", rango); //Resultados

    FILE *archivo = fopen("salida.txt", "a");
    if (archivo == NULL) {
        printf("Error al abrir el archivo.\n");
        return 1;
    }//Almacenamos los datos
    
    fprintf(archivo, "--------------------------------\n");
    fprintf(archivo, "1. Media: %.2f\n", media);
    fprintf(archivo, "2. Mediana: %.2f\n", mediana);
    fprintf(archivo, "3. Rango: %d\n", rango);

    fclose(archivo);
    int op;
do {
    printf("Opciones del Historial.\n");
    printf("1) Ver Historial.\n");
    printf("2) Borrar Historial.\n");
    printf("3) Salir.\n");
    scanf("%d", &op);
    switch (op)
    {
    case 1:
        system("clear");
        archivo = fopen("salida.txt", "r");
        if (archivo == NULL) {
                    printf("No se pudo abrir el archivo para escribir.\n");
                    return 1; 
                }
        printf("Historial:\n");
                char linea[100]; 
                while (fgets(linea, sizeof(linea), archivo) != NULL) {
                    printf("%s", linea); 
                }
                fclose(archivo);
        break;

    case 2:
        system("clear");
        archivo = fopen("salida.txt", "w");
                if (archivo == NULL) {
                    printf("No se pudo abrir el archivo para escribir.\n");
                    return 1; 
                }
                fclose(archivo); 
                printf("Historial borrado.\n");
        break;
    
    case 3:
        printf("Saliendo...");
        break;
    
    default:
        printf("Elija una opcion valida.\n");
        break;
    } 
    } while (op != 3);
    

    return 0;
}