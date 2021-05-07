# `wine-nvml`

## NVIDIA Management Library wrapper for Wine

`wine-nvml` allows applications running under Wine to call some NVML functions as if native Windows driver was installed into the prefix for purposes like monitoring GPU temperature, utilization, etc. Obviously, for this to work, the host system should have `libnvidia-ml.so` installed (it comes with the NVIDIA driver) and findable by the dynamic linker.

## Building

`wine-nvml` can be built with the Meson build system. You'll need `gcc`, `meson`, `ninja` and `wine` (more specifically: `winebuild`, `winegcc` and `wrc` programs available in your `$PATH`) to do so.

1. Update submodules (`git submodule update --init`) to acquire `nvml.h` from `nvidia-settings` repo and some Winelib headers from `wine` repo.
2. Call `meson setup` to generate build tree. Use `build-wine{64,32}.txt` cross files to build 64–bit and 32–bit wrappers respectively.
3. Call `ninja` to build the project.

Please refer to `build.sh` helper script for automated (but simplified and not very flexible) building procedure.

## Installing

In order for Wine to find and make use of `wine-nvml`, built wrapper libraries must be placed into specific locations. Two installation modes are expected to work:

### Local installation (affects only a single Wine prefix)

It is possible to install `wine-nvml` directly into a Wine prefix by renaming generated `nvml.dll.so` to `nvml.dll` and placing it in the `drive_c/windows/{system32,syswow64}` directories of your prefix for 64–bit and 32–bit libraries respectively (assuming a 64–bit Wine prefix).

### Global installation (usable in all prefixes managed by Wine)

Generated files can also be installed alongside other fakedlls of your Wine installation. For example, on Arch Linux using the `wine` package it would be:

```sh
/usr/lib/wine/x86_64-unix/libnvml.def
/usr/lib/wine/x86_64-unix/nvml.dll.so
/usr/lib/wine/x86_64-windows/nvml.dll
/usr/lib32/wine/i386-unix/libnvml.def
/usr/lib32/wine/i386-unix/nvml.dll.so
/usr/lib32/wine/i386-windows/nvml.dll
```

Calling `DESTDIR=. ./build.sh --install` will create such file tree in the current directory.

You can use `ninja install` to copy these files into appropriate locations, provided that `--prefix` and `--libdir` options of `meson setup` were used to set correct paths for your Wine installation.

## Usage

An example application by NVIDIA and a `Makefile` to build it for Wine can be found in `example/` directory. It can be used to test if the wrapper is working correctly. In order to build it, you need to either install `wine-nvml` globally or add path to `nvml.dll.so` to `LDFLAGS` like so: `LDFLAGS='-L/path/to/wine-nvml' make`. Please note that call to `nvmlDeviceSetComputeMode` is expected to fail because Wine cannot run as `root`.

## Potential issues

On Windows, `nvml.dll` can reside in `%ProgramW6432%/NVIDIA Corporation/NVSMI`, in `%SystemRoot%/System32`, or in some other directory. Because of this, it's possible that some applications may attempt to use NVML by means other than `LoadLibrary("nvml.dll")` or linking against it with `-lnvml`. Such attempts will most likely fail unless additional workarounds are applied.

## Licensing

This project is released on the terms of LGPL-2.1-or-later. However, this license _does not apply to all files in this repository_:

* `nvidia-settings` submodule is GPL-2.0, however the only file we use from that repo is `nvml.h`…
  * `nvml.h` is custom, see NVIDIA license below
* `example/example.c` is also custom NVIDIA license

## NVIDIA License

```
 Copyright 1993-2020 NVIDIA Corporation.  All rights reserved.

 NOTICE TO USER:

 This source code is subject to NVIDIA ownership rights under U.S. and
 international Copyright laws.  Users and possessors of this source code
 are hereby granted a nonexclusive, royalty-free license to use this code
 in individual and commercial software.

 NVIDIA MAKES NO REPRESENTATION ABOUT THE SUITABILITY OF THIS SOURCE
 CODE FOR ANY PURPOSE.  IT IS PROVIDED "AS IS" WITHOUT EXPRESS OR
 IMPLIED WARRANTY OF ANY KIND.  NVIDIA DISCLAIMS ALL WARRANTIES WITH
 REGARD TO THIS SOURCE CODE, INCLUDING ALL IMPLIED WARRANTIES OF
 MERCHANTABILITY, NONINFRINGEMENT, AND FITNESS FOR A PARTICULAR PURPOSE.
 IN NO EVENT SHALL NVIDIA BE LIABLE FOR ANY SPECIAL, INDIRECT, INCIDENTAL,
 OR CONSEQUENTIAL DAMAGES, OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS
 OF USE, DATA OR PROFITS,  WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE
 OR OTHER TORTIOUS ACTION,  ARISING OUT OF OR IN CONNECTION WITH THE USE
 OR PERFORMANCE OF THIS SOURCE CODE.

 U.S. Government End Users.   This source code is a "commercial item" as
 that term is defined at  48 C.F.R. 2.101 (OCT 1995), consisting  of
 "commercial computer  software"  and "commercial computer software
 documentation" as such terms are  used in 48 C.F.R. 12.212 (SEPT 1995)
 and is provided to the U.S. Government only as a commercial end item.
 Consistent with 48 C.F.R.12.212 and 48 C.F.R. 227.7202-1 through
 227.7202-4 (JUNE 1995), all U.S. Government End Users acquire the
 source code with only those rights set forth herein.

 Any use of this source code in individual and commercial software must
 include, in the user documentation and internal comments to the code,
 the above Disclaimer and U.S. Government End Users Notice.
```
