cmake_minimum_required(VERSION 3.30)
project(MovieRentalApp)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wextra")

find_program(CLANG_TIDY_EXE NAMES clang-tidy)
if(CLANG_TIDY_EXE)
    message(STATUS "Using clang-tidy: ${CLANG_TIDY_EXE}")

    set(CMAKE_CXX_CLANG_TIDY "${CLANG_TIDY_EXE}")
endif()

add_executable(MovieRentalApp
        main.cpp
        movie.cpp
        movie.h
        repository.cpp
        repository.h
        service.cpp
        service.h
        UI.cpp
        UI.h
        validator.cpp
        validator.h
        tests.cpp
        tests.h
        shoppingCart.cpp
        shoppingCart.h
        observer.h
        undo.h
)
