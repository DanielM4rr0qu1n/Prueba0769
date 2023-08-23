#include <stdio.h>
#include <string.h>

int main() {
    char mensaje[100];
    int desplazamiento;
    system("clear");
    printf("Introduce el mensaje en mayusculas, sin espacios ni caracteres especiales: ");
    scanf("%s", mensaje);
    printf("Introduce el numero fijo de desplazamiento: ");
    scanf("%d", &desplazamiento);
    for (int i = 0; i < strlen(mensaje); i++) {
        mensaje[i] = ((mensaje[i] - 'A' + desplazamiento) % 26) + 'A';
    }
    printf("El mensaje encriptado es: %s\n", mensaje);
return 0;
}