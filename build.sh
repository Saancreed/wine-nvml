#!/usr/bin/env bash

set -e

cd "$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")"

git submodule update --init

meson setup \
    --prefix /usr \
    --libdir lib \
    --buildtype release \
    --cross-file build-wine64.txt \
    build64 .

ninja -C build64

meson setup \
    --prefix /usr \
    --libdir lib32 \
    --buildtype release \
    --cross-file build-wine32.txt \
    build32 .

ninja -C build32

if [[ "${1}" == --install ]]
then
    ninja -C build64 install
    ninja -C build32 install
fi