# package.py
name = "zlib"
version = "1.2.11"  # zlib의 안정 버전을 사용합니다.

authors = ["Jean-loup Gailly", "Mark Adler"]

description = "zlib is a general purpose data compression library. CentOS 7 build."

variants = [
    ["platform-linux", "arch-x86_64", "os-CentOS-7"]
]

requires = [
    "gcc-4.8+",  # CentOS 7의 기본 GCC 버전
]

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")

build_command = "python3 {root}/build.py {install_path}"