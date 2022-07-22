#!/usr/bin/python3
"""
Author Milis Konecna <milis.konecna@gmail.com>

PURPOSE
change wallpaper of my fedora desktop
learn python scripting

USAGE
python scratch_13.py --dir ~/Pictures/
see --help

setup in fedora:
crontab -e

# run it each 30 minutes
crontab -l
*/30 * * * * /home/miluska/test/wallpaperchanger.py

"""
from optparse import OptionParser
import platform
import datetime
import random
import subprocess
import glob


class Main:
    __parser = None
    options = None
    __params = None
    __json_data = None
    __list = []
    __a = None

    def __init__(self):
        self.nicePicture = None
        self.atLeastOnePicture = False
        self.PictureList = []
        self.__parser = OptionParser(usage="usage: %prog [options]",
                                     version="%prog 1.0")

        self.__parser.add_option("--dir",
                                 dest="dir",
                                 help="directory to eat",
                                 default="/home")

        (self.options, args) = self.__parser.parse_args()

    def checkDirectory(self):
        # create LIST from many file
        # LIST is only jpg
        # if directory is not accessible , write nice error
        try:
            # root_dir needs a trailing slash (i.e. /root/dir/)
            for File in glob.iglob(self.options.dir + '/**/*.jpg', recursive=True):
                self.PictureList.append(File)
        except Exception as e:
            print("Directory is not accessible;", e)
            exit()

    def selectPicture(self):
        try:
            self.nicePicture = random.choice(self.PictureList)
            print(self.nicePicture)
        except Exception as e:
            print("Not any image found;", e)
            exit()

    def setFedoraBackgroung(self):
        # run bash command, the right cmd for changing wallpaper should be:
        # gsettings set org.gnome.desktop.background picture-options 'center'
        # gsettings set org.gnome.desktop.background picture-uri "${URI}"

        # subprocess.run(["gsettings", "set", "org.gnome.desktop.background", "picture-options","'center'"])
        result = subprocess.run(["gsettings", "set", "org.gnome.desktop.background", "picture-uri", self.nicePicture])
        # print(result.returncode)
        if result.returncode == 0:
            print('Wallpaper is there')
        else:
            print('gsettings command failed')


# READ Main class
getter = Main()

try:
    print('python  version', platform.python_version())
    print(datetime.datetime.now())
    getter.checkDirectory()
    getter.selectPicture()
    getter.setFedoraBackgroung()

# be able to ctrl+c if it stacks
except KeyboardInterrupt:
    print('\nStopped by user')
