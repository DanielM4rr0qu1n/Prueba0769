#include <stdio.h>

int main(){
    int n;
    system("clear");
    printf("Ingrese el numero a evaluar\n");
    scanf("%d", &n);

    if (n % 2 == 0)
    {
        printf("Su numero es par.\n");
    } else (printf("Su numero es impar.\n"));
    
    return 0;

}