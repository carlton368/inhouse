# -*- coding: utf-8 -*-
# build.py
import os
import sys
import subprocess
import hashlib

def download_source(source_path, libilmimf_url, archive_name):
    """
    libIlmImf 소스 코드를 다운로드합니다.
    
    Parameters:
        source_path (str): 소스 코드를 저장할 디렉토리 경로.
        libilmimf_url (str): 소스 코드 다운로드 URL.
        archive_name (str): 저장할 아카이브 파일 이름.
    
    Returns:
        str: 다운로드된 아카이브 파일의 전체 경로.
    """
    # 아카이브 파일의 전체 경로를 설정
    archive_path = os.path.join(source_path, archive_name)

    # 아카이브 파일이 이미 존재하는지 확인
    if not os.path.exists(archive_path):
        print(f"libIlmImf 소스 코드를 {libilmimf_url}에서 다운로드 중...")
        try:
            # curl 명령어를 사용하여 소스 코드를 다운로드
            subprocess.check_call(["curl", "-L", "--fail", libilmimf_url, "-o", archive_path])
        except subprocess.CalledProcessError as e:
            print(f"libIlmImf 소스 다운로드에 실패했습니다: {e}")
            sys.exit(1)
        print("다운로드 완료.")
    else:
        print(f"소스 아카이브가 이미 존재합니다: {archive_path}")

    # 다운로드된 파일의 크기를 확인
    file_size = os.path.getsize(archive_path)
    print(f"다운로드된 파일 크기: {file_size} bytes")
    if file_size < 100000:  # 예시로 100KB 미만이면 실패로 간주
        print("다운로드된 파일이 너무 작습니다. 다운로드가 제대로 완료되지 않았을 수 있습니다.")
        sys.exit(1)

    return archive_path

def verify_checksum(archive_path, expected_checksum):
    """
    소스 아카이브의 체크섬을 검증합니다.
    
    Parameters:
        archive_path (str): 검증할 아카이브 파일의 경로.
        expected_checksum (str): 예상되는 SHA256 체크섬 값.
    
    Raises:
        ValueError: 체크섬이 일치하지 않을 경우 발생.
    """
    print("체크섬을 검증 중...")
    sha256 = hashlib.sha256()
    with open(archive_path, "rb") as f:
        # 파일을 8KB 단위로 읽어 해시 계산
        for chunk in iter(lambda: f.read(8192), b""):
            sha256.update(chunk)
    calculated_checksum = sha256.hexdigest()
    if calculated_checksum != expected_checksum:
        raise ValueError(f"체크섬 불일치: 예상 {expected_checksum}, 실제 {calculated_checksum}")
    print("체크섬 검증 성공.")

def extract_archive(archive_path, build_path):
    """
    소스 아카이브를 추출합니다.
    
    Parameters:
        archive_path (str): 추출할 아카이브 파일의 경로.
        build_path (str): 아카이브를 추출할 디렉토리 경로.
    
    Raises:
        subprocess.CalledProcessError: 추출 과정에서 오류 발생 시.
    """
    print(f"{archive_path}를 {build_path}로 추출 중...")
    try:
        # tar 명령어를 사용하여 .tar.gz 형식의 아카이브를 추출
        subprocess.check_call(["tar", "-xzf", archive_path, "-C", build_path])
    except subprocess.CalledProcessError as e:
        print(f"아카이브 추출에 실패했습니다: {e}")
        sys.exit(1)
    print("추출 완료.")

def configure_libIlmImf(source_dir, install_path):
    """
    libIlmImf를 구성합니다.
    
    Parameters:
        source_dir (str): 소스 디렉토리 경로.
        install_path (str): 설치할 경로.
    
    Raises:
        subprocess.CalledProcessError: 구성 과정에서 오류 발생 시.
    """
    # 소스 디렉토리로 이동
    os.chdir(source_dir)

    # 빌드를 위한 환경 변수 설정
    env = os.environ.copy()
    env["PKG_CONFIG_PATH"] = f"{install_path}/lib64/pkgconfig:" + env.get("PKG_CONFIG_PATH", "")
    env["CFLAGS"] = f"-I{install_path}/include " + env.get("CFLAGS", "")
    env["LDFLAGS"] = f"-L{install_path}/lib64 " + env.get("LDFLAGS", "")

    # CMake 구성 명령어 설정
    configure_cmd = [
        "cmake",
        f"-DCMAKE_INSTALL_PREFIX={install_path}",  # 설치 경로 지정
        "-DBUILD_SHARED_LIBS=ON",                 # 공유 라이브러리 빌드 설정
        "-DCMAKE_BUILD_TYPE=Release",              # 빌드 타입 설정
        "."                                        # 현재 디렉토리에서 CMake 설정
    ]

    print("libIlmImf를 구성 중...")
    # CMake 명령어 실행
    subprocess.check_call(configure_cmd, env=env)

def build_libIlmImf(source_dir):
    """
    libIlmImf를 빌드합니다.
    
    Parameters:
        source_dir (str): 소스 디렉토리 경로.
    
    Raises:
        subprocess.CalledProcessError: 빌드 과정에서 오류 발생 시.
    """
    # 소스 디렉토리로 이동
    os.chdir(source_dir)
    print("libIlmImf를 빌드 중...")
    # make 명령어를 사용하여 빌드 (병렬 작업 4개)
    subprocess.check_call(["make", "-j4"])

def install_libIlmImf(source_dir):
    """
    libIlmImf를 설치합니다.
    
    Parameters:
        source_dir (str): 소스 디렉토리 경로.
    
    Raises:
        subprocess.CalledProcessError: 설치 과정에서 오류 발생 시.
    """
    # 소스 디렉토리로 이동
    os.chdir(source_dir)
    print("libIlmImf를 설치 중...")
    # make install 명령어를 사용하여 설치
    subprocess.check_call(["make", "install"])

def build(source_path, build_path, install_path, targets):
    """
    libIlmImf 빌드 스크립트의 메인 함수입니다.
    
    Parameters:
        source_path (str): 소스 파일을 저장할 디렉토리 경로.
        build_path (str): 빌드 파일을 저장할 디렉토리 경로.
        install_path (str): 설치 경로.
        targets (list): 빌드할 타겟 목록 (사용되지 않음).
    """
    print("libIlmImf 빌드 프로세스를 시작합니다...")

    # libIlmImf 소스코드 다운로드 URL 및 아카이브 이름 설정
    libilmimf_url = "https://github.com/AcademySoftwareFoundation/openexr/archive/refs/tags/v2.4.3.tar.gz"  # 소스 코드 다운로드 URL
    archive_name = "openexr-2.4.3.tar.gz"  # 아카이브 파일 이름

    # 소스 코드 다운로드
    archive_path = download_source(source_path, libilmimf_url, archive_name)

    # 체크섬 검증
    expected_checksum = "017367529a21196905bcabc6f046f3033363d90115395196b9c1abd0ad80606a"  # 실제 체크섬으로 교체 필요
    verify_checksum(archive_path, expected_checksum)

    # 소스 아카이브 추출
    extract_archive(archive_path, build_path)

    # 추출된 소스 디렉토리 경로 설정
    # 원래는 "openexr-2.4.3/IlmImf" 경로을 참조했으나 실제 구조는 "openexr-2.4.3/OpenEXR/IlmImf"임
    libilmimf_source_dir = os.path.join(build_path, "openexr-2.4.3", "OpenEXR", "IlmImf")
    
    # 소스 디렉토리 존재 여부 확인
    if not os.path.exists(libilmimf_source_dir):
        raise FileNotFoundError(f"소스 디렉토리가 존재하지 않습니다: {libilmimf_source_dir}")

    # libIlmImf 구성
    configure_libIlmImf(libilmimf_source_dir, install_path)

    # libIlmImf 빌드
    build_libIlmImf(libilmimf_source_dir)

    # libIlmImf 설치
    install_libIlmImf(libilmimf_source_dir)

    print("libIlmImf가 성공적으로 빌드되고 설치되었습니다.")

if __name__ == "__main__":
    """
    스크립트의 진입점입니다.
    환경 변수에서 설치 경로, 빌드 경로, 소스 경로를 읽어와 빌드 과정을 시작합니다.
    """
    # 환경 변수에서 경로를 읽어옵니다.
    install_path = os.environ.get("REZ_BUILD_INSTALL_PATH")  # 설치 경로
    build_path = os.environ.get("REZ_BUILD_PATH")          # 빌드 경로
    source_path = os.environ.get("REZ_BUILD_SOURCE_PATH", os.path.dirname(os.path.realpath(__file__)))  # 소스 경로

    # 설치 경로와 빌드 경로가 설정되어 있는지 확인
    if not install_path or not build_path:
        print("환경 변수 REZ_BUILD_INSTALL_PATH 또는 REZ_BUILD_PATH가 설정되지 않았습니다.")
        sys.exit(1)

    # 빌드 함수 호출
    build(source_path, build_path, install_path, targets=None)
