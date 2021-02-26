project('wine-nvml', ['c'], version: '461.09', license: 'LGPL-2.1-or-later')

lib_dl = meson.get_compiler('c').find_library('dl')

winebuild = find_program('winebuild')
wrc       = find_program('wrc')

target_arch = target_machine.cpu_family() == 'x86_64' ? '-m64' : '-m32'

install_dir = get_option('libdir') / 'wine'

subdir('src')
