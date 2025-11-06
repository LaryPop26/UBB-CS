cmake_minimum_required(VERSION 3.31)
project(DictionarL4)

set(CMAKE_CXX_STANDARD 20)

add_executable(DictionarL4 App.cpp
        Teste/TestScurt.cpp
        Teste/TestExtins.cpp
        Dictionar/IteratorDictionar.cpp
        Dictionar/Dictionar.cpp)
