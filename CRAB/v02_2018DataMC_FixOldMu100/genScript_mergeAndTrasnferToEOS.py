from MuonAnalysis.TagAndProbe.TransferToEOSTool import *

tool = TransferToEOSTool()
# -- common settings
tool.scriptName = "script_mergeAndTrasnferToEOS.sh"
tool.xrdProtocol = "root://eoscms.cern.ch"

# -- individual settings

# # -- Z MC tree
tool.SEPath = "/pnfs/knu.ac.kr/data/cms/store/user/kplee/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8"

tool.crabDir = "crab_TnPTreeZ_v20190509_10FilesPerJob_102XAutumn18_DYJetsToLL_M50_MadgraphMLM"
tool.treeName = "TnPTreeZ_102XAutumn18_DYJetsToLL_M50_MadgraphMLM_Incomplete_20190513.root"
tool.eosPath = "None"
tool.Register()

# -- SingleMuon tree
tool.SEPath = "/pnfs/knu.ac.kr/data/cms/store/user/kplee/SingleMuon"

tool.crabDir = "crab_TnPTreeZ_v20190509_100LumiPerJob_17Sep2018_SingleMuon_Run2018Av2_GoldenJSON"
tool.treeName = "TnPTreeZ_17Sep2018_SingleMuon_Run2018Av2_GoldenJSON_Incomplete_20190513.root"
tool.eosPath = "None"
tool.Register()

tool.crabDir = "crab_TnPTreeZ_v20190504_17Sep2018_SingleMuon_Run2018Bv1_GoldenJSON"
tool.treeName = "TnPTreeZ_17Sep2018_SingleMuon_Run2018Bv1_GoldenJSON.root"
tool.eosPath = "None"
tool.Register()

tool.crabDir = "crab_TnPTreeZ_v20190509_100LumiPerJob_17Sep2018_SingleMuon_Run2018Cv1_GoldenJSON"
tool.treeName = "TnPTreeZ_17Sep2018_SingleMuon_Run2018Cv1_GoldenJSON_Incomplete_20190513.root"
tool.eosPath = "None"
tool.Register()

tool.crabDir = "crab_TnPTreeZ_v20190509_100LumiPerJob_SingleMuon_Run2018Dv2_GoldenJSON"
tool.treeName = "TnPTreeZ_17Sep2018_SingleMuon_Run2018Dv1_GoldenJSON_Incomplete_20190513.root"
tool.eosPath = "None"
tool.Register()


tool.GenScript()