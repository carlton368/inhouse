import os
import sys
import urllib.request
import tarfile
import shutil
import tempfile

def main():
    if len(sys.argv) < 2:
        print("사용법: build.py <설치 경로>")
        sys.exit(1)

    # 설치 경로를 인자로 받음
    install_path = os.path.abspath(sys.argv[1])
    version = "3.26.6"            # CMake 버전
    short_version = "3.26"        # 짧은 버전 (URL 생성을 위한 변수)
    platform = "linux"            # 리눅스 플랫폼 가정
    arch = os.uname().machine      # 시스템 아키텍처 감지

    # 아키텍처에 맞는 CMake tarball 이름 설정
    if arch == "x86_64":
        arch_str = "x86_64"
    elif arch == "aarch64":
        arch_str = "aarch64"
    else:
        print(f"지원되지 않는 아키텍처: {arch}")
        sys.exit(1)

    # 다운로드 URL 생성
    url = f"https://cmake.org/files/v{short_version}/cmake-{version}-linux-{arch_str}.tar.gz"
    download_dir = os.path.join(os.getcwd(), "downloads")
    os.makedirs(download_dir, exist_ok=True)
    tarball = os.path.join(download_dir, f"cmake-{version}-linux-{arch_str}.tar.gz")

    # CMake tarball 다운로드
    try:
        print(f"{url}에서 CMake를 다운로드 중...")
        with urllib.request.urlopen(url) as response, open(tarball, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
        print("다운로드가 성공적으로 완료되었습니다.")
    except Exception as e:
        print(f"CMake 바이너리 다운로드 실패: {e}")
        sys.exit(1)

    # tarball 압축 해제 및 설치
    try:
        print(f"{install_path}에 CMake를 압축 해제 중...")
        with tarfile.open(tarball, "r:gz") as tar:
            temp_dir = tempfile.mkdtemp()
            tar.extractall(path=temp_dir)
            
            # tarball에 단일 최상위 디렉토리가 있는지 확인
            top_level = os.listdir(temp_dir)
            if len(top_level) != 1:
                print("예상치 못한 tarball 구조입니다.")
                sys.exit(1)
            
            top_dir = os.path.join(temp_dir, top_level[0])
            
            # 기존 설치 경로가 있을 경우 삭제
            if os.path.exists(install_path):
                shutil.rmtree(install_path)
            
            # 압축 해제된 파일을 설치 경로로 이동
            shutil.move(top_dir, install_path)
            shutil.rmtree(temp_dir)
        print(f"CMake {version}가 {install_path}에 성공적으로 설치되었습니다.")
    except Exception as e:
        print(f"CMake 바이너리 압축 해제 실패: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

