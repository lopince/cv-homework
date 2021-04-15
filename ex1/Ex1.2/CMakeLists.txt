cmake_minimum_required(VERSION 3.17)
project(Ex1_2)

set(CMAKE_CXX_STANDARD 14)

include_directories(/opt/x11/include)
link_directories(/opt/X11/lib)

add_executable(Ex1_2 main.cpp canny.cpp canny.h)
target_link_libraries(Ex1_2 -lX11)