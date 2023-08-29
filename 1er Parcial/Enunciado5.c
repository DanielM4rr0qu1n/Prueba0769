#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_STUDENTS 100
#define MAX_SUBJECT_LENGTH 50

struct Student {
    char name[50];
    char subject[MAX_SUBJECT_LENGTH];
    float grade;
};

struct Student students[MAX_STUDENTS];
int numStudents = 0;

void saveToFile() {
    FILE *file = fopen("salida.txt", "w");
    if (file == NULL) {
        printf("No se pudo abrir el archivo de salida.\n");
        return;
    }

    for (int i = 0; i < numStudents; i++) {
        fprintf(file, "Nombre: %s\n", students[i].name);
        fprintf(file, "Materia: %s\n", students[i].subject);
        fprintf(file, "Nota: %.2f\n\n", students[i].grade);
    }

    fclose(file);
    printf("Datos guardados en salida.txt\n");
}

void showHistory() {
    if (numStudents == 0) {
        printf("No hay registros en el historial.\n");
        return;
    }

    for (int i = 0; i < numStudents; i++) {
        printf("Nombre: %s\n", students[i].name);
        printf("Materia: %s\n", students[i].subject);
        printf("Nota: %.2f\n\n", students[i].grade);
    }
}

void clearHistory() {
    numStudents = 0;
    printf("Historial de notas borrado.\n");
}

int main() {
    system("clear");
    int choice;

    do {
        printf("Menu:\n");
        printf("1. Registrar nuevo estudiante y sus notas\n");
        printf("2. Ver el historial de notas\n");
        printf("3. Borrar historial de notas\n");
        printf("4. Salir\n");
        printf("Ingrese su eleccion: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1: {
                system("clear");
                if (numStudents < MAX_STUDENTS) {
                    printf("Ingrese el nombre del estudiante: ");
                    scanf("%s", students[numStudents].name);
                    printf("Ingrese el nombre de la materia: ");
                    scanf("%s", students[numStudents].subject);
                    printf("Ingrese la nota: ");
                    scanf("%f", &students[numStudents].grade);
                    numStudents++;
                    printf("Registro guardado.\n");
                } else {
                    printf("Se ha alcanzado el máximo de estudiantes.\n");
                }
                break;
            }
            case 2: {
                system("clear");
                showHistory();
                break;
            }
            case 3: {
                system("clear");
                clearHistory();
                break;
            }
            case 4: {
                saveToFile();
                printf("Saliendo del programa.\n");
                break;
            }
            default:
                printf("Opcion no valida. Por favor, elija una opción valida.\n");
        }
    } while (choice != 4);

    return 0;
}
