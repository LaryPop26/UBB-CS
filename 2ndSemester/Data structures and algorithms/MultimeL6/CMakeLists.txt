cmake_minimum_required(VERSION 3.31)
project(MultimeL6)

set(CMAKE_CXX_STANDARD 20)

add_executable(MultimeL6 App.cpp
        Teste/TestExtins.cpp
        Teste/TestScurt.cpp
        Multime/Multime.cpp
        Multime/IteratorMultime.cpp)
