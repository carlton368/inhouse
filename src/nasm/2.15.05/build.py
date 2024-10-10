# build.py
import os
import sys
import subprocess
from pathlib import Path

def build(source_path, build_path, install_path, targets):
    # NASM 소스코드 다운로드
    nasm_url = "https://www.nasm.us/pub/nasm/releasebuilds/2.15.05/nasm-2.15.05.tar.xz"
    subprocess.check_call(["curl", "-L", nasm_url, "-o", "nasm.tar.xz"])
    subprocess.check_call(["tar", "-xvf", "nasm.tar.xz"])
    
    # 소스 디렉토리로 이동
    os.chdir("nasm-2.15.05")
    
    # Configure 스크립트 실행
    configure_cmd = [
        "./configure",
        f"--prefix={install_path}",
    ]
    subprocess.check_call(configure_cmd)
    
    # 빌드 및 설치
    subprocess.check_call(["make", "-j4"])  # 4개의 병렬 작업으로 빌드
    subprocess.check_call(["make", "install"])

if __name__ == "__main__":
    install_path = os.environ["REZ_BUILD_INSTALL_PATH"]
    build_path = os.environ["REZ_BUILD_PATH"]
    source_path = os.path.dirname(os.path.realpath(__file__))
    
    build(source_path, build_path, install_path, targets=None)