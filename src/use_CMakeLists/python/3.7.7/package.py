name = "python"
version = "3.7.7"
authors = ["wonjin LEE"]
description = "Python programming language"

tools = [
    "python",
    "python3",
    "pip",
    "pip3"
]

# Runtime dependencies
requires = [
    "platform-linux",
    "arch-x86_64"
]

# Build-time dependencies
build_requires = [
    "cmake-3.10+",
    "make",
    "gcc"
]

variants = [
    ["platform-linux", "arch-x86_64"]
]

def commands():
    env.PATH.prepend("{root}/bin")
    env.PYTHONPATH.prepend("{root}/lib/python3.7/site-packages")
    env.LD_LIBRARY_PATH.prepend("{root}/lib")
    
    import os
    python_bin_dir = os.path.join(str(env.REZ_PYTHON_ROOT), "bin")
    python_executable = os.path.join(python_bin_dir, "python3.7")
    python_symlink = os.path.join(python_bin_dir, "python")
    
    if os.path.exists(python_executable) and not os.path.exists(python_symlink):
        os.symlink(python_executable, python_symlink)
        print(f"Created symlink: {python_symlink} -> {python_executable}")
    elif not os.path.exists(python_executable):
        print(f"Error: {python_executable} does not exist.")
    else:
        print(f"Symlink {python_symlink} already exists.")

build_command = "cmake -DCMAKE_INSTALL_PREFIX={install_path} {root} && cmake --build . --target install_python"

def pre_build_commands():
    env.REZ_BUILD_CONFIG = "Release"