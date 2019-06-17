from MuonAnalysis.TagAndProbe.TransferToEOSTool import *

tool = TransferToEOSTool()
# -- common settings
tool.scriptName = "script_mergeAndTrasnferToEOS_v7.sh"
tool.xrdProtocol = "root://eoscms.cern.ch"

# -- individual settings

# # -- Z MC tree
# tool.SEPath = "/pnfs/knu.ac.kr/data/cms/store/user/kplee/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"

# tool.crabDir = "crab_TnPTreeZ_v20190504_80X_DYJetsToLL_M50_MadgraphMLM"
# tool.treeName = "TnPTreeZ_80X_DYJetsToLL_M50_MadgraphMLM.root"
# tool.eosPath = "None"
# tool.Register()

# -- SingleMuon tree
tool.SEPath = "/pnfs/knu.ac.kr/data/cms/store/user/kplee/SingleMuon"

tool.crabDir = "crab_TnPTreeZ_v20190607_notFinishedLumis_07Aug17_SingleMuon_Run2016D_GoldenJSON"
tool.treeName = "TnPTreeZ_07Aug17_SingleMuon_Run2016D_GoldenJSON_unFinishedLumis.root"
tool.eosPath = "None"
tool.Register()


tool.GenScript()