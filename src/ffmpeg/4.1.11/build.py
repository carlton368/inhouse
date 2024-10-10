# -*- coding: utf-8 -*-
# build.py
import os
import sys
import subprocess
import hashlib

def download_source(source_path, ffmpeg_url, archive_name):
    """FFmpeg 소스 코드를 다운로드합니다."""
    archive_path = os.path.join(source_path, archive_name)
    
    if not os.path.exists(archive_path):
        print(f"FFmpeg 소스 코드를 {ffmpeg_url}에서 다운로드 중...")
        try:
            # --fail 옵션 추가하여 HTTP 오류 시 실패하도록 함
            subprocess.check_call(["curl", "-L", "--fail", ffmpeg_url, "-o", archive_path])
        except subprocess.CalledProcessError as e:
            print(f"FFmpeg 소스 다운로드에 실패했습니다: {e}")
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

def configure_ffmpeg(source_dir, install_path):
    """FFmpeg을 구성합니다."""
    os.chdir(source_dir)
    
    # 빌드를 위한 환경 변수 설정
    env = os.environ.copy()
    env["PKG_CONFIG_PATH"] = f"{install_path}/lib/pkgconfig:" + env.get("PKG_CONFIG_PATH", "")
    env["CFLAGS"] = f"-I{install_path}/include " + env.get("CFLAGS", "")
    env["LDFLAGS"] = f"-L{install_path}/lib " + env.get("LDFLAGS", "")
    
    # FFmpeg 구성 명령어
    configure_cmd = [
        "./configure",
        f"--prefix={install_path}",
        "--enable-gpl",
        "--enable-nonfree",
        "--enable-libx264",
        "--disable-static",
        "--enable-shared",
        "--enable-pthreads",
        "--enable-postproc",
        "--enable-zlib"  # 올바른 옵션으로 수정
    ]
    
    print("FFmpeg을 구성 중...")
    subprocess.check_call(configure_cmd, env=env)

def build_ffmpeg(source_dir):
    """FFmpeg을 빌드합니다."""
    os.chdir(source_dir)
    print("FFmpeg을 빌드 중...")
    subprocess.check_call(["make", "-j4"])  # 4개의 병렬 작업으로 빌드

def install_ffmpeg(source_dir):
    """FFmpeg을 설치합니다."""
    os.chdir(source_dir)
    print("FFmpeg을 설치 중...")
    subprocess.check_call(["make", "install"])  # 설치

def build(source_path, build_path, install_path, targets):
    """FFmpeg 빌드 스크립트."""
    print("FFmpeg 빌드 프로세스를 시작합니다...")
    
    # FFmpeg 소스코드 다운로드 (.tar.gz 사용)
    ffmpeg_url = "https://www.ffmpeg.org/releases/ffmpeg-4.1.11.tar.gz"
    archive_name = "ffmpeg-4.1.11.tar.gz"
    archive_path = download_source(source_path, ffmpeg_url, archive_name)
    
    # 체크섬 검증
    expected_checksum = "5c46dbd3c9c1becb372cf4f6d4b32bb9ed86f81119356f461ce0402af238eb22"
    verify_checksum(archive_path, expected_checksum)
    
    # 소스 아카이브 추출
    extract_archive(archive_path, build_path)
    
    # 추출된 소스 디렉토리 경로
    ffmpeg_source_dir = os.path.join(build_path, "ffmpeg-4.1.11")
    if not os.path.exists(ffmpeg_source_dir):
        raise FileNotFoundError(f"소스 디렉토리가 존재하지 않습니다: {ffmpeg_source_dir}")
    
    # FFmpeg 구성
    configure_ffmpeg(ffmpeg_source_dir, install_path)
    
    # FFmpeg 빌드
    build_ffmpeg(ffmpeg_source_dir)
    
    # FFmpeg 설치
    install_ffmpeg(ffmpeg_source_dir)
    
    print("FFmpeg이 성공적으로 빌드되고 설치되었습니다.")

if __name__ == "__main__":
    # 환경 변수에서 경로를 읽어옵니다.
    install_path = os.environ.get("REZ_BUILD_INSTALL_PATH")
    build_path = os.environ.get("REZ_BUILD_PATH")
    source_path = os.environ.get("REZ_BUILD_SOURCE_PATH", os.path.dirname(os.path.realpath(__file__)))
    
    if not install_path or not build_path:
        print("환경 변수 REZ_BUILD_INSTALL_PATH 또는 REZ_BUILD_PATH가 설정되지 않았습니다.")
        sys.exit(1)
    
    build(source_path, build_path, install_path, targets=None)
