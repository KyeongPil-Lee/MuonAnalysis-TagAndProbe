import os, sys, getpass

# -- in case paramiko is not available: pip install paramiko --user
import paramiko 
paramiko.util.log_to_file('./sftp.log')

def GetCRABOutputDir(crabDirName, SEPath='/pnfs/knu.ac.kr/data/cms/store/user/kplee'):
    thePath = ""
    print "[GetCRABOutputDir] Searching for %s under %s ..." % (crabDirName, SEPath)

    for (path, list_dir, list_file) in os.walk(SEPath):
        # print "current directories: %s" % list_dir
        if crabDirName in list_dir:
            thePath = "%s/%s" % (path, crabDirName)
            break

    if thePath == "":
        print "[GetCRABOutputDir] No crab directory is found for %s" % crabDirName
        sys.exit()

    if len(os.listdir(thePath)) > 1:
        print "[GetCRABOutputDir] Find more than 1 sub-directories under the crab directory"
        print "  crabDir = %s" % crabDirName
        print "  listDir = ", os.listdir(thePath)
        sys.exit()

    print "[GetCRABOutputDir] Find: %s" % thePath

    return thePath


class TransferTool:
    def __init__(self):
        self.dic_input_to_outputPath = {}

        self.user = "" # -- e.g. kplee
        self.host = "" # -- e.g. lxplus.cern.ch
        self.port = 22
        
        self.do_hadd = False
        self.dic_input_to_mergedFileName = {}

        # -- internal variables
        self.list_outputFile = []
        self.sftp = ""

    def Transfer(self):
        transport = paramiko.Transport((self.host, self.port))
        password = getpass.getpass(prompt="password for %s@%s: " % (self.user, self.host) )
        try:
            transport.connect(username = self.user, password = password)
        except paramiko.ssh_exception.AuthenticationException:
            print "[TransferTool] Wrong password!"
            sys.exit()

        # -- open SFTP
        self.sftp = paramiko.SFTPClient.from_transport(transport)

        for inputPath in self.dic_input_to_outputPath.keys():
            outputPath = self.dic_input_to_outputPath[inputPath]
            self.Transfer_Input_to_Output(inputPath, outputPath)
            print "[Transfer] Transferring is done"
            print "   %s ---> %s" % (inputPath, outputPath)


    def Transfer_Input_to_Output(self, inputPath, outputPath):
        if not self.SFTP_exists(outputPath):
            print "%s does not exist in %s: make it" % (outputPath, self.host)
            self.mkdir_p(outputPath)

        list_outputFile = self.GetListOfOutputFiles(inputPath)
        print "list_outputFile = ", list_outputFile

        if self.do_hadd:
            mergedFilePath = self.MergeROOTFiles(inputPath, list_outputFile)
            list_outputFile = [mergedFilePath] # -- transfer merged file only

        for outputFile in list_outputFile:
            fileName = outputFile.split("/")[-1]
            self.sftp.put(outputFile, outputPath+"/"+fileName)



    # -- search .root file under the drectory (including sub-directories)
    def GetListOfOutputFiles(self, inputPath):
        list_outputFile = []
        print "[GetListOfOutputFiles] Collecting files from %s ..." % inputPath

        for (path, list_dir, list_file) in os.walk(inputPath):
            for fileName in list_file:
                # print "path = ", path
                # print "list_dir = ", list_dir
                # print "list_file = ", list_file
                # print "fileName = ", fileName
                # print "os.path.splitext = ", os.path.splitext(fileName)

                if ".root" == os.path.splitext(fileName)[-1] and "failed" not in path:
                    list_outputFile.append( "%s/%s" % (path, fileName) )

        return list_outputFile

    def MergeROOTFiles(self, inputPath, list_file):
        if len(self.dic_input_to_mergedFileName) == 0:
            print "[MergeROOTFiles] dic_input_to_mergedFileName is empty!"
            sys.exit()

        mergedFileName = self.dic_input_to_mergedFileName[inputPath]

        # -- save in current directory
        cwd = os.getcwd()
        fulloutputPath = "%s/%s" % (cwd, mergedFileName)

        if os.path.exists(fulloutputPath):
            print "[MergeROOTFiles] already merged file exists: %s" % fulloutputPath
            return fulloutputPath

        cmd_hadd = "hadd %s \\\n" % (fulloutputPath)
        for fileName in list_file:
            if fileName == list_file[-1]:
                cmd_hadd = cmd_hadd + "%s" % fileName
            else:
                cmd_hadd = cmd_hadd + "%s \\\n" % fileName

        print cmd_hadd
        os.system(cmd_hadd)

        return fulloutputPath

    def SFTP_exists(self, path):
        try:
            self.sftp.stat(path)
        except IOError, e:
            if e[0] == 2: # -- IOError: [Errno 2] No such file
                return False
            raise
        else:
            return True

    # -- https://stackoverflow.com/questions/14819681/upload-files-using-sftp-in-python-but-create-directories-if-path-doesnt-exist
    def mkdir_p(self, remote_directory):
        if remote_directory == '/':
            # absolute path so change directory to root
            self.sftp.chdir('/')
            return
        if remote_directory == '':
            # top-level relative directory must exist
            return
        try:
            self.sftp.chdir(remote_directory) # sub-directory exists
        except IOError:
            dirname, basename = os.path.split(remote_directory.rstrip('/'))
            self.mkdir_p(dirname) # make parent directories
            self.sftp.mkdir(basename) # sub-directory missing, so created it
            self.sftp.chdir(basename)
            return True










