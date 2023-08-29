#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Funcion para lanzar un dado
int lanzarDado() {
    return rand() % 6 + 1;
}

int main() {
    srand(time(NULL));

    FILE *archivo = fopen("salida.txt", "r");
    if (archivo == NULL) {
        printf("No se encontro el archivo.");
        return 1;
    }

    int suma, resultado, lanzamientos = 0;
    int op;

    do
    {

        printf("------GRAN 8------\n");
        printf("¿Deseas Lanzar?\n");
        printf("1) Si.\n");
        printf("2) No.\n");
        printf("3) Historial.\n");
        printf("4) Borrar Historial.\n");
        scanf("%d", &op);

        switch (op)
        {
        case 1:
            system("clear");
            do
            {
                int dado1 = lanzarDado();
                int dado2 = lanzarDado();
                suma = dado1 + dado2;
                lanzamientos++;

                FILE *archivo = fopen("salida.txt", "a"); // Abrir archivo en modo "append"
                if (archivo == NULL) {
                    printf("No se encontro el archivo.\n");
                    return 1;
                }
                fprintf(archivo, "Lanzamiento %d: %d + %d = %d\n", lanzamientos, dado1, dado2, suma);
                fclose(archivo);

                printf("Lanzamiento %d: %d + %d = %d\n", lanzamientos, dado1, dado2, suma);

                if (suma == 8) {
                    resultado = 1;
                    printf(">>>>> Ganaste :D <<<<<\n");

                    break;
                } else if (suma == 7) {
                    resultado = -1;
                    printf(">>>>> Perdiste :c <<<<<\n");

                    break;
                }

                if (lanzamientos > 1) {
                    printf("Lanza de nuevo\n");
                    printf("-------------------------\n");
                }
            } while (1);
            break;
        
        case 2:
            printf("Esta bien, vuelve pronto.");
            break;

        case 3:
            system("clear");
            printf("Historial:\n");
            FILE *archivo = fopen("salida.txt", "r");
                    char linea[300]; 
                    while (fgets(linea, sizeof(linea), archivo) != NULL) {
                        printf("%s", linea); 
                    }
                    fclose(archivo);
            break;

        case 4:
            system("clear");
            archivo = fopen("salida.txt", "w");
                    if (archivo == NULL) {
                        printf("No se encontro el archivo.\n");
                        return 1;
                    }
                    fclose(archivo);
                    printf("Historial borrado.\n");
            break;

        default:
            printf("Elije una opcion valida.");
            break;
        }

    } while (op != 2);

    return 0;
}
