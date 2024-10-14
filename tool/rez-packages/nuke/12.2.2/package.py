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

    # env.prefix가 문자열인지 확인하고, 그렇지 않다면 문자열로 변환합니다.
    if not isinstance(env.prefix, str):
        bin_dir = os.path.join(str(env.prefix), 'bin')
    else:
        bin_dir = os.path.join(env.prefix, 'bin')

    print(f"env.prefix: {env.prefix} (Type: {type(env.prefix)})")
    print(f"bin_dir: {bin_dir} (Type: {type(bin_dir)})")

    # LD_LIBRARY_PATH에 Nuke의 라이브러리 경로를 추가합니다.
    env.LD_LIBRARY_PATH.prepend(os.path.join(nuke_root, 'lib'))

    # NUKE_PATH에 플러그인 경로를 추가합니다.
    env.NUKE_PATH.append(os.path.join(nuke_root, 'plugins'))

    # PYTHONPATH에 Nuke의 파이썬 모듈 경로를 추가합니다.
    env.PYTHONPATH.prepend(os.path.join(nuke_root, 'python'))

    # Rez 패키지 내에 bin 디렉토리를 생성합니다.
    if not os.path.exists(bin_dir):
        os.makedirs(bin_dir)

    # Nuke 실행 파일을 호출하는 래퍼 스크립트를 생성합니다.
    wrapper_script = os.path.join(bin_dir, 'nuke')
    if not os.path.exists(wrapper_script):
        with open(wrapper_script, 'w') as f:
            f.write(f"""#!/bin/bash
{nuke_root}/Nuke12.2 "$@"
""")
        os.chmod(wrapper_script, 0o755)

    # 새로 생성한 bin 디렉토리를 PATH의 최상단에 추가합니다.
    env.PATH.prepend(bin_dir)

    # 추가적인 환경 변수 설정 (필요 시)
    # 예: env.NUKE_USER_HOME = os.path.expanduser("~/.nuke")
    
    print(f"env.prefix: {env.prefix} (Type: {type(env.prefix)})")
    print(f"nuke_root: {nuke_root} (Type: {type(nuke_root)})")
    print(f"bin_dir: {bin_dir} (Type: {type(bin_dir)})")
