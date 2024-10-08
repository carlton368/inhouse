name = "cmake"
version = "3.26.6"
description = """
    CMake is an extensible, open-source system that manages the build process 
    in an operating system and in a compiler-independent manner.
"""

authors = ["Kitware"]

variants = [
    ["platform-linux", "arch-x86_64"]
]

tools = [
    "cmake",
    "ctest",
    "cpack",
    "ccmake"
]

def commands():
    env.PATH.prepend("{root}/bin")
    env.CMAKE_MODULE_PATH.append("{root}/share/cmake-{version}/Modules")
    env.MANPATH.append("{root}/share/man")
    

build_command = "python3 {root}/build.py {install_path}"

def pre_build_commands():
    print("CMake pre_build_commands() called")
    env.REZ_BUILD_CONFIG = "Release"
    print("알림: {root}는 'root'입니다.")
    print("알림: {install_path}는 'install_paht'입니다.")
    



