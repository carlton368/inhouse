import os
import subprocess
import sys

def build(source_path, build_path, install_path, targets):
    # 소스 코드 다운로드 (특정 버전 태그 사용)
    subprocess.check_call(["git", "clone", "--depth", "1", "--branch", "3.4", "https://bitbucket.org/multicoreware/x265_git.git"])
    
    # 빌드 디렉토리 생성 및 이동
    os.makedirs("x265_build", exist_ok=True)
    os.chdir("x265_build")
    
    # CMake 설정 및 빌드
    cmake_cmd = [
        "cmake",
        "../x265_git/source",
        f"-DCMAKE_INSTALL_PREFIX={install_path}",
        "-DENABLE_SHARED=ON",
        "-DENABLE_CLI=ON",
        "-DENABLE_LIBNUMA=OFF",  # ffmpeg 4.1.11 호환성을 위해 비활성화
        "-DHIGH_BIT_DEPTH=OFF"   # 기본 8-bit depth 사용
    ]
    subprocess.check_call(cmake_cmd)
    
    # 빌드 및 설치
    subprocess.check_call(["make", "-j4"])
    subprocess.check_call(["make", "install"])

if __name__ == "__main__":
    install_path = os.environ["REZ_BUILD_INSTALL_PATH"]
    build_path = os.environ["REZ_BUILD_PATH"]
    source_path = os.path.dirname(os.path.realpath(__file__))
    
    build(source_path, build_path, install_path, targets=None)