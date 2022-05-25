#!/usr/bin/env bash

set -e

srcdir="$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")"

(cd "${srcdir}/src" && ./make_nvml)

meson setup \
    --cross-file "${srcdir}"/cross-mingw64.txt \
    --prefix /usr \
    --libdir lib64 \
    --buildtype release \
    --strip \
    ./build-mingw64 "${srcdir}"

ninja -C ./build-mingw64

meson setup \
    --cross-file "${srcdir}"/cross-wine64.txt \
    --prefix /usr \
    --libdir lib64 \
    --buildtype release \
    --strip \
    ./build-wine64 "${srcdir}"

ninja -C ./build-wine64

meson setup \
    --cross-file "${srcdir}"/cross-mingw32.txt \
    --prefix /usr \
    --libdir lib32 \
    --buildtype release \
    --strip \
    ./build-mingw32 "${srcdir}"

ninja -C ./build-mingw32

meson setup \
    --cross-file "${srcdir}"/cross-wine32.txt \
    --prefix /usr \
    --libdir lib32 \
    --buildtype release \
    --strip \
    ./build-wine32 "${srcdir}"

ninja -C ./build-wine32

if [[ "${1:-}" == --install ]]
then
    ninja -C ./build-mingw32 install
    ninja -C ./build-wine32 install
    ninja -C ./build-mingw64 install
    ninja -C ./build-wine64 install
fi