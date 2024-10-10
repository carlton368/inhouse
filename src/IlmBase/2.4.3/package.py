# package.py
name = "IlmBase"
version = "2.4.3"  # 사용하려는 IlmBase 버전으로 변경

authors = ["Industrial Light & Magic"]
description = "IlmBase is a collection of libraries used by OpenEXR and other ILM software."
license = "BSD-3-Clause"
url = "https://www.openexr.com/"

# 빌드 타임 의존성: 빌드 시 필요한 도구들
build_requires = [
    "gcc-4.8+",          # CentOS 7의 기본 GCC 버전
    "cmake-3.26.6+",     # 빌드 시스템 생성 도구
    "zlib-1.2.11+"    # 데이터 압축 라이브러리
]

# 런타임 의존성: IlmBase가 동작하는 데 필요한 라이브러리들
requires = [
    "zlib-1.2.11+"
]

variants = [
    ["platform-linux", "arch-x86_64", "os-CentOS-7.9.2009"]
]

tools = [
    # IlmBase는 주로 라이브러리이므로, 별도의 도구가 필요하지 않을 수 있습니다.
    # 필요 시 여기에 도구 이름을 추가하세요.
]

# 빌드 명령어 정의: build.py를 실행하도록 설정
build_command = "python3 {root}/build.py {install_path}"

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.prepend("{root}/lib64")
    env.PKG_CONFIG_PATH.prepend("{root}/lib64/pkgconfig")
    env.C_INCLUDE_PATH.prepend("{root}/include")
