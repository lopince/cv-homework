# include "ImgUtils.h"

int main() {

    ImgUtils imgUtils;

    CImg<unsigned char> img = imgUtils.getDefault();

    // draw img using CImg
    CImg<unsigned char> _img = imgUtils.getDefault();

    // 1. 读入 0.bmp 文件，并用 CImg.display() 显示
    CImg<unsigned char> bmp_0 = imgUtils.load("e:\\workspace\\cv-homework\\cv1\\Ex1.1\\0.bmp");
    imgUtils.display(bmp_0);

    // 2. 在图上绘制一个等边三角形区域，其中心坐标(50,50)，边长为 40，填充颜色为蓝色
    unsigned char blue[] = {0, 0, 255};
    imgUtils.draw_triangle(img, 50, 50, 40, blue);
    imgUtils._draw_triangle(_img, 50, 50, 40, blue);

    // 3. 在图上绘制一个圆形区域，圆心坐标(50,50)，半径为 15，填充颜色为黄色
    unsigned char yellow[] = {255, 255, 0};
    imgUtils.draw_circle(img, 50, 50, 15, yellow);
    imgUtils._draw_circle(_img, 50, 50, 15, yellow);

    // 4. 在图上绘制一条长为 100 的直线段，起点坐标为(0, 0)，方向角为 45 度，直线的颜色为绿色
    unsigned char green[] = {0, 255, 0};
    imgUtils.draw_line(img, 0, 0, 100, 45, green);
    imgUtils.draw_line(_img, 0, 0, 100, 45, green);

    // 5. 用 C++的写图像旋转函数(不调用其他的图像处理库函数), 把第四步的结果图像, 绕坐标(50,50)顺时针旋转 25 和 45 度。
    imgUtils.rotate(img, 45, 50, 50);
//    imgUtils.rotate(img, 45, 50, 50);
    imgUtils._rotate(_img, 25, 50, 50);
//    imgUtils._rotate(_img, 45, 50, 50);

    // 6. 把上面的操作结果保存为 2.bmp
    imgUtils.save(img, "e:\\workspace\\cv-homework\\cv1\\Ex1.1\\2.bmp");

    imgUtils.display(img);
    imgUtils.display(_img);

    return 0;
}


