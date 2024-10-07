name = "make"
version = "4.3"  # 최신 안정 버전을 사용합니다. 필요에 따라 변경 가능합니다.
authors = ["Rez User"]
description = "GNU Make build tool"

variants = [
    ["platform-linux", "arch-x86_64"]
]

build_requires = [
    "gcc",
    "cmake-3.10+"
]

def commands():
    env.PATH.prepend("{root}/bin")

build_command = "bash {root}/build.sh {install_path}"

def pre_build_commands():
    env.REZ_BUILD_CONFIG = "Release"

# build.sh와 함께 사용할 package.py 파일