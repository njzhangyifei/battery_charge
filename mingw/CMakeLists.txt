cmake_minimum_required(VERSION 3.9)
project(battery_charge)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_FLAGS ${CMAKE_CXX_FLAGS} -O3)

add_executable(battery_charge main.cpp)