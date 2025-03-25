cmake_minimum_required(VERSION 3.30)
project(lab2_4 C)

set(CMAKE_C_STANDARD 23)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} --coverage")
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} --coverage -Wall -Wextra")

add_executable(lab2_4 ui.c
        controller.h
        controller.c
        entity.h
        entity.c
        MyList.c
        MyList.h
        tests.c
        tests.h
        validation.c
        validation.h
        mysort.c
        mysort.h)
