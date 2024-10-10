# package.py
name = "nasm"
version = "2.15.05"  # NASM의 최신 안정 버전을 사용합니다.

authors = ["H. Peter Anvin", "Jim Kukunas", "Frank B. Warren", "Cyrill Gorcunov"]

description = "NASM (Netwide Assembler) is an 80x86 and x86-64 assembler. CentOS 7 build."

variants = [
    ["platform-linux", "arch-x86_64", "os-CentOS-7"]
]

tools = ["nasm", "ndisasm"]

requires = [
    "gcc-4.8+",  # CentOS 7의 기본 GCC 버전
]

def commands():
    env.PATH.append("{root}/bin")
    env.MANPATH.append("{root}/share/man")

build_command = "python3 {root}/build.py {install_path}"
