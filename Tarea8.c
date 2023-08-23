#include <stdio.h>
#include <string.h>

int main(){
    char n[50], n2[100];
    system("clear");

    printf("Ingrese una palabra.\n");
    scanf("%s", n);

    int longitud = strlen(n);
    int j = 0;

    for (int i = 0; i <= longitud; i++)
    {
        n2[j++]= n[i];
        n2[j++]= n[i];
    }
    n2[j] = '\0';

    printf("Palabra duplicada: %s\n", n2);    

    return 0;

}