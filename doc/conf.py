# Environment variables, including running path of garffield, mpich, etc, and library of garffield.
env = {
    'PATH': '/tmp/garffield/mpich/bin:/tmp/garffield/bin:/tmp/garffield/mpich/bin:/tmp/garffield/bin:/home/charlesxu/anaconda3/bin:/home/charlesxu/.userscripts:/home/charlesxu/.fzf/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games', 
    'LD_LIBRARY_PATH': '/opt/intel/compilers_and_libraries_2017.2.174/linux/compiler/lib/intel64_lin_mic/:/opt/intel/compilers_and_libraries_2017.2.174/linux/compiler/lib/intel64_lin:/tmp/garffield/lib:/tmp/garffield/fftw/lib:/tmp/garffield/mpich/lib:/opt/intel/compilers_and_libraries_2017.2.174/linux/compiler/lib/intel64_lin_mic/:/opt/intel/compilers_and_libraries_2017.2.174/linux/compiler/lib/intel64_lin:/tmp/garffield/lib:/tmp/garffield/fftw/lib:/tmp/garffield/mpich/lib'}

files_input = {
        'geo': '/home/charlesxu/Workspace/softs/GARFfield/test/reax/Cl2/unweighted/MPE/geo.new',
        'ffield': '/home/charlesxu/Workspace/softs/GARFfield/test/reax/Cl2/unweighted/MPE/ffield',
        'trainset.in': '/home/charlesxu/Workspace/softs/GARFfield/test/reax/Cl2/unweighted/MPE/trainset.in.new',
        'params': '/home/charlesxu/Workspace/softs/GARFfield/test/reax/Cl2/unweighted/MPE/params'
        }

files_output = {
        'log': '~/.cache/drlff.log'
        }
