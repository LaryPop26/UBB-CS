cmake_minimum_required(VERSION 3.30)
project(VectorDinamicL1)

set(CMAKE_CXX_STANDARD 23)

add_executable(VectorDinamicL1 App.cpp
                TestScurt.cpp
                TestScurt.h
                TestExtins.cpp
                TestExtins.h
                IteratorVectorDinamic.cpp
                IteratorVectorDinamic.h
                VectorDinamic.cpp
                VectorDinamic.h)
