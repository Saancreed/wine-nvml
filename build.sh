#!/usr/bin/env bash

set -e

if [ -z "$1" ]; then
  echo "Usage: build.sh destdir"
  exit 1
fi

NVML_SRC_DIR=`dirname $(readlink -f $0)`
NVML_BUILD_DIR=$(realpath "$1")"/wine-nvml"

if [ -e "$NVML_BUILD_DIR" ]; then
  echo "Build directory $NVML_BUILD_DIR already exists"
  exit 1
fi

git submodule update --init

function build_arch {
  export WINEARCH="win$1"

  cd "$NVML_SRC_DIR"

  meson --cross-file "$NVML_SRC_DIR/build-wine$1.txt"  \
        --buildtype "release"                         \
        --prefix "$NVML_BUILD_DIR/install.$1"         \
        --libdir="lib$1"                                \
        "$NVML_BUILD_DIR/build.$1"

  cd "$NVML_BUILD_DIR/build.$1"
  ninja install

  if ! [ -e "$NVML_BUILD_DIR/lib" ]; then
    mkdir -p "$NVML_BUILD_DIR/lib/wine"
  fi

  cp -r "$NVML_BUILD_DIR/install.$1/lib$1/wine" "$NVML_BUILD_DIR/lib"
  rm -R "$NVML_BUILD_DIR/build.$1"
  rm -R "$NVML_BUILD_DIR/install.$1"
}

build_arch 64
build_arch 32
