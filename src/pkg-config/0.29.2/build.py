import os, shutil, sys, stat, urllib.request, tarfile, glob

def download_tarball(url, dest):
    """지정된 URL에서 tarball을 다운로드합니다."""
    print(f"다운로드 중: {url}")
    try:
        with urllib.request.urlopen(url) as response, open(dest, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
        print(f"다운로드 완료: {dest}")
    except Exception as e:
        print(f"다운로드 중 오류 발생: {e}")
        sys.exit(1)

def extract_tarball(tarball_path, extract_to):
    """tar.gz 파일을 추출합니다."""
    print(f"소스 추출 중: {tarball_path} -> {extract_to}")
    try:
        with tarfile.open(tarball_path, "r:gz") as tar:
            tar.extractall(path=extract_to)
        print("소스 추출 완료")
    except Exception as e:
        print(f"소스 추출 중 오류 발생: {e}")
        sys.exit(1)

def configure(source_dir, install_path):
    """configure 스크립트를 실행합니다."""
    configure_cmd = f"./configure --prefix={install_path}"
    print(f"configure 실행 중: {configure_cmd}")
    result = os.system(configure_cmd)
    if result != 0:
        print("configure 실행 중 오류 발생")
        sys.exit(1)

def make_build(source_dir):
    """make를 실행하여 빌드합니다."""
    cpu_count = os.cpu_count() or 1
    make_cmd = f"make -j{cpu_count}"
    print(f"make 실행 중: {make_cmd}")
    result = os.system(make_cmd)
    if result != 0:
        print("make 실행 중 오류 발생")
        sys.exit(1)

def make_install(source_dir):
    """make install을 실행하여 설치합니다."""
    make_install_cmd = "make install"
    print(f"make install 실행 중: {make_install_cmd}")
    result = os.system(make_install_cmd)
    if result != 0:
        print("make install 실행 중 오류 발생")
        sys.exit(1)

def build(source_path, build_path, install_path, targets):

    def _build():
        # 소스 tarball 찾기
        tarball_pattern = os.path.join(source_path, "pkg-config-*.tar.gz")
        tarballs = glob.glob(tarball_pattern)

        if not tarballs:
            # tarball이 없으면 다운로드
            tarball_url = "https://pkgconfig.freedesktop.org/releases/pkg-config-0.29.2.tar.gz"
            tarball_name = os.path.join(source_path, "pkg-config-0.29.2.tar.gz")
            download_tarball(tarball_url, tarball_name)
            tarball = tarball_name
        else:
            tarball = tarballs[0]

        # 소스 추출
        extract_tarball(tarball, build_path)

        # 소스 디렉토리 찾기
        source_dirs = glob.glob(os.path.join(build_path, "pkg-config-*"))
        if not source_dirs:
            print("소스 디렉토리를 찾을 수 없습니다.")
            sys.exit(1)
        source_dir = source_dirs[0]

        # 구성 단계
        configure(source_dir, install_path)

        # 컴파일 단계
        make_build(source_dir)



    def _install():
        # 설치 단계
        make_install(source_dir)

    _build()
    _install()

if __name__ == '__main__':
    build(
        source_path=os.environ.get('REZ_BUILD_SOURCE_PATH', '.'),
        build_path=os.environ.get('REZ_BUILD_BUILD_PATH', './build'),
        install_path=os.environ.get('REZ_BUILD_INSTALL_PATH', './install')
        
    )