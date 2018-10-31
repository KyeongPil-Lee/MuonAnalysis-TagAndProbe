from MuonAnalysis.TagAndProbe.TransferToEOSTool import *

tool = TransferToEOSTool()
# -- common settings
tool.scriptName = "script_mergeAndTrasnferToEOS.sh"
tool.xrdProtocol = "root://eoscms.cern.ch"

# -- individual settings

# -- DY MC sample
tool.SEPath = "/pnfs/knu.ac.kr/data/cms/store/user/kplee/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8"
tool.crabDir = "crab_TnPTreeZ_v20181026_102X_DYJetsToLL_M50_MadgraphMLM"
tool.treeName = "TnPTreeZ_102X_DYJetsToLL_M50_MadgraphMLM_withtpTreeSta.root"
tool.eosPath = "/eos/cms/store/group/phys_muon/TagAndProbe/Run2018/94_pre3"
tool.Register()

tool.GenScript()