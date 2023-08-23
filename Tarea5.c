#include <stdio.h>

int main(){
    int op;
    float n;
    system("clear");

    printf(" ¿Que desea hacer?\n");
    printf(" 1) Convertir Celsius a Farenheint.\n");
    printf(" 2) Convertir Farenheint a Celsius.\n");
    printf(" 3) Salir.\n");
    scanf("%d", &op);

    do{  
        switch (op){
            case 1:
            printf("Ingrese los valores Celsius a convertir: \n");
            scanf("%f", &n);
            float far = (n*1.8)+32;
            printf("El valor en grados Farenheint es: %f\n", far);
            break;

            case 2:
            printf("Ingrese los valores Farenheint a convertir: \n");
            scanf("%f", &n);
            float cel = (n-32)/1.8;
            printf("El valor en grados Celsius es: %f\n", cel);
            break;

            case 3:
            printf("Salir.\n");
            break;
    
        default:
            printf("Solo te estoy dando 3 opciones, usa esas 3 opciones.\n");
            break;
    }
    } while (op != 3);
    
    return 0;

}