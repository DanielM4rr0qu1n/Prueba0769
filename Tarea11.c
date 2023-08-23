#include <stdio.h>
#include <string.h>

    void filtro(char *pos){
        int Longitud = strlen(pos);
        int Letras[256] = {0};
        int filtrado = 0;

        for (int i = 0; i < Longitud; i++)
        {
            if (Letras[(int)pos[i] == 0])
            {
                Letras[(int)pos[i]] = 1;
                pos[filtrado++] = pos[i];
            }
            
        }
        pos[filtrado] = '\0';
    }
    
    int main (){
        char pos[100];
        
        printf("Ingrese la serie valores.\n");
        fgets(pos, sizeof(pos), stdin);

         if (pos[strlen(pos) - 1] == '\n') {
        pos[strlen(pos) - 1] = '\0';
        }        

        filtro(pos);

        printf("Su serie de valores sin datos repetidos es %s\n", pos);

    return 0;
    }
