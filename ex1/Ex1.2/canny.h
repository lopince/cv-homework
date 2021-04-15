#pragma once
#include "CImg.h"
#include <string>
#include <vector>
#include <iostream>
#include <time.h>

using namespace std;
using namespace cimg_library;

#define M_PI       acos(-1.0)
#define FOLDER  "/Users/lopince/workspace/c++s/cv-homework/cv1/Ex1.2/test_Data/"

struct Point {
    int x, y;
    Point(int a, int b) {
        x = a;
        y = b;
    }
};

class canny {

private:
    CImg<unsigned char> img; //Original Image
    CImg<unsigned char> grayscaled; // Grayscale
    CImg<unsigned char> gFiltered; // Gradient
    CImg<unsigned char> sFiltered; //Sobel Filtered
    CImg<float> angles; //Angle Map
    CImg<unsigned char> non; // Non-maxima supp.
    CImg<unsigned char> thres; //Double threshold and final

public:
    canny(string); //Constructor
    CImg<unsigned char> toGrayScale();
	vector<vector<double>> createFilter(int, int, double); //Creates a gaussian filter
    CImg<unsigned char> useFilter(CImg<unsigned char>, vector<vector<double>>); //Use some filter
    CImg<unsigned char> sobel(); //Sobel filtering
    CImg<unsigned char> nonMaxSupp(); //Non-maxima supp.
    CImg<unsigned char> threshold(CImg<unsigned char>, int, int); //Double threshold and finalize picture
};

