#include <stdio.h>
#include <math.h>

#define PI 3.14159265

int factorial(int n) {
    int fact = 1;
    for (int i = 1; i <= n; i++) {
        fact *= i;
    }
    return fact;
}

double seno(double x, int n) {
    double sum = 0;
    for (int i = 0; i < n; i++) {
        sum += pow(-1, i) * pow(x, 2 * i + 1) / factorial(2 * i + 1);
    }
    return sum;
}

int main() {
    double angulo;
    printf("Ingrese el angulo en grados: ");
    scanf("%lf", &angulo);

    angulo = angulo * PI / 180.0;

    printf("El seno de %.2lf es: %.4lf\n", angulo, seno(angulo, 10));

    return 0;
}