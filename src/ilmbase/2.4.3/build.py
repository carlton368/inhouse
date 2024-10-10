# -*- coding: utf-8 -*-
# build.py
import os
import sys
import subprocess
import hashlib

def download_source(source_path, ilmbase_url, archive_name):
    """IlmBase 소스 코드를 다운로드합니다."""
    archive_path = os.path.join(source_path, archive_name)

    if not os.path.exists(archive_path):
        print(f"IlmBase 소스 코드를 {ilmbase_url}에서 다운로드 중...")
        try:
            subprocess.check_call(["curl", "-L", "--fail", ilmbase_url, "-o", archive_path])
        except subprocess.CalledProcessError as e:
            print(f"IlmBase 소스 다운로드에 실패했습니다: {e}")
            sys.exit(1)
        print("다운로드 완료.")
    else:
        print(f"소스 아카이브가 이미 존재합니다: {archive_path}")

    # 파일 크기 확인
    file_size = os.path.getsize(archive_path)
    print(f"다운로드된 파일 크기: {file_size} bytes")
    if file_size < 100000:  # 예시로 100KB 미만이면 실패로 간주
        print("다운로드된 파일이 너무 작습니다. 다운로드가 제대로 완료되지 않았을 수 있습니다.")
        sys.exit(1)

    return archive_path

def verify_checksum(archive_path, expected_checksum):
    """소스 아카이브의 체크섬을 검증합니다."""
    print("체크섬을 검증 중...")
    sha256 = hashlib.sha256()
    with open(archive_path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            sha256.update(chunk)
    calculated_checksum = sha256.hexdigest()
    if calculated_checksum != expected_checksum:
        raise ValueError(f"체크섬 불일치: 예상 {expected_checksum}, 실제 {calculated_checksum}")
    print("체크섬 검증 성공.")

def extract_archive(archive_path, build_path):
    """소스 아카이브를 추출합니다."""
    print(f"{archive_path}를 {build_path}로 추출 중...")
    try:
        # .tar.gz 형식 추출
        subprocess.check_call(["tar", "-xzf", archive_path, "-C", build_path])
    except subprocess.CalledProcessError as e:
        print(f"아카이브 추출에 실패했습니다: {e}")
        sys.exit(1)
    print("추출 완료.")

def configure_ilmbase(source_dir, install_path):
    """IlmBase를 구성합니다."""
    os.chdir(source_dir)

    # 빌드를 위한 환경 변수 설정
    env = os.environ.copy()
    env["PKG_CONFIG_PATH"] = f"{install_path}/lib64/pkgconfig:" + env.get("PKG_CONFIG_PATH", "")
    env["CFLAGS"] = f"-I{install_path}/include " + env.get("CFLAGS", "")
    env["LDFLAGS"] = f"-L{install_path}/lib64 " + env.get("LDFLAGS", "")

    # CMake 구성 명령어
    configure_cmd = [
        "cmake",
        f"-DCMAKE_INSTALL_PREFIX={install_path}",
        "-DBUILD_SHARED_LIBS=ON",
        "-DCMAKE_BUILD_TYPE=Release",
        "."  # 소스 디렉토리
    ]

    print("IlmBase를 구성 중...")
    subprocess.check_call(configure_cmd, env=env)

def build_ilmbase(source_dir):
    """IlmBase를 빌드합니다."""
    os.chdir(source_dir)
    print("IlmBase를 빌드 중...")
    subprocess.check_call(["make", "-j4"])  # 4개의 병렬 작업으로 빌드

def install_ilmbase(source_dir):
    """IlmBase를 설치합니다."""
    os.chdir(source_dir)
    print("IlmBase를 설치 중...")
    subprocess.check_call(["make", "install"])  # 설치

def build(source_path, build_path, install_path, targets):
    """IlmBase 빌드 스크립트."""
    print("IlmBase 빌드 프로세스를 시작합니다...")

    # IlmBase 소스코드 다운로드 (.tar.gz 사용)
    ilmbase_url = "https://github.com/AcademySoftwareFoundation/openexr/archive/refs/tags/v2.4.3.tar.gz"  # 버전에 맞는 URL
    archive_name = "openexr-2.4.3.tar.gz"
    archive_path = download_source(source_path, ilmbase_url, archive_name)

    # 체크섬 검증
    expected_checksum = "017367529a21196905bcabc6f046f3033363d90115395196b9c1abd0ad80606a"  
    verify_checksum(archive_path, expected_checksum)

    # 소스 아카이브 추출
    extract_archive(archive_path, build_path)

    # 추출된 소스 디렉토리 경로
    ilmbase_source_dir = os.path.join(build_path, "openexr-2.4.3", "IlmBase")
    if not os.path.exists(ilmbase_source_dir):
        raise FileNotFoundError(f"소스 디렉토리가 존재하지 않습니다: {ilmbase_source_dir}")

    # IlmBase 구성
    configure_ilmbase(ilmbase_source_dir, install_path)

    # IlmBase 빌드
    build_ilmbase(ilmbase_source_dir)

    # IlmBase 설치
    install_ilmbase(ilmbase_source_dir)

    print("IlmBase가 성공적으로 빌드되고 설치되었습니다.")

if __name__ == "__main__":
    # 환경 변수에서 경로를 읽어옵니다.
    install_path = os.environ.get("REZ_BUILD_INSTALL_PATH")
    build_path = os.environ.get("REZ_BUILD_PATH")
    source_path = os.environ.get("REZ_BUILD_SOURCE_PATH", os.path.dirname(os.path.realpath(__file__)))

    if not install_path or not build_path:
        print("환경 변수 REZ_BUILD_INSTALL_PATH 또는 REZ_BUILD_PATH가 설정되지 않았습니다.")
        sys.exit(1)

    build(source_path, build_path, install_path, targets=None)
