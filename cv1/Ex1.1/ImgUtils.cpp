#include "ImgUtils.h"

ImgUtils::ImgUtils() {}

ImgUtils::~ImgUtils() {}

CImg<unsigned char> ImgUtils::load(const char *path) {
    CImg<unsigned char> img;
    img.load(path);

    return img;
}

void ImgUtils::display(CImg<unsigned char> &img) {
    img.display();
}


void ImgUtils::draw_triangle(CImg<unsigned char> &img,
                             int cenX,
                             int cenY,
                             int len,
                             unsigned char color[]) {

    double a = len / 2 / cos(pi / 6);
    double b = len / 2 * tan(pi / 6);
    double Ax = cenX;
    double Ay = cenY - a;
    double Bx = cenX - len / 2;
    double By = cenY + b;
    double Cx = cenX + len / 2;
    double Cy = cenY + b;

    double k01 = (Ay - By) / (Ax - Bx);
    double k02 = (Ay - Cy) / (Ax - Cx);
    cimg_forXY(img, x, y) {
            // range of the triangle pixels
            if (Bx <= x && x < Cx && Ay <= y && y <= By) {
                double kx1 = (y - By) / (x - Bx);
                double kx2 = (y - Cy) / (x - Cx);
                // fill color
                if (kx1 >= k01 && kx2 <= k02) {
                    img(x, y, 0) = color[0];
                    img(x, y, 1) = color[1];
                    img(x, y, 2) = color[2];
                }
            }
        }
}

void ImgUtils::_draw_triangle(CImg<unsigned char> &img,
                              int cenX,
                              int cenY,
                              int len,
                              unsigned char *color) {

    double a = len / 2 / cos(pi / 6);
    double b = len / 2 * tan(pi / 6);
    double Ax = cenX;
    double Ay = cenY - a;
    double Bx = cenX - len / 2;
    double By = cenY + b;
    double Cx = cenX + len / 2;
    double Cy = cenY + b;

    img.draw_triangle(Ax, Ay, Bx, By, Cx, Cy, color);
}

void ImgUtils::draw_circle(CImg<unsigned char> &img,
                           int cenX,
                           int cenY,
                           int r,
                           unsigned char color[]) {

    cimg_forXY(img, x, y) {
            if (pow((cenX - x), 2) + pow((cenY - y), 2) <= pow(r, 2)) {
                img(x, y, 0) = color[0];
                img(x, y, 1) = color[1];
                img(x, y, 2) = color[2];
            }
        }
}

void ImgUtils::_draw_circle(CImg<unsigned char> &img,
                            int cenX,
                            int cenY,
                            int r,
                            unsigned char color[]) {
    img.draw_circle(cenX, cenY, r, color);
}

void ImgUtils::draw_line(CImg<unsigned char> &img,
                         int x0,
                         int y0,
                         int len,
                         int degree,
                         unsigned char color[]) {

    double anglePi = degree * pi / 180;

    double xEnd = len * cos(anglePi);
    double yEnd = len * cos(anglePi);
    cimg_forXY(img, x, y) {
            if (x0 <= x && x <= xEnd
                && y0 <= y && y <= yEnd
                && abs((double) x * tan(anglePi) - (double) y) <= 0.5) {
                img(x, y, 0) = color[0];
                img(x, y, 1) = color[1];
                img(x, y, 2) = color[2];
            }
        }
}

void ImgUtils::_draw_line(CImg<unsigned char> &img,
                          int x0,
                          int y0,
                          int len,
                          int degree,
                          unsigned char color[]) {
    img.draw_line(x0,  y0, len, degree, color);
}

double interpolation(int valueA,
                     int valueB,
                     int valueC,
                     int valueD,
                     double p,
                     double q) {
    return (1 - q) * (1 - p) * valueA + (1 - q) * p * valueD + q * (1 - p) * valueB + p * q * valueC;
}

void ImgUtils::rotate(CImg<unsigned char> &img,
                      int degree,
                      int x0,
                      int y0) {

    double anglePi = degree * pi / 180;
    double sinA = sin(anglePi);
    double cosA = cos(anglePi);

    double w0 = img.width();
    double h0 = img.height();


    double w = w0 * cosA + h0 * sinA;
    double h = h0;
    if (w0 == h0) {
        h = w;
    } else {
        h = h0 * cosA + w0 * sinA;
    }


    CImg<unsigned char> newImg(w, h, 1, 3, 0);

    cimg_forXY(newImg, x, y) {

            double x0 = (x - w / 2) * cosA + (y - h / 2) * sinA + w0 / 2;
            double y0 = (y - h / 2) * cosA - (x - w / 2) * sinA + h0 / 2;

            if (x0 > 0 && x0 < w0 && y0 > 0 && y0 < h0) {

                int aX = (int) x0;
                int aY = (int) y0;
                int bX = aX + 1;
                int bY = aY;
                int cX = (int) x0;
                int cY = aY + 1;
                int dX = aX + 1;
                int dY = aY + 1;

                // distance to point A
                double p = x0 - aX;
                double q = y0 - aY;

                // interpolation
                newImg(x, y, 0) = interpolation(img(aX, aY, 0), img(bX, bY, 0), img(cX, cY, 0), img(dX, dY, 0), p, q);
                newImg(x, y, 1) = interpolation(img(aX, aY, 1), img(bX, bY, 1), img(cX, cY, 1), img(dX, dY, 1), p, q);
                newImg(x, y, 2) = interpolation(img(aX, aY, 2), img(bX, bY, 2), img(cX, cY, 2), img(dX, dY, 2), p, q);
            }
        }
    img = newImg;
}

void ImgUtils::_rotate(CImg<unsigned char> &img,
                      int degree,
                      int x0,
                      int y0) {
    img.rotate(degree, x0, y0);
}
