name = "python"
version = "3.7.7"
authors = ["wonjin LEE"]
description = "Python programming language"

tools = [
    "python",
    "python3",
    "pip",
    "pip3"
]

# 런타임 의존성
requires = [
    "platform-linux",
    "arch-x86_64"
]

# 빌드 타임 의존성
build_requires = [
    "cmake-3.10+",
    "make",
    "gcc"
]

variants = [
    ["platform-linux", "arch-x86_64"]
]

def commands():
    # 환경 변수 설정
    env.PATH.prepend("{root}/bin")
    env.PYTHONPATH.prepend("{root}/lib/python3.7/site-packages")
    env.LD_LIBRARY_PATH.prepend("{root}/lib")

build_command = """
cmake -DCMAKE_INSTALL_PREFIX={install_path} {root} && \
cmake --build . --target install_python && \
ln -sf {install_path}/bin/python3.7 {install_path}/bin/python
"""

def pre_build_commands():
    env.REZ_BUILD_CONFIG = "Release"

