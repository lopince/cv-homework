#include "ImgUtils.h"

CImg<unsigned char> load(const char *path){
    CImg<unsigned char> img;
    img.load(path);

    return img;
}

void display(CImg<unsigned char>& img){
    img.display();
}

void drawCircle(CImg<unsigned char>& img, int cenX, int cenY, int r, unsigned char color[]){

    cimg_forXY(img, x, y) {
        if(abs(cenX - x) <= r && abs(cenY - y) <= r) {

            img(x, y , 0) = color[0];
            img(x, y , 1) = color[1];
            img(x, y , 2) = color[2];
        }
    }
}

void drawCircleUsingCImg(CImg<unsigned char>& img, int cenX, int cenY, int r, unsigned char color[]){
    img.draw_circle(cenX, cenY, r, color);
}
