import os
import shutil

NAS_VAR = "TRUENAS"
MUSIC_VAR = "Music"
MOVIES_VAR = "Movies"
APP_VAR = "Applications"
DATA_VAR = "Data"
TMP_VAR = "tmp"
PIC_VAR = "Pictures"
DIR_ARRAY = {MUSIC_VAR,MOVIES_VAR,APP_VAR,DATA_VAR,TMP_VAR,PIC_VAR}
DIR_ARRAY_TEST = {MUSIC_VAR}
BACKUP_DIR = "DIR"

class FileBackup:
    def main(self):
        #win 
        for directoryToCheck in DIR_ARRAY:
            filesAndDir = self.getListFilesAndDir(os.path.sep + os.path.sep + NAS_VAR + os.path.sep + os.path.sep + directoryToCheck)
            diffToCopy = self.compareOriginalWithBackUp(filesAndDir[0], directoryToCheck)
            self.copyFiles(diffToCopy,filesAndDir[2])
            self.getDirectories(filesAndDir[1])

    def compareOriginalWithBackUp(self, arrayFiles, dirToBackUp):
        filesAndDirBack = self.getListFilesAndDir(os.path.sep + BACKUP_DIR + os.path.sep + dirToBackUp)
        diff = list(set(arrayFiles) - set(filesAndDirBack))
        return diff

    def copyFiles(self, filesToCopy, dirToBack):
        try:
            for activeFile in filesToCopy:
                shutil.copy2(activeFile,dirToBack)
            return True
        finally:
            return False

# Obtiene una lista de Archivos y directorios 
    def getListFilesAndDir(self, path):
        files = []
        directory = []
        dirP = []
        for (dirpath, dirnames, filenames) in os.walk(path):
            files.extend(filenames)
            directory.extend(dirnames)
            dirP.extend(dirpath)
            break
        return files, directory, dirP
