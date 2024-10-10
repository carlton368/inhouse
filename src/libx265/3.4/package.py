name = "libx265"
version = "3.4"  # ffmpeg 4.1.11과 호환되는 x265 버전

requires = [
    "gcc-4.8+<9",  # gcc 9 이상은 호환성 문제를 일으킬 수 있음
    "cmake-3.1+<3.30",  # 너무 새로운 CMake 버전은 피함
    "nasm-2.13+<2.16"  # 안정적인 nasm 버전 범위
]

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")
    env.PATH.prepend("{root}/bin")

build_command = "python3 {root}/build.py {install_path}"