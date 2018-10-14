from MuonAnalysis.TagAndProbe.TransferToEOSTool import *

tool = TransferToEOSTool()
# -- common settings
# tool.scriptName = "script_mergeAndTrasnferToEOS.sh"
tool.scriptName = "script_mergeAndTrasnferToEOS_v2_DYMC.sh"
tool.xrdProtocol = "root://eoscms.cern.ch"

# -- individual settings

# # -- SingleMuon trees
# tool.SEPath = "/pnfs/knu.ac.kr/data/cms/store/user/kplee/SingleMuon"

# tool.crabDir = "crab_TnPTreeZ_v20180904_SingleMuon_Run2018Cv3_GoldenJSON_from319852ToEnd"
# tool.treeName = "TnPTreeZ_SingleMuon_Run2018Cv3_GoldenJSON_from319852ToEnd.root"
# tool.eosPath = "/eos/cms/store/group/phys_muon/TagAndProbe/Run2018/94_pre3"
# tool.Register()

# tool.crabDir = "crab_TnPTreeZ_v20181012_SingleMuon_Run2018Dv2_GoldenJSON_FirstRun_to_323523"
# tool.treeName = "TnPTreeZ_SingleMuon_Run2018Dv2_GoldenJSON_FirstRun_to_323523.root"
# tool.eosPath = "/eos/cms/store/group/phys_muon/TagAndProbe/Run2018/94_pre3"
# tool.Register()


# -- DY MC sample
tool.SEPath = "/pnfs/knu.ac.kr/data/cms/store/user/kplee/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8"
tool.crabDir = "crab_TnPTreeZ_v20181013_102X_DYJetsToLL_M50_MadgraphMLM"
tool.treeName = "TnPTreeZ_102X_DYJetsToLL_M50_MadgraphMLM.root"
tool.eosPath = "/eos/cms/store/group/phys_muon/TagAndProbe/Run2018/94_pre3"
tool.Register()


# # -- Charmonium sample
# tool.SEPath = "/pnfs/knu.ac.kr/data/cms/store/user/kplee/Charmonium"
# tool.crabDir = "crab_TnPTreeJPsi_v20181012_Charmonium_Run2018Dv2_GoldenJSON_321222_to_323523"
# tool.treeName = "TnPTreeJPsi_Charmonium_Run2018Dv2_GoldenJSON_321222_to_323523.root"
# tool.eosPath = "/eos/cms/store/group/phys_muon/TagAndProbe/Run2018/94_pre3"
# tool.Register()


# # -- J/Psi MC sample
# tool.SEPath = "/pnfs/knu.ac.kr/data/cms/store/user/kplee/JpsiToMuMu_JpsiPt8_TuneCP5_13TeV-pythia8"
# tool.crabDir = "crab_TnPTreeJPsi_v20181012_102X_JpsiToMuMu_JpsiPt8_Pythia8"
# tool.treeName = "TnPTreeJPsi_102X_JpsiToMuMu_JpsiPt8_Pythia8.root"
# tool.eosPath = "/eos/cms/store/group/phys_muon/TagAndProbe/Run2018/94_pre3"
# tool.Register()


tool.GenScript()