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

    void display(CImg<unsigned char>& img);

    void drawCircle(CImg<unsigned char>& img);

    void drawCircleUsingCImg(CImg<unsigned char>& img);

    void drawTriangle(CImg<unsigned char>& img);

    void drawTriangleUsingCImg(CImg<unsigned char>& img);

    void drawLine(CImg<unsigned char>& img);

    void drawLineUsingCImg(CImg<unsigned char>& img);

    void rotate(CImg<unsigned char>& img);

    void rotateUsingCImg(CImg<unsigned char>& img);

    void save(const char *path);

};


#endif //EX1_1_IMGUTILS_H
