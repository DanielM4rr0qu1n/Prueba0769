#include <stdio.h>
#include <math.h>

int main () {
    char op;
    system("clear");
    do {

    float VolumenCubo(float lado) {
        return lado * lado * lado;
    }

    float VolumenEsfera(float radio) {
        return 4 / 3 * 3.141592 * pow(radio, 3);
    }

    float VolumenPiramideTriangular(float base, float altura) {
        return 0.333333 * base * altura;
    }

    float VolumenPiramideCuadrada(float base, float altura) {
        return 0.333333 * base * base * altura;
    }
        
        printf("¿En que te puedo ayudar?\n");
        printf("1) Volumen de un Cubo\n");
        printf("2) Volumen de una Esfera\n");
        printf("3) Volumen de una Piramide de base triangular\n");
        printf("4) Volumen de una Piramide de base cuadrada\n");
        printf("Salir\n");
        scanf("%d", &op);
        
        switch (op) {
            case 1:
                {
                    float lado;
                    printf("Ingrese el lado del cubo: ");
                    scanf("%f", &lado);
                    printf("El volumen del cubo es: %.2f\n", VolumenCubo(lado));
                }
                break;
            case 2:
                {
                    float radio;
                    printf("Ingrese el radio de la esfera: ");
                    scanf("%f", &radio);
                    printf("El volumen de la esfera es: %.2f\n", VolumenEsfera(radio));
                }
                break;
            case 3:
                {
                    float base, altura;
                    printf("Ingrese la base de la piramide triangular: ");
                    scanf("%f", &base);
                    printf("Ingrese la altura de la piramide triangular: ");
                    scanf("%f", &altura);
                    printf("El volumen de la piramide de base triangular es: %.2f\n", VolumenPiramideTriangular(base, altura));
                }
                break;
            case 4:
                {
                    float base, altura;
                    printf("Ingrese la base de la piramide cuadrada: ");
                    scanf("%f", &base);
                    printf("Ingrese la altura de la piramide cuadrada: ");
                    scanf("%f", &altura);
                    printf("El volumen de la piramide de base cuadrada es: %.2f\n", VolumenPiramideCuadrada(base, altura));
                }
                break;
            case 5:
                {
                    printf("Salir\n");
                }
            default:
                printf("Opcion invalida.\n");
                break;
            
        }
        } while (op!=5);
    return 0;
}