#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#include "pcg_basic.h"

int main(int argc, char *argv[]){
   int blahblah = 5;

   pcg32_random_t rng;

   pcg32_srandom_r(&rng, time(NULL) ^ (intptr_t)&printf, (intptr_t)&blahblah); 

   int randnumber;
   int lower = 100;
   int upper = 1000;
   randnumber = (int)pcg32_boundedrand_r(&rng, upper) + lower;

   printf ("%d\n", randnumber );

return 0;
}


