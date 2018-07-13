#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#include "pcg_basic.h"

int main(int argc, char *argv[]){
   int blahblah;
   int num1, num2;

   pcg32_random_t rng;

   if (argc < 3) {
      num1 = 100;
      num2 = 1000;
   } else {
      num1 = atoi(argv[1]);
      num2 = atoi(argv[2]);
   }

   pcg32_srandom_r(&rng, time(NULL) ^ (intptr_t)&printf, (intptr_t)&blahblah);

   int randnumber;
   randnumber = (int)pcg32_boundedrand_r(&rng, num2) + num1;

   printf ("%d\n", randnumber % num2+1 );

   return 0;
}
