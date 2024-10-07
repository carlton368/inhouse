name = "cmake"
version = "3.26.6"
description = """
    CMake is an extensible, open-source system that manages the build process 
    in an operating system and in a compiler-independent manner.
"""

authors = ["Kitware"]

variants = [
    ["platform-linux", "arch-aarch64"]
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
    env.REZ_BUILD_CONFIG = "Release"

