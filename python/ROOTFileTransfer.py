import os, sys

def GetCRABOutputDir(crabDirName, SEPath='/pnfs/knu.ac.kr/data/cms/store/user/kplee'):
    thePath = ""
    for (path, dirName, list_file) in os.walk(SEPath):
        if crabDirName == dirName:
            thePath = "%s/%s" % (path, dirName)
            break

    if thePath == "":
        print "[GetCRABOutputDir] No crab directory is found for %s" % crabDirName
        sys.exit()

    if len(os.listdir(thePath)) > 1:
        print "[GetCRABOutputDir] Find more than 1 sub-directories under the crab directory"
        print "  crabDir = %s" % crabDir
        print "  listDir = ", os.listdir(thePath)
        sys.exit()

    return thePath 


class TransferTool:
    def __init__(self):
        self.dic_input_to_outputPath = {}

        self.user = "" # -- e.g. kplee
        self.host = "" # -- e.g. lxplus.cern.ch
        self.port = 22
        
        self.do_hadd = False
        self.needPassward = False

        # -- internal variables
        self.list_outputFile = []


    def Transfer(self):
        for inputPath in dic_input_to_outputPath.keys():
            outputPath = dic_input_to_outputPath[inputPath]
            self.Transfer_Input_to_Output(inputPath, outputPath)


    def Transfer_Input_to_Output(self, inputPath, outputPath):
        list_outputFile = self.GetListOfOutputFiles(inputPath)
        print list_outputFile


    # -- search .root file under the drectory (including sub-directories)
    def GetListOfOutputFiles(self, inputPath):
        list_outputFile = []
        for (path, dirName, list_file) in os.walk(inputPath):
            for fileName in list_file:
                if ".root" == os.path.splittext(fileName) and "failed" not in path2:
                    list_outputFile.append( "%s/%s" % (path, fileName) )

        return list_outputFile







