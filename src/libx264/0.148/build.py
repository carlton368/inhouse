import os
import subprocess
import sys

def build(source_path, build_path, install_path, targets):
    # 소스 코드 다운로드
    subprocess.check_call(["git", "clone", "--depth", "1", "--branch", "stable", "https://github.com/mirror/x264.git"])
    
    # 빌드 디렉토리로 이동
    os.chdir("x264")
    
    # 설정 및 빌드
    configure_cmd = [
        "./configure",
        f"--prefix={install_path}",
        "--enable-shared",
        "--enable-static",
    ]
    subprocess.check_call(configure_cmd)
    
    # 빌드 및 설치
    subprocess.check_call(["make", "-j4"])
    subprocess.check_call(["make", "install"])

if __name__ == "__main__":
    install_path = os.environ["REZ_BUILD_INSTALL_PATH"]
    build_path = os.environ["REZ_BUILD_PATH"]
    source_path = os.path.dirname(os.path.realpath(__file__))
    
    build(source_path, build_path, install_path, targets=None)