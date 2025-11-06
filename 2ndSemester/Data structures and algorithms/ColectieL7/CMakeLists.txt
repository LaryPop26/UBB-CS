cmake_minimum_required(VERSION 3.31)
project(ColectieL7)

set(CMAKE_CXX_STANDARD 20)

add_executable(ColectieL7 App.cpp
        "Teste(cu-rel)/TestExtins.cpp"
        "Teste(cu-rel)/TestScurt.cpp"
        "Colectie(cu-rel)/Colectie.cpp"
        "Colectie(cu-rel)/IteratorColectie.cpp")
