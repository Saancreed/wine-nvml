#!/usr/bin/env bash

set -e

srcdir="$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")"

(cd "${srcdir}/src" && ./make_nvml)

BITS="${BITS:-64}"

meson setup \
    --cross-file "${srcdir}/cross-mingw${BITS}.txt" \
    --prefix /usr \
    --libdir "lib${BITS}" \
    --buildtype release \
    --strip \
    "./build-mingw${BITS}" "${srcdir}"

ninja -C "./build-mingw${BITS}"

meson setup \
    --cross-file "${srcdir}/cross-wine${BITS}.txt" \
    --prefix /usr \
    --libdir "lib${BITS}" \
    --buildtype release \
    --strip \
    "./build-wine${BITS}" "${srcdir}"

ninja -C "./build-wine${BITS}"

if [[ "${1:-}" == --install ]]
then
    ninja -C "./build-mingw${BITS}" install
    ninja -C "./build-wine${BITS}" install
fi
