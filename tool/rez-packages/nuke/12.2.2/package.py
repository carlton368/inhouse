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

    # PATH 환경 변수에 Nuke의 실행 파일 경로를 추가합니다.
    env.PATH.prepend(nuke_root)

    # LD_LIBRARY_PATH에 Nuke의 라이브러리 경로를 추가합니다.
    env.LD_LIBRARY_PATH.prepend(os.path.join(nuke_root, 'lib'))

    # NUKE_PATH에 플러그인 경로를 추가합니다.
    env.NUKE_PATH.append(os.path.join(nuke_root, 'plugins'))

    # PYTHONPATH에 Nuke의 파이썬 모듈 경로를 추가합니다.
    env.PYTHONPATH.prepend(os.path.join(nuke_root, 'python'))

    # Executable 설정
    env.NUKE_EXECUTABLE = os.path.join(nuke_root, 'Nuke12.2')
    env.aliases['nuke'] = env.NUKE_EXECUTABLE
    print(f"NUKE_EXECUTABLE: {env.NUKE_EXECUTABLE}")