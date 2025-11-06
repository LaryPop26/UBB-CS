cmake_minimum_required(VERSION 3.30)
project(MultimeCuRelatieL3)

set(CMAKE_CXX_STANDARD 20)

add_executable(MultimeCuRelatieL3
        "App.cpp"
        "Multime(cu-rel)/IteratorMultime.cpp"
        "Multime(cu-rel)/IteratorMultime.h"
        "Multime(cu-rel)/Multime.cpp"
        "Multime(cu-rel)/Multime.h"
        "Teste(cu relatie)/TestExtins.cpp"
        "Teste(cu relatie)/TestExtins.h"
        "Teste(cu relatie)/TestScurt.cpp"
        "Teste(cu relatie)/TestScurt.h")
