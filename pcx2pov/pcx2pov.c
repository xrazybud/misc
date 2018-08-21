#include <stdio.h>
#include <stdlib.h>

#include <allegro5/allegro.h>
#include <allegro5/allegro_image.h>

int main(int argc, char *argv[]){
   ALLEGRO_BITMAP *povpic;

   al_init();
   al_init_image_addon();

   povpic = al_load_bitmap("cheshire-cat-icon-16.pcx");
   if (povpic == NULL) {printf("ERROR\n"); return 0;}

   int picx = al_get_bitmap_width(povpic);
   int picy = al_get_bitmap_height(povpic);

   printf("#version 3.7\n\nbackground {color rgb<1,1,1>}\n");
   printf("global_settings { ambient_light rgb<2, 2, 2> }\n");
   printf("light_source { <10, 0, 0> color rgb<1,1,1> }\n");
   printf("camera {orthographic location <10,10,10> look_at <0,0,0> angle 45}\n\n");

   int x, y;
   float startx, starty, endx, endy;

   ALLEGRO_COLOR currentcolor;

   for (x = 0; x < picx; x++) {
      for (y = 0; y < picy; y++) {
         startx = -(picx/2*0.5)+(0.5*x);
         endx = startx + 0.5;

         starty = (picy/2*0.5)-(0.5*y);
         endy = starty + 0.5;

         currentcolor = al_get_pixel(povpic, x, y);

         printf("box { <-0.5,%f,%f>,<0,%f,%f> texture {pigment {color rgb<%f,%f,%f>} } }\n",
                 starty, startx, endy, endx, currentcolor.r, currentcolor.g, currentcolor.b);
      }
   }

   return 0;
}
