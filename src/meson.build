include_dirs = include_directories('.')

if is_windows
    nvml_res = custom_target(
        'nvml.res',
        output: 'nvml.res',
        input: 'nvml.rc',
        command: [wrc, '-o', '@OUTPUT@', '@INPUT@'],
        install: false,
    )

    shared_library(
        'nvml',
        ['nvml.c', nvml_res],
        name_prefix: '',
        include_directories: include_dirs,
        link_depends: ['nvml.spec'],
        link_args: ['-Wl,--wine-builtin', meson.current_source_dir() / 'nvml.spec'],
        install: true,
        install_dir: install_dir,
    )
else
    shared_library(
        'nvml',
        ['nvml_unixlib.c'],
        name_prefix: '',
        include_directories: include_dirs,
        dependencies: [lib_dl],
        install: true,
        install_dir: install_dir,
    )
endif
