import os
import re
import shutil

class FileBackup:

    def main(self):
        return False
    
    def startBackup(self, fromD, toD):
        if self.isNotBlank(fromD) and self.isNotBlank(toD):
            if os.path.exist(fromD):
                if not os.path.exist(toD):
                    path = shutil.copytree(fromD, toD, True)
                    return self.isNotBlank(path)
                else:
                    #
        return False

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
    
    def isBlank (self, myString):
        return not (myString and myString.strip())
    
    def isNotBlank (self, myString):
        return bool(myString and myString.strip())
