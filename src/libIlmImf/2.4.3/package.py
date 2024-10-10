# package.py
name = "libIlmImf"
version = "2.4.3"  # 사용하려는 libIlmImf 버전으로 변경

authors = ["Industrial Light & Magic"]
description = "libIlmImf is a library for reading and writing OpenEXR image files."
license = "BSD-3-Clause"
url = "https://www.openexr.com/"

# 빌드 타임 의존성: 빌드 시 필요한 도구들
build_requires = [
    "gcc-4.8+",          # CentOS 7의 기본 GCC 버전
    "cmake-3.26.6+",     # 빌드 시스템 생성 도구
    "zlib-1.2.11+",      # 데이터 압축 라이브러리
    "IlmBase-2.4.3+"    # openEXR의 기반 라이브러리
]

# 런타임 의존성: libIlmImf가 동작하는 데 필요한 라이브러리들
requires = [
    "zlib-1.2.11+",
    "IlmBase-2.4.3+"
]

variants = [
    ["platform-linux", "arch-x86_64", "os-CentOS-7.9.2009"]
]

tools = [
    "ImfDump",      # libIlmImf 도구 예시
    "ImfReanimator"
]

# 빌드 명령어 정의: build.py를 실행하도록 설정
build_command = "python3 {root}/build.py {install_path}"

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.prepend("{root}/lib64")
    env.PKG_CONFIG_PATH.prepend("{root}/lib64/pkgconfig")
    env.C_INCLUDE_PATH.prepend("{root}/include")
