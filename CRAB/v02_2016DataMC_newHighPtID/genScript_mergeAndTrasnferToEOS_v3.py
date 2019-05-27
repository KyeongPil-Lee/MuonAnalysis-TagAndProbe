from MuonAnalysis.TagAndProbe.TransferToEOSTool import *

tool = TransferToEOSTool()
# -- common settings
tool.scriptName = "script_mergeAndTrasnferToEOS_v3.sh"
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

# tool.crabDir = "crab_TnPTreeZ_v20190504_07Aug17_SingleMuon_Run2016Bver2_GoldenJSON"
# tool.treeName = "TnPTreeZ_07Aug17_SingleMuon_Run2016Bver2_GoldenJSON.root"
# # tool.eosPath = "/eos/cms/store/group/phys_muon/TagAndProbe/Run2018/102X"
# tool.eosPath = "None"
# tool.Register()

# tool.crabDir = "crab_TnPTreeZ_v20190504_07Aug17_SingleMuon_Run2016C_GoldenJSON"
# tool.treeName = "TnPTreeZ_07Aug17_SingleMuon_Run2016C_GoldenJSON.root"
# tool.eosPath = "None"
# tool.Register()

tool.crabDir = "crab_TnPTreeZ_v20190514_ignoreLocality_07Aug17_SingleMuon_Run2016D_GoldenJSON"
tool.treeName = "TnPTreeZ_07Aug17_SingleMuon_Run2016D_GoldenJSON_Incomplete_20190527.root"
tool.eosPath = "None"
tool.Register()

# tool.crabDir = "crab_TnPTreeZ_v20190504_07Aug17_SingleMuon_Run2016E_GoldenJSON"
# tool.treeName = "TnPTreeZ_07Aug17_SingleMuon_Run2016E_GoldenJSON.root"
# tool.eosPath = "None"
# tool.Register()

tool.crabDir = "crab_TnPTreeZ_v20190514_ignoreLocality_07Aug17_SingleMuon_Run2016F_GoldenJSON"
tool.treeName = "TnPTreeZ_07Aug17_SingleMuon_Run2016F_GoldenJSON_Incomplete_20190527.root"
tool.eosPath = "None"
tool.Register()

tool.crabDir = "crab_TnPTreeZ_v20190514_ignoreLocality_07Aug17_SingleMuon_Run2016G_GoldenJSON"
tool.treeName = "TnPTreeZ_07Aug17_SingleMuon_Run2016G_GoldenJSON.root"
tool.eosPath = "None"
tool.Register()

# tool.crabDir = "crab_TnPTreeZ_v20190509_100LumiPerJob_07Aug17_SingleMuon_Run2016H_GoldenJSON"
# tool.treeName = "TnPTreeZ_07Aug17_SingleMuon_Run2016H_GoldenJSON_Incomplete_20190513.root"
# tool.eosPath = "None"
# tool.Register()

tool.GenScript()