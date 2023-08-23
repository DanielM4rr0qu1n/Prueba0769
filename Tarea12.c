#include <stdio.h>

int main() {
    double mpg, kpl;
    printf("Introduce la cantidad de millas por galon imperial: ");
    scanf("%lf", &mpg);
    kpl = (mpg * 1.609344) / 4.54609188;
    printf("La cantidad de kilometros por litro es: %.2lf\n", kpl);
    return 0;
}