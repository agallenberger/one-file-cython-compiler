## =================================================================================================
## Python 3.6+
## =================================================================================================
import distutils.core
import os
import platform

import Cython.Distutils
import numpy as np
from colorama import Fore, Style

## =================================================================================================
MODULE_NAMES   = ['Example']                    # List of modules to compile
MODULE_SOURCES = [['example_cython.pyx']]       # List of sources for each module
COMPILE_ARGS   = []                             # Compiler arguments
LINK_ARGS      = []                             # Linker arguments
FORCE_COMPILE  = True                           # Force project recompile

## =================================================================================================
def main():
    script_args = ['build_ext', '--inplace']
    if FORCE_COMPILE == True:
        script_args.append('--force')

    ## Call this script again, but this time __name__ will be 'builtins' instead of '__main__'.
    dist = distutils.core.run_setup(
        script_name=os.path.basename(__file__),
        script_args=script_args,
    )
    if dist.have_run['build_ext'] == 0:
        print(f'{Fore.RED}Error: Unable to build Cython modules{Style.RESET_ALL}')
    else:
        print(f'{Fore.GREEN}Success!{Style.RESET_ALL}')


## -------------------------------------------------------------------------------------------------
def cy_compile():
    if platform.system() == 'Windows':
        arg_prefix = '/'
    else:
        arg_prefix = '-f'

    compile_args = [f'{arg_prefix}{arg}' for arg in COMPILE_ARGS]
    link_args = [f'{arg_prefix}{arg}' for arg in LINK_ARGS]

    ## Add files to be compiled
    ext_modules = []
    for module_name, module_sources in zip(MODULE_NAMES, MODULE_SOURCES):
        ext_modules.append(
            Cython.Distutils.Extension(
                name=module_name,
                sources=module_sources,
                cython_directives={'language_level': '3'},
                extra_compile_args=compile_args,
                extra_link_args=link_args,
            )
        )

    ## Compile
    distutils.core.setup(
        cmdclass={'build_ext': Cython.Distutils.build_ext},
        ext_modules=ext_modules,
        include_dirs=[np.get_include()],
    )


## =================================================================================================
if __name__ == '__main__':
    main()
elif __name__ == 'builtins':
    cy_compile()

