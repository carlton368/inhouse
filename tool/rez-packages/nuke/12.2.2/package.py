name = "nuke"
version = "12.2.2"
description = "Rez package for Nuke version 12.2.2"
authors = ["foundry"]
requires = ["python-2.7.5"]  # 추가 의존성이 있다면 여기에 추가

build_command = False  # 이미 설치된 Nuke를 사용하므로 빌드 명령은 필요 없습니다.

def commands():
    import os

    print("Nuke 12.2.2를 기본 nuke로 설정합니다.")

    # Nuke 설치 경로를 설정합니다.
    nuke_root = "/usr/local/Nuke12.2v2"  # 실제 Nuke 설치 경로.

    if not os.path.exists(nuke_root):
        print(f"Warning: Nuke root directory {nuke_root} does not exist.")

    # LD_LIBRARY_PATH에 Nuke의 라이브러리 경로를 추가.
    lib_path = os.path.join(nuke_root, 'lib')
    if os.path.exists(lib_path):
        env.LD_LIBRARY_PATH.prepend(lib_path)
    else:
        print(f"Warning: Library path {lib_path} does not exist.")

    # NUKE_PATH에 플러그인 경로를 추가합니다.
    plugins_path = os.path.join(nuke_root, 'plugins')
    if os.path.exists(plugins_path):
        env.NUKE_PATH.append(plugins_path)
    else:
        print(f"Warning: Plugins path {plugins_path} does not exist.")

    # PYTHONPATH에 Nuke의 파이썬 모듈 경로를 추가합니다.
    python_path = os.path.join(nuke_root, 'python')
    if os.path.exists(python_path):
        env.PYTHONPATH.prepend(python_path)
    else:
        print(f"Warning: Python path {python_path} does not exist.")

    # Nuke 실행 파일의 절대 경로를 설정하고 alias로 등록합니다.
    nuke_executable = os.path.join(nuke_root, 'Nuke12.2')
    if not os.path.exists(nuke_executable):
        print(f"Warning: Nuke executable {nuke_executable} does not exist.")
    else:
        # alias() 함수를 사용하여 별칭을 설정합니다.
        alias("nuke", nuke_executable)
        alias("nukex", f"{nuke_executable} -x")
        print(f"nuke executable set to: {nuke_executable}")
        print(f"nukex executable set to: {nuke_executable} -x")

    # 추가적인 환경 변수 설정 (필요 시)
    # 예: env.NUKE_USER_HOME = os.path.expanduser("~/.nuke")
