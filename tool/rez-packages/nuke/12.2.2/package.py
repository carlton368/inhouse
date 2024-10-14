name = "nuke"
version = "12.2.2"
description = "Rez package for Nuke version 12.2.2"
authors = ["foundary"]
# Python 의존성 제거
# requires = ["python-2.7.5"]

build_command = False  # 빌드 명령 필요 없음

def commands():
    import os

    print("Nuke 12.2.2 환경을 설정 중입니다.")

    nuke_root = "/usr/local/Nuke12.2v2"  # 실제 Nuke 설치 경로로 업데이트

    # PYTHONPATH를 재설정하여 충돌 방지
    env.PYTHONPATH = ""

    # Nuke의 라이브러리 경로 설정
    lib_path = os.path.join(nuke_root, 'lib')
    env.LD_LIBRARY_PATH.prepend(lib_path)

    # Nuke의 플러그인 경로 설정
    plugins_path = os.path.join(nuke_root, 'plugins')
    env.NUKE_PATH.append(plugins_path)

    # Nuke의 Python 경로 추가
    python_extensions_path = os.path.join(nuke_root, 'pythonextensions', 'site-packages')
    python_lib_path = os.path.join(nuke_root, 'lib', 'python2.7', 'site-packages')

    env.PYTHONPATH.prepend(python_extensions_path)
    env.PYTHONPATH.prepend(python_lib_path)

    # Nuke 실행 파일의 별칭 설정
    nuke_executable = os.path.join(nuke_root, 'Nuke12.2')
    alias("nuke", nuke_executable)
    alias("nukex", f"{nuke_executable} -x")

    print(f"nuke 실행 파일 경로: {nuke_executable}")
    print(f"nukex 실행 파일 경로: {nuke_executable} -x")
