name = "cmake"
version = "3.26.6"  # 버전을 3.26.6으로 수정
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

def pre_build_commands():
    env.REZ_BUILD_CONFIG = "Release"

# CMakelists.txt과 함께 사용할 package.py 파일