project('wine-nvml', ['c'], license: 'LGPL-2.1-or-later')

is_windows = target_machine.system() == 'windows'
arch_dir_prefix = target_machine.cpu_family() == 'x86_64' ? 'x86_64' : 'i386'
os_dir_suffix = is_windows ? 'windows' : 'unix'
install_dir = get_option('libdir') / 'wine' / arch_dir_prefix + '-' + os_dir_suffix

cc = meson.get_compiler('c')

if not is_windows
    lib_dl = cc.find_library('dl')
endif

wrc = find_program('wrc')

subdir('src')
