#include <stdio.h>
#include <stdlib.h>

#include <allegro5/allegro.h>
#include <allegro5/allegro_image.h>

int main(int argc, char *argv[]){
   ALLEGRO_BITMAP *povpic;

   al_init();
   al_init_image_addon();

   povpic = al_load_bitmap("./cheshire-cat-icon-16.pcx");

   if (povpic == NULL) {printf("ERROR\n"); return 0;}

   int picx = al_get_bitmap_width(povpic);
   int picy = al_get_bitmap_height(povpic);

   printf("background {color rgb<1,1,1>}\n\n");
   printf("global_settings { ambient_light rgb<2, 2, 2> }\n");
   printf("light_source { <12, 12, 12> color rgb<1,1,1> }\n");
   printf("camera {\northographic\nlocation <10,10,10>\nlook_at <0,0,0>\nangle 45\n}\n\n");

   int x, y;
   float startx, starty, endx, endy;

   ALLEGRO_COLOR currentcolor;
   unsigned char red, green, blue;
   float colorr, colorg, colorb;

   for (x = 1; x < picx; x++) {
      for (y = 1; y < picy; y++) {
         startx = -4+(0.5*(1*x));
         endx = startx + 0.5;

         starty = -4+(0.5*(1*y));
         endy = starty + 0.5;

         currentcolor = al_get_pixel(povpic, x, y);
         //al_unmap_rgb(currentcolor, &red, &green, &blue);
         //colorr = red/256; colorg = green/256; colorb = blue/256;

         //colorr=0.5; colorg=0.5; colorb=0.5;
         printf("box { <-0.5, %f, %f>, <0, %f, %f> texture {pigment {color rgb<%f,%f,%f>} } }\n", starty, startx, endy, endx, currentcolor.r, currentcolor.g, currentcolor.b);
         //printf("box { <-0.5, %f, %f>, <0, %f, %f> texture {pigment {color rgb<%f,%f,%f>} } }\n", starty, startx, endy, endx, colorr, colorg, colorb);
      }
      printf("\n");
   }

   return 0;
}


// -4+(0.5*(1*x))

// "box { <%f, %f, %f>, <%f, %f, %f> texture {pigment {color rgb<%f,%f,%f>} } }"
