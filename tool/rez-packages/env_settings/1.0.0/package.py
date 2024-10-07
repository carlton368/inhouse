# /home/t003/westworld/inhouse/tool/rez-packages/env_settings/1.0.0/package.py

name = "env_settings"
version = "1.0.0"

def commands():
    import os
    # 환경 변수 설정
    env.REZ_BUILD_ARCH = "aarch64"
    env.REZ_BUILD_PLATFORM = "linux"
    env.REZ_BUILD_OS = "centos-7"
    env.REZ_PACKAGES_PATH = "/home/t003/westworld/inhouse/tool/rez-packages"
    env.REZ_BUILD_INSTALL_PATH = "/home/t003/westworld/inhouse/tool/rez-packages"
    env.PYTHONPATH.prepend("/home/t003/westworld/rez/lib/python3.7/site-packages")

    # Bash 완성 스크립트 설정 (옵션)
    completion_script = "/home/t003/westworld/rez/completion/complete.sh"
    if os.path.isfile(completion_script):
        env.REZ_BASH_COMPLETION_SCRIPT = completion_script

