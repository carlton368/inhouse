# package.py
# Rez 패키지 설정 파일

# 패키지 이름과 버전 정의
name = "libIlmImf"
version = "2.4.3"  # 사용하려는 libIlmImf 버전으로 변경

# 패키지 작성자 정보
authors = ["Industrial Light & Magic"]

# 패키지 설명
description = "libIlmImf은 OpenEXR 이미지 파일을 읽고 쓰기 위한 라이브러리입니다."

# 라이선스 정보
license = "BSD-3-Clause"

# 패키지의 공식 웹사이트 URL
url = "https://www.openexr.com/"

# 빌드 타임 의존성: 빌드 시 필요한 도구들
build_requires = [
    "gcc-4.8+",          # CentOS 7의 기본 GCC 버전
    "cmake-3.26.6+",     # 빌드 시스템 생성 도구
    "zlib-1.2.11+",      # 데이터 압축 라이브러리
    "IlmBase-2.4.3+"     # openEXR의 기반 라이브러리
]

# 런타임 의존성: libIlmImf가 동작하는 데 필요한 라이브러리들
requires = [
    "zlib-1.2.11+",
    "IlmBase-2.4.3+"
]

# 지원하는 플랫폼 및 아키텍처 정의
variants = [
    ["platform-linux", "arch-x86_64", "os-CentOS-7.9.2009"]
]

# 패키지에 포함된 도구들
tools = [
    "ImfDump",      # libIlmImf 도구 예시
    "ImfReanimator"
]

# 빌드 명령어 정의: build.py를 실행하도록 설정
build_command = "python3 {root}/build.py {install_path}"

def commands():
    """
    패키지를 사용할 때 필요한 환경 변수 설정을 정의합니다.
    """
    # 실행 파일 경로를 PATH에 추가
    env.PATH.prepend("{root}/bin")
    
    # 공유 라이브러리 경로를 LD_LIBRARY_PATH에 추가
    env.LD_LIBRARY_PATH.prepend("{root}/lib64")
    
    # pkg-config 파일 경로를 PKG_CONFIG_PATH에 추가
    env.PKG_CONFIG_PATH.prepend("{root}/lib64/pkgconfig")
    
    # C 헤더 파일 경로를 C_INCLUDE_PATH에 추가
    env.C_INCLUDE_PATH.prepend("{root}/include")
