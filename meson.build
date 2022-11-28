project('wine-nvml', ['c'], license: 'LGPL-2.1-or-later')

is_windows      = target_machine.system() == 'windows'
arch_dir_prefix = target_machine.cpu_family() == 'x86_64' ? 'x86_64' : 'i386'
os_dir_suffix   = is_windows ? 'windows' : 'unix'
install_dir     = get_option('libdir') / 'wine' / arch_dir_prefix + '-' + os_dir_suffix

cc = meson.get_compiler('c')

has_reasonable_format_warnings = cc.get_supported_arguments('-Wformat', '-Werror').length() < 2 or cc.compiles(
    '''
    #include <stdio.h>

    int main()
    {
        printf("%lli\n", (long long)0);
    }
    ''',
    args: ['-Wformat', '-Werror'],
    name: 'reasonable format warnings')

if not has_reasonable_format_warnings
    add_project_arguments(cc.get_supported_arguments('-Wno-format'), language: ['c'])
endif

if not is_windows
    lib_dl = cc.find_library('dl')
endif

winebuild = find_program('winebuild')
wrc       = find_program('wrc')

subdir('src')
