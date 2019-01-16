from cx_Freeze import setup, Executable

base = None    

executables = [Executable("monitor.py", base=base)]

packages = ["psutil"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "dnf-monitor",
    options = options,
    version = "1.0",
    description = '',
    executables = executables
)