cmake_minimum_required(VERSION 3.30)
project(lab2_4 C)

set(CMAKE_C_STANDARD 23)

add_executable(lab2_4 main.c
        controller.h
        controller.c
        entity.h
        entity.c
        MyList.c
        MyList.h
        ui.c
        ui.h
        tests.c
        tests.h
        validation.c
        validation.h)
