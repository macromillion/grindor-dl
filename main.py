import time
import os
import colored
from colored import fg, bg, attr
from os import system
import platform

# Color Configuration
error = fg('#FF0000')
good = fg('#00FF00')
warn = fg('#FFFF00')
res = attr('reset')

def clean():
    print(warn + '[WRN] Installation aborted...' + res)
    print('[INS] Cleaning installation...')
    os.chdir('.')

# Check for an installation of BepInEx
def checkBepinex(install):
    try:
        os.chdir(f'{install}\BepInEx')
    except OSError:
        print('[INS] Active BepInEx install located...')
        bepActive = True

# Preprint casting
checkDir = True
system("cls")
if platform.system() == 'Windows':
    print('[INS] Starting installation from Windows enviroment...' + good + 'OK' + res)
elif platform.system() == 'Linux':
    print('[INS] Starting installation from Linux enviroment...' + good + 'OK' + res)
elif platform.system() == 'Darwin':
    print(error + '[ERR] Cannot install on MacOS not supported...' + res)
    clean()

print('[INS] Checking working directory... ' + good + 'OK' + res)

try:
    os.chdir('C:\Program Files (x86)\Steam\steamapps\common\Valheim')
except OSError:
    print(warn + '[WRN] Directory could not be found automatically. Please paste your Valheim install directory!' + res)
    checkDir = False

if not checkDir:
    print('Install directory could not be found automatically, please paste your Valheim installation directory!')
    installDir = input()
    try:
        os.chdir(str(installDir))
    except OSError:
        print(error + '[ERR] Directory could still not be identified, please restart the installation process!' + res)
        clean()