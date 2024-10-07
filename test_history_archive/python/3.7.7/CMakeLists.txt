cmake_minimum_required(VERSION 3.10)
project(Python3.7.7)

include(ExternalProject)

set(PYTHON_VERSION 3.7.7)
set(PYTHON_URL https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tgz)
set(PYTHON_SHA256 "8c8be91cd2648a1a0c251f04ea0bb4c2a5570feb9c45eaaa2241c785585b475a")

ExternalProject_Add(Python
    URL ${PYTHON_URL}
    URL_HASH SHA256=${PYTHON_SHA256}
    CONFIGURE_COMMAND <SOURCE_DIR>/configure 
                      --prefix=${CMAKE_INSTALL_PREFIX}
                      --enable-shared
                      --with-ensurepip=install
    BUILD_COMMAND make
    INSTALL_COMMAND make install
    BUILD_IN_SOURCE 1
    LOG_DOWNLOAD ON
    LOG_CONFIGURE ON
    LOG_BUILD ON
    LOG_INSTALL ON
)

# Custom target for installation
add_custom_target(install_python
    DEPENDS Python
    COMMAND ${CMAKE_COMMAND} -E echo "Installing Python ${PYTHON_VERSION}..."
    COMMAND ${CMAKE_COMMAND} -E env ${CMAKE_COMMAND} --build . --target Python
    COMMAND ${CMAKE_COMMAND} -E echo "Python ${PYTHON_VERSION} installation complete."
)

# Ensure shared libraries are built
set(BUILD_SHARED_LIBS ON CACHE BOOL "Build shared libraries" FORCE)

# Set install rpath
set(CMAKE_INSTALL_RPATH "${CMAKE_INSTALL_PREFIX}/lib")
set(CMAKE_INSTALL_RPATH_USE_LINK_PATH TRUE)