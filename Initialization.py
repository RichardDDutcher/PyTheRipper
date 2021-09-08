#imports
import subprocess as sp

sp.run(["python3", "-m", "pip", "install", "PySimpleGUI"])
sp.run(["sudo", "apt-get", "install", "python3-tk"])
sp.run(["git", "clone", "https://github.com/Phantom9298/PyTheRipper/main/Initialization.py"])
sp.run(["python3", "PyTheRipper.py"])
sp.run(["clear"])
