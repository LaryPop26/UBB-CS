cmake_minimum_required(VERSION 3.31)
project(MovieRentalAppQT)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wextra")
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_AUTOUIC ON)

SET(CMAKE_PREFIX_PATH "C:\\Qt\\6.9.0\\mingw_64")

find_package(Qt6 COMPONENTS
        Core
        Gui
        Widgets
        REQUIRED)

add_executable(MovieRentalAppQT main.cpp movie.cpp
        repository.cpp
        service.cpp
        tests.cpp
        validator.cpp
        shoppingCart.cpp
        GUI.cpp
)
target_link_libraries(MovieRentalAppQT
        Qt::Core
        Qt::Gui
        Qt::Widgets
)

