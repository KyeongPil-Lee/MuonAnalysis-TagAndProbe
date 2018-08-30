import os, sys

class TransferToEOSTool:
    def __init__(self):

        self.scriptName = ""

        self.SEPath = "" # -- SE = storage element
        self.xrdProtocol = "root://eoscms.cern.ch"

        # -- individual settings for each tree
        self.crabDir = ""
        self.treeName = ""
        self.eosPath = ""

        # -- internal variable
        self.haddCMDs = []
        self.xrdcpCMDs = []

    def Register(self):
        self._PrintVar()
        self._CheckVar()

        self._MakeHaddCMD()
        self._MakeXrdcpCMD()

    def GenScript(self):

        if self.scriptName in os.listdir("."):
            print "%s already exists in same directory ... please change the name" % self.scriptName
            sys.exit()

        f = open(self.scriptName, "w")

        f.write("#!bin/bash\n\n")

        for iTree in range(0, len(self.haddCMDs)):
            haddCMD = self.haddCMDs[iTree]
            xrdcpCMD = self.xrdcpCMDs[iTree]

            f.write( haddCMD  + "\n" )
            f.write( xrdcpCMD + "\n\n\n" )

        f.write( 'echo "All jobs are finished"\n')

        f.close()

        os.system( "cat %s" % self.scriptName )

        print "*" * 100
        print "*" * 100
        print "script is generated: %s" % self.scriptName
        print "source %s >&%s.log&" % (self.scriptName, self.scriptName.split('.sh')[0])
        print "Check list before running script"
        print "1) ROOT: available? (for hadd)"
        print "2) VOCMS certificate: valid?"
        print "3) All necessary EOS directories are available?"
        print "*" * 100
        print "*" * 100

    def _MakeHaddCMD(self):
        rootFilePaths = []

        basePath = "%s/%s" % (self.SEPath, self.crabDir)

        subDirs = os.listdir(basePath)
        print "subDirs: ", subDirs
        if len(subDirs) != 1:
            print "More than 1 sub directories ... please check"
            for subDir in subDirs:
                print "%s/%s" % (basePath, subDir)
            sys.exit()

        extendedPath = "%s/%s" % (basePath, subDirs[0])

        subsubDirs = os.listdir(extendedPath)
        print "subsubDirs: ", subsubDirs

        for subsubDir in subsubDirs:
            rootFilePath = "%s/%s" % (extendedPath, subsubDir)
            rootFilePaths.append( rootFilePath+"/*.root" )

        print "rootFilePaths: ", rootFilePaths

        cmd = "hadd %s \\\n" % (self.treeName)
        for rootFilePath in rootFilePaths:
            if rootFilePath == rootFilePaths[-1]: # -- last path?
                cmd = cmd + "%s\n" % rootFilePath
            else:
                cmd = cmd + "%s \\\n" % rootFilePath
        cmd = cmd + 'echo "[%s] is produced"\n' % self.treeName

        print "cmd for hadd: \n", cmd
        self.haddCMDs.append( cmd )


        # print "under %s" % basePath
        # for (path, dir1, files) in os.walk( basePath ):
        #     print "path:  ", path
        #     print "dir1:  ", dir1
        #     print "files: ", files

    def _MakeXrdcpCMD(self):
        cmd = "xrdcp %s %s/%s\n" % (self.treeName, self.xrdProtocol, self.eosPath)
        cmd = cmd + 'echo "[xrdcp is finished: %s -> %s]"\n' % (self.treeName, self.eosPath)
        print "cmd for xrdcp: \n", cmd

        self.xrdcpCMDs.append( cmd )

    def _PrintVar(self):
        print "*" * 100
        print "scriptName  = %s" % self.scriptName
        print "SEPath      = %s" % self.SEPath
        print "xrdProtocol = %s" % self.xrdProtocol
        print "crabDir     = %s" % self.crabDir
        print "treeName    = %s" % self.treeName
        print "eosPath     = %s" % self.eosPath
        print "*" * 100
        print "\n"

    def _CheckVar(self):
        if self.scriptName  == "" or \
           self.SEPath      == "" or \
           self.xrdProtocol == "" or \
           self.crabDir     == "" or \
           self.treeName    == "" or \
           self.eosPath     == "":
           print "at least one mandatory variable is not set yet ... check"
           sys.exit()
