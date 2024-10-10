# package.py
name = "yasm"
version = "1.3.0"

authors = ["Peter Johnson", "Michael Urman"]

description = "Yasm is a complete rewrite of the NASM assembler. CentOS 7 build."

variants = [
    ["platform-linux", "arch-x86_64", "os-CentOS-7"]
]

tools = ["yasm"]

requires = [
    "cmake-3+",
    "gcc-4.8+",  # CentOS 7의 기본 GCC 버전
]

def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")

build_command = "python3 {root}/build.py {install_path}"

def pre_build_commands():
    env.CMAKE_PREFIX_PATH.append('{root}')
