name = "libx264"
version = "0.148"

requires = [
    "gcc-4.8+",
    "yasm-1+",
    "nasm-2.13+"
]

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")
    env.PATH.prepend("{root}/bin")

build_command = "python3 {root}/build.py {install_path}"