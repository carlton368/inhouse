# -*- coding: utf-8 -*-
# build.py
import os
import sys
import subprocess
from pathlib import Path

def build(source_path, build_path, install_path, targets):
    # Yasm 소스코드 다운로드
    yasm_url = "https://www.tortall.net/projects/yasm/releases/yasm-1.3.0.tar.gz"
    subprocess.check_call(["curl", "-L", yasm_url, "-o", "yasm.tar.gz"])
    subprocess.check_call(["tar", "-xzvf", "yasm.tar.gz"])
    
    # 소스 디렉토리로 이동
    os.chdir("yasm-1.3.0")
    
    # Configure 스크립트 실행
    configure_cmd = [
        "./configure",
        f"--prefix={install_path}",
        "--disable-nls",  # NLS 비활성화 (CentOS 7에서 문제 발생 가능성 줄임)
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
