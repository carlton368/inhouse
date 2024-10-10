# package.py
name = "ffmpeg"
version = "4.1.11"  # 버전 업데이트

authors = ["FFmpeg Developers"]
description = "FFmpeg is a complete, cross-platform solution to record, convert and stream audio and video."
license = "GPLv3"
url = "https://ffmpeg.org/"

# 빌드 타임 의존성: 빌드 시 필요한 도구들
build_requires = [
    "gcc-4.8+",          # CentOS 7의 기본 GCC 버전
    "yasm-1.3.0+",       # 어셈블리 컴파일러
    "nasm-2.15.05+",     # NASM 어셈블러
    "cmake-3.26.6+"
]

# 런타임 의존성: FFmpeg이 동작하는 데 필요한 라이브러리들
requires = [
    "zlib-1.2.11+",
    "libx264-0.148+",  # x264 라이브러리
    "libx265-3.4+"
]

variants = [
    ["platform-linux", "arch-x86_64", "os-CentOS-7.9.2009"]
]

tools = [
    "ffmpeg",
    "ffplay",
    "ffprobe"
]

# 빌드 명령어 정의: build.py를 실행하도록 설정
build_command = "python3 {root}/build.py {install_path}"

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.prepend("{root}/lib")
    env.PKG_CONFIG_PATH.prepend("{root}/lib/pkgconfig")
    env.C_INCLUDE_PATH.prepend("{root}/include")
