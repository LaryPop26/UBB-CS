cmake_minimum_required(VERSION 3.30)
project(lab2_4 C)

set(CMAKE_C_STANDARD 23)
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -Wall -Wextra")

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
