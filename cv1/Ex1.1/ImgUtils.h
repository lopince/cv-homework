#ifndef EX1_1_IMGUTILS_H
#define EX1_1_IMGUTILS_H

# include "iostream"
# include "cmath"
# include "CImg.h"

using namespace std;
using namespace cimg_library;
const double pi(3.1415926);

class ImgUtils {

public:

    ImgUtils();

    ~ImgUtils();

    CImg<unsigned char> load(const char *path);

    CImg<unsigned char> getDefault(){

        CImg<unsigned char> img(400, 400, 1, 3);
        return img;
    }

    void display(CImg<unsigned char>& img);

    void draw_triangle(CImg<unsigned char> &img,
                       int cenX,
                       int cenY,
                       int len,
                       unsigned char color[]);

    void _draw_triangle(CImg<unsigned char> &img,
                       int cenX,
                       int cenY,
                       int len,
                       unsigned char color[]);

    void draw_circle(CImg<unsigned char>& img,
                    int cenX,
                    int cenY,
                    int r,
                    unsigned char color[]);

    void _draw_circle(CImg<unsigned char>& img, int cenX, int cenY, int r, unsigned char color[]);


    void draw_line(CImg<unsigned char>& img,
                   int x0,
                   int y0,
                   int len,
                   int degree,
                   unsigned char color[]);

    void _draw_line(CImg<unsigned char>& img,
                    int x0,
                    int y0,
                    int len,
                    int degree,
                    unsigned char color[]);




    void rotate(CImg<unsigned char>& img,
                int degree,
                int x0,
                int y0);

    void _rotate(CImg<unsigned char>& img,
                int degree,
                int x0,
                int y0);

    void save(const char *path);

};


#endif //EX1_1_IMGUTILS_H
