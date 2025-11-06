cmake_minimum_required(VERSION 4.0)
project(InClass3)

set(CMAKE_CXX_STANDARD 20)

add_executable(InClass3 hello.cpp
        suma.cpp
        suma2.cpp)

find_package(MPI REQUIRED)

target_link_libraries(InClass3 PUBLIC MPI::MPI_CXX)