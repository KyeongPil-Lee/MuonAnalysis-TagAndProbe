import os, sys

class TransferTool:
    def __init__(self):

        self.scriptName = ""
        self.transferType = "" # -- ssh or xrd
        self.do_hadd = True # -- merge into one file and transfer it; if false, just transfer individual files without merging

        # -- for ssh
        self.host = "" # -- e.g. 147.47.50.161
        self.username = "kplee"
        self.port = 22

        # -- for xrd
        self.xrdProtocol = "" # -- e.g. root://eoscms.cern.ch

        # -- individual settings for each tree
        self.SEPath = "" # -- SE = storage element
        self.crabDir = ""
        self.treeName = ""
        self.outputPath = "" # -- xrd: xrd path, ssh: absolute path at the remote server

        # -- internal variable
        self.list_rootFilePath = []
        self.list_haddCMD = []
        self.list_cpCMD = [] # -- scp or xrdcp

    def Register(self):
        self._PrintVar()
        self._CheckVar()

        self._GetROOTFilePath()

        if self.do_hadd:
            self._MakeCMD_hadd()

        self._MakeCMD_cp()

        self._Init()

    def GenScript(self):

        if self.scriptName in os.listdir("."):
            print "%s already exists in same directory ... please change the name" % self.scriptName
            sys.exit()

        f = open(self.scriptName, "w")

        f.write("#!bin/bash\n\n")

        for i_tree in range(0, len(self.list_cpCMD)):
            if self.do_hadd:
                haddCMD = self.list_haddCMD[i_tree]
                cpCMD = self.list_cpCMD[i_tree]

                f.write( haddCMD  + "\n" )
                f.write( cpCMD + "\n\n\n" )

            else:
                cpCMD = self.list_cpCMD[i_tree]
                f.write( cpCMD + "\n\n\n" )

        f.write( 'echo "All jobs are finished"\n')

        f.close()

        os.system( "cat %s" % self.scriptName )

        print "*" * 100
        print "*" * 100
        print "script is generated: %s" % self.scriptName
        print "source %s >&%s.log&" % (self.scriptName, self.scriptName.split('.sh')[0])
        print "Check list before running script"
        print "1) ROOT: available? (for hadd)"
        print "2) VOCMS certificate: valid? (if transferType == xrd)"
        print "3) All necessary EOS directories are available? (if transferType == xrd)"
        print "*" * 100
        print "*" * 100


    def _GetROOTFilePath(self):
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
            self.list_rootFilePath.append( rootFilePath+"/*.root" )

        print "list_rootFilePath: ", self.list_rootFilePath


    def _MakeCMD_hadd(self):
        cmd = "hadd %s \\\n" % (self.treeName)
        for rootFilePath in self.list_rootFilePath:
            if rootFilePath == self.list_rootFilePath[-1]: # -- last path?
                cmd = cmd + "%s\n" % rootFilePath
            else:
                cmd = cmd + "%s \\\n" % rootFilePath
        cmd = cmd + 'echo "[%s] is produced"\n' % self.treeName

        print "cmd for hadd: \n", cmd
        self.list_haddCMD.append( cmd )


        # print "under %s" % basePath
        # for (path, dir1, files) in os.walk( basePath ):
        #     print "path:  ", path
        #     print "dir1:  ", dir1
        #     print "files: ", files

    def _MakeCMD_cp(self):
        if self.do_hadd:
            if self.transferType == "xrd":
                cmd = "xrdcp %s %s/%s\n" % (self.treeName, self.xrdProtocol, self.outputPath)
                cmd = cmd + 'echo "[xrdcp is finished: %s -> %s]"\n' % (self.treeName, self.outputPath)
                print "cmd for xrdcp: \n", cmd

            elif self.transferType == "ssh":
                cmd = "scp -P %d %s %s@%s:%s\n" % (self.port, self.treeName, self.username, self.host, self.outputPath)
                cmd = cmd + 'echo "[scp is finished: %s -> %s]"\n' % (self.treeName, self.outputPath)
                print "cmd for scp: \n", cmd

        else:
            if self.transferType == "xrd":
                cmd = "xrdcp \\\n"
                for rootFilePath in self.list_rootFilePath:
                    cmd = cmd + "%s \\\n" % rootFilePath
                cmd = cmd + "%s/%s\n" % (self.xrdProtocol, self.outputPath)
                cmd = cmd + 'echo "[xrdcp to %s is finished]"\n' % (self.outputPath)
                print "cmd for xrdcp: \n", cmd

            elif self.transferType == "ssh":
                cmd = "scp -P %d \\\n" % (self.port)
                for rootFilePath in self.list_rootFilePath:
                    cmd = cmd + "%s \\\n" % rootFilePath
                cmd = cmd + "%s@%s:%s\n" % (self.username, self.host, self.outputPath)
                print "cmd for scp: \n", cmd

        self.list_cpCMD.append( cmd )

    def _PrintVar(self):
        print "*" * 100

        print "scriptName   = %s" % self.scriptName
        print "transferType = %s" % self.transferType
        print "do_hadd      = %s" % self.do_hadd

        if self.transferType == "ssh":
            print "host     = %s" % self.host
            print "username = %s" % self.username
            print "port     = %d" % self.port
        elif self.transferType == "xrd":
            print "xrdProtocol = %s" % self.xrdProtocol

        print "crabDir     = %s" % self.crabDir
        print "treeName    = %s" % self.treeName
        print "outputPath  = %s" % self.outputPath

        print "*" * 100
        print "\n"

    def _CheckVar(self):
        if self.scriptName   == "" or \
           self.transferType == "" or \
           self.crabDir      == "" or \
           self.outputPath   == "":
           print "at least one mandatory variable is not set yet ... check"
           sys.exit()

        if self.do_hadd and self.treeName == "":
            print "at least one mandatory variable is not set yet ... check"

        if self.transferType == "ssh" and self.host == "":
            print "at least one mandatory variable is not set yet ... check"

        if self.transferType == "xrd" and self.xrdProtocol == "":
            print "at least one mandatory variable is not set yet ... check"


    def _Init(self):
        self.crabDir = ""
        self.treeName = ""
        self.outputPath = ""
        self.list_rootFilePath = []


