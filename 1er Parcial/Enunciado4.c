#include <stdio.h>
#include <stdbool.h>

bool Prime(int num) {
    if (num <= 1) {
        return false;
    }
    for (int i = 2; i * i <= num; i++) {
        if (num % i == 0) {
            return false;
        }
    }
    return true;
}

int main() {
    system("clear");

    FILE *archivo = fopen("salida.txt", "r"); 
            if (archivo == NULL) {
                printf("No se encontro el archivo.\n");
                return 1;
            }

     int num, op;

    do
    {
        printf("----------------------------------\n");
        printf("Holi, ¿Que deseas hacer?\n");
        printf("1) Evaluar.\n");
        printf("2) Ver el Historial.\n");
        printf("3) Borrar Historial.\n");
        printf("4) Salir.\n");
        scanf("%d", &op);

        switch (op)
        {
        case 1:
            system("clear");
            printf("Ingrese un numero: ");
            scanf("%d", &num);

            bool primo = Prime(num);

            FILE *archivo = fopen("salida.txt", "a"); 
            if (archivo == NULL) {
                printf("No se encontro el archivo.\n");
                return 1;
            }

            if (primo) {
                printf("%d es un numero primo.\n", num);
                fprintf(archivo, "%d es un número primo.\n", num);
            } else {
                printf("%d es un numero compuesto.\n", num);
                fprintf(archivo, "%d es un número compuesto.\n", num);
            }

            fclose(archivo);
            
            break;
        
        case 2:
            system("clear");
            printf("Historial:\n");
                char linea[100]; 
                while (fgets(linea, sizeof(linea), archivo) != NULL) {
                    printf("%s", linea); 
                }
                fclose(archivo);
            break;

        case 3:
            system("clear");
            archivo = fopen("salida.txt", "w");
                if (archivo == NULL) {
                    printf("No se pudo abrir el archivo.\n");
                    return 1;
                }
                fclose(archivo);
                    printf("Historial borrado.\n");
            break;

        case 4:
            printf("Adios.");
            break;
        
        default:

            printf("Ingresa una opcion valida.");

            break;
        }
        
    } while (op != 4);
    

    return 0;
}
