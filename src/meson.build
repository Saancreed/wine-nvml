nvml_res_target = custom_target('nvml.res',
    output  : 'nvml.res',
    input   : 'nvml.rc',
    command : [wrc, target_arch, '-D__WINESRC__', '-o', '@OUTPUT@', '@INPUT@'],
    install : false)

nvml_def_target = custom_target('libnvml.def',
    output      : 'libnvml.def',
    input       : 'nvml.spec',
    command     : [winebuild, target_arch, '--def', '-o', '@OUTPUT@', '-E', '@INPUT@'],
    install     : true,
    install_dir : install_dir)

nvml_dll_target = custom_target('nvml.dll',
    output      : 'nvml.dll',
    input       : [nvml_def_target, nvml_res_target],
    command     : [winebuild, target_arch, '--dll', '--fake-module', '-o', '@OUTPUT@', '-E', '@INPUT@'],
    install     : true,
    install_dir : install_dir / 'fakedlls')

nvml_dll = shared_library('nvml.dll', ['nvml.c'],
    name_prefix  : '',
    dependencies : [lib_dl],
    link_depends : [nvml_def_target],
    link_args    : [meson.current_build_dir() / 'libnvml.def'],
    install      : true,
    install_dir  : install_dir)