from MuonAnalysis.TagAndProbe.TransferToEOSTool import *

tool = TransferToEOSTool()
# -- common settings
tool.scriptName = "script_mergeAndTrasnferToEOS.sh"
tool.xrdProtocol = "root://eoscms.cern.ch"

# -- individual settings

# -- J/Psi MC tree
tool.SEPath = "/pnfs/knu.ac.kr/data/cms/store/user/kplee/JpsiToMuMu_JpsiPt8_TuneCP5_13TeV-pythia8"

tool.crabDir = "crab_TnPTreeJPsi_v20181212_102XAutumn18_JpsiToMuMu_JpsiPt8_Pythia8"
tool.treeName = "TnPTreeJPsi_102XAutumn18_JpsiToMuMu_JpsiPt8_Pythia8.root"
tool.eosPath = "/eos/cms/store/group/phys_muon/TagAndProbe/Run2018/94_pre3"
tool.Register()

# -- Charmonium tree
tool.SEPath = "/pnfs/knu.ac.kr/data/cms/store/user/kplee/Charmonium"

tool.crabDir = "crab_TnPTreeJPsi_v20181212_Charmonium_Run2018Dv2_GoldenJSON_323524_to_End"
tool.treeName = "TnPTreeJPsi_Charmonium_Run2018Dv2_GoldenJSON_323524_to_End.root"
tool.eosPath = "/eos/cms/store/group/phys_muon/TagAndProbe/Run2018/94_pre3"
tool.Register()

# -- Z MC tree
tool.SEPath = "/pnfs/knu.ac.kr/data/cms/store/user/kplee/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8"

tool.crabDir = "crab_TnPTreeZ_v20181212_102XAutumn18_DYJetsToLL_M50_MadgraphMLM"
tool.treeName = "TnPTreeZ_102XAutumn18_DYJetsToLL_M50_MadgraphMLM.root"
tool.eosPath = "/eos/cms/store/group/phys_muon/TagAndProbe/Run2018/94_pre3"
tool.Register()

# # -- SingleMuon tree
# tool.SEPath = "/pnfs/knu.ac.kr/data/cms/store/user/kplee/SingleMuon"

# tool.crabDir = "crab_TnPTreeZ_v20181212_SingleMuon_Run2018Dv2_GoldenJSON_323524_to_End"
# tool.treeName = "TnPTreeZ_SingleMuon_Run2018Dv2_GoldenJSON_323524_to_End.root"
# tool.eosPath = "/eos/cms/store/group/phys_muon/TagAndProbe/Run2018/94_pre3"
# tool.Register()

tool.GenScript()