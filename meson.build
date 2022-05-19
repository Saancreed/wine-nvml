project('wine-nvml', ['c'], license: 'LGPL-2.1-or-later')

is_windows      = target_machine.system() == 'windows'
arch_dir_prefix = target_machine.cpu_family() == 'x86_64' ? 'x86_64' : 'i386'
os_dir_suffix   = is_windows ? 'windows' : 'unix'
install_dir     = get_option('libdir') / 'wine' / arch_dir_prefix + '-' + os_dir_suffix

winebuild = find_program('winebuild')
wrc       = find_program('wrc')

if not is_windows
    lib_dl = meson.get_compiler('c').find_library('dl')
endif

subdir('src')
