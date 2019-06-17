from MuonAnalysis.TagAndProbe.TransferToEOSTool import *

tool = TransferToEOSTool()
# -- common settings
tool.scriptName = "script_mergeAndTrasnferToEOS_v5.sh"
tool.xrdProtocol = "root://eoscms.cern.ch"

# -- individual settings

# # -- Z MC tree
# tool.SEPath = "/pnfs/knu.ac.kr/data/cms/store/user/kplee/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8"

# tool.crabDir = "crab_TnPTreeZ_v20190509_10FilesPerJob_94X_DYJetsToLL_M50_MadgraphMLM"
# tool.treeName = "TnPTreeZ_94X_DYJetsToLL_M50_MadgraphMLM_Incomplete_20190607_Final.root"
# tool.eosPath = "None"
# tool.Register()

# -- SingleMuon tree
tool.SEPath = "/pnfs/knu.ac.kr/data/cms/store/user/kplee/SingleMuon"

tool.crabDir = "crab_TnPTreeZ_v20190607_notFinishedLumis_17Nov2017_SingleMuon_Run2017Bv1_GoldenJSON"
tool.treeName = "TnPTreeZ_17Nov2017_SingleMuon_Run2017Bv1_GoldenJSON_notFinishedLumis.root"
tool.eosPath = "None"
tool.Register()


tool.crabDir = "crab_TnPTreeZ_v20190607_notFinishedLumis_17Nov2017_SingleMuon_Run2017Ev1_GoldenJSON"
tool.treeName = "TnPTreeZ_17Nov2017_SingleMuon_Run2017Ev1_GoldenJSON_notFinishedLumis.root"
tool.eosPath = "None"
tool.Register()

# tool.crabDir = "crab_TnPTreeZ_v20190514_ignoreLocality_17Nov2017_SingleMuon_Run2017Fv1_GoldenJSON"
# tool.treeName = "TnPTreeZ_17Nov2017_SingleMuon_Run2017Fv1_GoldenJSON_Incomplete_20190607_Final.root"
# tool.eosPath = "None"
# tool.Register()


tool.GenScript()