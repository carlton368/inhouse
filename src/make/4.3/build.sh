#!/bin/bash
set -e

INSTALL_PATH=$1
VERSION="4.3"
MAKE_URL="https://ftp.gnu.org/gnu/make/make-${VERSION}.tar.gz"

# Download
curl -L "${MAKE_URL}" -o make-${VERSION}.tar.gz

# Extract
tar -xzf make-${VERSION}.tar.gz
cd make-${VERSION}

# Configure
./configure --prefix=${INSTALL_PATH}

# Build
make -j$(nproc)

# Install
make install

# Clean up
cd ..
# rm -rf make-${VERSION} make-${VERSION}.tar.gz

echo "make ${VERSION} is installed"