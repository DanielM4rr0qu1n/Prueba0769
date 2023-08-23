#include <stdio.h>
#include <string.h>

int main(){
    char n[100];
    system("clear");

    printf("Ingrese su palabra.\n");
    fgets(n, sizeof(n), stdin);
    n[strcspn(n, "\n")] = '\0';

    int longitud = strlen(n);
    printf("La longitud es: %d", longitud);
    
    return 0;

}