# build.py
import os
import sys
import subprocess
from pathlib import Path

def build(source_path, build_path, install_path, targets):
    # zlib 소스코드 다운로드
    zlib_url = "https://zlib.net/fossils/zlib-1.2.11.tar.gz"
    subprocess.check_call(["curl", "-L", zlib_url, "-o", "zlib.tar.gz"])
    subprocess.check_call(["tar", "-xzvf", "zlib.tar.gz"])
    
    # 소스 디렉토리로 이동
    os.chdir("zlib-1.2.11")
    
    # Configure 스크립트 실행
    configure_cmd = [
        "./configure",
        f"--prefix={install_path}",
    ]
    subprocess.check_call(configure_cmd)
    
    # 빌드 및 설치
    subprocess.check_call(["make", "-j4"])  # 4개의 병렬 작업으로 빌드
    subprocess.check_call(["make", "install"])

    # pkgconfig 파일 생성
    pkgconfig_dir = os.path.join(install_path, "lib", "pkgconfig")
    os.makedirs(pkgconfig_dir, exist_ok=True)
    with open(os.path.join(pkgconfig_dir, "zlib.pc"), "w") as f:
        f.write(f"""
prefix={install_path}
exec_prefix=${{prefix}}
libdir=${{exec_prefix}}/lib
includedir=${{prefix}}/include

Name: zlib
Description: zlib compression library
Version: 1.2.11

Requires:
Libs: -L${{libdir}} -lz
Cflags: -I${{includedir}}
""")

if __name__ == "__main__":
    install_path = os.environ["REZ_BUILD_INSTALL_PATH"]
    build_path = os.environ["REZ_BUILD_PATH"]
    source_path = os.path.dirname(os.path.realpath(__file__))
    
    build(source_path, build_path, install_path, targets=None)