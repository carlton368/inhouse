name = "pkg-config"
version = "0.29.2"  # 원하는 버전으로 수정

authors = ["Freedesktop"]  
description = """
pkg-config is a helper tool used when compiling applications and libraries.
It helps to manage compile and link flags for libraries.
"""

requires = []
build_requires = ["python-3"]  # rez-build 제거
private_build_requires = []

variants = [["platform-linux", "arch-x86_64"]]

tools = ["pkg-config"]  # 필요한 도구만 포함

# 빌드 커맨드를 python3 build.py {install_path}로 지정
build_command = "python3 build.py {install_path}"

def commands():
    """환경 변수를 설정합니다."""
    env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")
    env.PATH.prepend("{root}/bin")