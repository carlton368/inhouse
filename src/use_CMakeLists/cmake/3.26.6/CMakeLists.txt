CMAKE_MINIMUM_REQUIRED(VERSION 2.8.12)
include(RezBuild)

# CMake 버전 정보 설정
set(cmake_version "3.26.6")
set(cmake_short_version "3.26")
set(url_cmake https://cmake.org/files/v${cmake_short_version}/cmake-${cmake_version}-linux-x86_64.tar.gz)

# 다운로드 디렉토리 설정
set(download_dir ${CMAKE_CURRENT_BINARY_DIR}/downloads)
file(MAKE_DIRECTORY ${download_dir})

# curl을 사용하여 수동으로 다운로드
execute_process(
    COMMAND curl -L ${url_cmake} -o ${download_dir}/cmake-${cmake_version}-linux-x86_64.tar.gz
    RESULT_VARIABLE download_result
)

if(NOT ${download_result} EQUAL 0)
    message(FATAL_ERROR "Failed to download CMake binary. Please check your internet connection and try again.")
endif()

# 압축 해제
file(MAKE_DIRECTORY ${CMAKE_INSTALL_PREFIX})
execute_process(
    COMMAND tar -xzf ${download_dir}/cmake-${cmake_version}-linux-x86_64.tar.gz --strip-components=1 -C ${CMAKE_INSTALL_PREFIX}
    RESULT_VARIABLE extract_result
)

if(NOT ${extract_result} EQUAL 0)
    message(FATAL_ERROR "Failed to extract CMake binary.")
endif()

# install 타겟 추가 (여기에 새로운 부분이 추가되었습니다)
add_custom_target(install
    COMMAND ${CMAKE_COMMAND} -E echo "CMake ${cmake_version} has been installed to ${CMAKE_INSTALL_PREFIX}"
)