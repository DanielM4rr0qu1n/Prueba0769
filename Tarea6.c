#include <stdio.h>

int main(){
    int n, p;
    system("clear");
    
    printf("Ingrese el valor inicial.\n");
    scanf("%d", &n);

    printf("Ingrese el valor final.\n");
    scanf("%d", &p);

    for (int i = n; i <= p; i++)
    {
       if (i % 2 == 0)
       {
        printf("Los valores pares dentro de ese rango son: %d, \n", i);
       }
    }
    
return 0;

}