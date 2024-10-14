name = "nuke"
version = "12.2.2"
description = "Rez package for Nuke version 12.2.2"
authors = ["foundary"]
requires = ["python-2.7.5"]  # 추가 의존성이 있다면 여기에 추가

build_command = False  # 이미 설치된 Nuke를 사용하므로 빌드 명령은 필요 없습니다.

def commands():
    import os

    print("Nuke 12.2.2를 기본 nuke로 설정합니다.")

    # Nuke 설치 경로를 설정합니다.
    nuke_root = "/usr/local/Nuke12.2v2"  # 실제 Nuke 설치 경로로 변경하세요.

    if not os.path.exists(nuke_root):
        print(f"Warning: Nuke root directory {nuke_root} does not exist.")

    # LD_LIBRARY_PATH에 Nuke의 라이브러리 경로를 추가합니다.
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
        # Rez 3.x에서는 env.aliases를 사용하여 alias를 설정할 수 있습니다.
        env.aliases['nuke'] = nuke_executable
        print(f"nuke executable set to: {nuke_executable}")

    # 래퍼 스크립트를 생성하지 않고 직접 alias를 설정함으로써 문제를 해결합니다.
    # build_command = False이므로, bin 디렉토리를 생성하지 않습니다.
