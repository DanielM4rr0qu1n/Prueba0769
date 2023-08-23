#include <stdio.h>

int main (){
    int n;
    system("clear");
    printf("Ingrese el numero del cual quiera la tabla.\n");
    scanf("%d", &n);

    printf("La tabla de multiplicar de %d es: \n", n);
    for (int i = 1; i <= 12; i++)
    {
        printf("%d * %d = %d\n", n, i, n*i);
    }
    
    return 0;

}