from MuonAnalysis.TagAndProbe.TransferTool import *

tool = TransferTool()
# -- common settings
tool.scriptName = "script_mergeAndTransferToMuonServer.sh"
tool.transferType = "ssh"
tool.do_hadd = True

# -- specific setting for ssh
tool.port = 50001
tool.username = "kplee"
tool.host = "147.47.50.161"

# tool.scriptName = "script_mergeAndTransferToMuonServer_noHadd.sh"
# tool.do_hadd = False

# -- individual settings

# -- SingleMuon tree
tool.SEPath = "/pnfs/knu.ac.kr/data/cms/store/user/kplee/SingleMuon"

tool.crabDir    = "crab_TnPTreeZ_v20191105_UnpreIsoMu24_17Nov2017_SingleMuon_Run2017Bv1_GoldenJSON"
tool.treeName   = "TnPTreeZ_UnpreIsoMu24_17Nov2017_SingleMuon_Run2017Bv1_GoldenJSON.root"
tool.outputPath = "/scratch/kplee/TagProbe/TnPTree/2017/v01_unprescaledIsoMu24"
tool.Register()

tool.crabDir    = "crab_TnPTreeZ_v20191105_UnpreIsoMu24_17Nov2017_SingleMuon_Run2017Cv1_GoldenJSON"
tool.treeName   = "TnPTreeZ_UnpreIsoMu24_17Nov2017_SingleMuon_Run2017Cv1_GoldenJSON.root"
tool.outputPath = "/scratch/kplee/TagProbe/TnPTree/2017/v01_unprescaledIsoMu24"
tool.Register()

tool.crabDir    = "crab_TnPTreeZ_v20191105_UnpreIsoMu24_17Nov2017_SingleMuon_Run2017Dv1_GoldenJSON"
tool.treeName   = "TnPTreeZ_UnpreIsoMu24_17Nov2017_SingleMuon_Run2017Dv1_GoldenJSON.root"
tool.outputPath = "/scratch/kplee/TagProbe/TnPTree/2017/v01_unprescaledIsoMu24"
tool.Register()

tool.crabDir    = "crab_TnPTreeZ_v20191105_UnpreIsoMu24_17Nov2017_SingleMuon_Run2017Ev1_GoldenJSON"
tool.treeName   = "TnPTreeZ_UnpreIsoMu24_17Nov2017_SingleMuon_Run2017Ev1_GoldenJSON.root"
tool.outputPath = "/scratch/kplee/TagProbe/TnPTree/2017/v01_unprescaledIsoMu24"
tool.Register()

# tool.crabDir    = "crab_TnPTreeZ_v20191105_UnpreIsoMu24_17Nov2017_SingleMuon_Run2017Fv1_GoldenJSON"
# tool.treeName   = "TnPTreeZ_UnpreIsoMu24_17Nov2017_SingleMuon_Run2017Fv1_GoldenJSON.root"
# tool.outputPath = "/scratch/kplee/TagProbe/TnPTree/2017/v01_unprescaledIsoMu24"
# tool.Register()


tool.GenScript()