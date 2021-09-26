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
                    resultFromD = self.getListFilesAndDir(fromD)
                    resultToD = self.getListFilesAndDir(toD)
                    #for all files inside check for the ones that are not in the toD
                    #for all of those that exist check the metadata for creation date if fromD is > toD replace
                    #do it recursible for all paths
                    return self.recursiveCopy(resultFromD,resultToD)
        return False
    
    def recursiveCopy(self, fromD, toD):
        if fromD[2]:
             path = shutil.copytree(fromD[2],toD[0])
        if fromD[1]:
            for dirActive in fromD[1]:
                newFromD = self.getListFilesAndDir(fromD[0]+os.path.sep+dirActive)
                self.startBackup(newFromD,)
        return False
    
    def compareNCpy(self,resultFromD,resultToD):
        filesOnDirToCpy = list(set(resultFromD[0]) - set(resultToD[0]))
        self.copyFiles(filesOnDirToCpy,resultToD[3])
        for dirAct in resultFromD[1]:
            newFromD = self.getListFilesAndDir(dirAct)
            self.copyFiles(newFromD[1],resultToD[3] + os.path.sep + dirAct)
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
