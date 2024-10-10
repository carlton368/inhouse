name = "env_settings"
version = "1.0.0"
authors = ["Your Company Name"]
description = "Rez 환경 설정을 중앙에서 관리하기 위한 패키지"

def commands():
    import os

    # 환경 변수 설정
    env.REZ_BUILD_ARCH = os.getenv("REZ_BUILD_ARCH", "x86_64")
    env.REZ_BUILD_PLATFORM = os.getenv("REZ_BUILD_PLATFORM", "linux")
    env.REZ_BUILD_OS = os.getenv("REZ_BUILD_OS", "centos-7")
    env.REZ_PACKAGES_PATH = os.getenv("REZ_PACKAGES_PATH", "/home/t003/westworld/inhouse/tool/rez-packages")
    env.REZ_BUILD_INSTALL_PATH = os.getenv("REZ_BUILD_INSTALL_PATH", "/home/t003/westworld/inhouse/tool/rez-packages")
  
    # Bash 자동 완성 스크립트 설정 (옵션)
    completion_script = "/home/t003/westworld/rez/completion/complete.sh"
    if os.path.isfile(completion_script):
        env.REZ_BASH_COMPLETION_SCRIPT = completion_script
