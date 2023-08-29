#include <stdio.h>

float IVA(float n) {
    return n * 0.12;
}
float SINIVA(float n) {
    return n - (n * 0.12);
}

int main(){
    float n;
    int op;
    system("clear");

    do
    {

        FILE *archivo = fopen("salida.txt", "r");
        if (archivo == NULL){
            printf("No se pudo encontrar el archivo");
            return 1;
        }

        printf(" ¿Quiere evaluar algun producto?\n");
        printf("1) Si\n");
        printf("2) Historial\n");
        printf("3) Borrar Historial\n");
        printf("4) No\n");
        scanf("%d", &op);
        switch (op)
        {
        case 1:
            printf("Ingrese el precio a evaluar en Q.\n");
            scanf("%f", &n);

            float PIVA = IVA(n);

            float SIVA = SINIVA(n);

            FILE *archivo = fopen("salida.txt", "a");
                if (archivo == NULL) {
                    printf("No se pudo abrir el archivo para escribir.\n");
                    return 1; 
                }
                fprintf(archivo, "Precio: %.2f, IVA: %.2f, Precio sin va: %.2f\n",
                        n, PIVA, SIVA);
                fclose(archivo); 

            printf("Su IVA es %.2f y su precio sin IVA %.2f\n", PIVA, SIVA);
            break;
        
        case 2:
            printf("Historial:\n");
                char linea[100]; 
                while (fgets(linea, sizeof(linea), archivo) != NULL) {
                    printf("%s", linea); 
                }
                fclose(archivo);
            break;

        case 3:
            archivo = fopen("salida.txt", "w");
                if (archivo == NULL) {
                    printf("No se pudo abrir el archivo.\n");
                    return 1;
                }
            break;

        case 4:
            printf("Esta bien, Feliz dia.\n");
            break;
        
        default:
            printf("Ingrese una opcion valida\n");
            break;
        }
    } while (op != 4);

    return 0; 
}