name = "python"
version = "3.7.7"
authors = ["Guido van Rossum"]
description = \
    """ 프로그래밍 언어인 Python 3.7.7 버전"""

tools = [
    "python",
    "python3",
    "python3.7",
    "pip",
    "pip3",
    "idle",
    "pydoc"
]

uuid = "repository.python"

variants = [
    ["platform-linux", "arch-x86_64"]
]

build_requires = [
    "cmake-3.0+",
    "make",
    "gcc"
]

def commands():
    # 환경 변수 설정
    env.PATH.prepend("{root}/bin")
    env.PYTHONPATH.prepend("{root}/lib/python3.7/site-packages")
    env.LD_LIBRARY_PATH.prepend("{root}/lib")
    env.PYTHONHOME = "{root}"

build_command = """
mkdir -p {build_path} && cd {build_path} && \\
cmake -DCMAKE_INSTALL_PREFIX={install_path} -DCMAKE_BUILD_TYPE=Release {root} && \\
cmake --build . --target install && \\
ln -sf {install_path}/bin/python3.7 {install_path}/bin/python
"""

def test_commands():
    command("python --version")
