from MuonAnalysis.TagAndProbe.TransferToEOSTool import *

tool = TransferToEOSTool()
# -- common settings
tool.scriptName = "script_mergeAndTrasnferToEOS.sh"
tool.xrdProtocol = "root://eoscms.cern.ch"

# -- individual settings

# # -- SingleMuon trees
tool.SEPath = "/pnfs/knu.ac.kr/data/cms/store/user/kplee/SingleMuon"

tool.crabDir = "crab_TnPTreeZ_v20181130_102XAutumn18_DYJetsToLL_M50_MadgraphMLM"
tool.treeName = "TnPTreeZ_102XAutumn18_DYJetsToLL_M50_MadgraphMLM_Incomplete.root"
tool.eosPath = "/eos/cms/store/group/phys_muon/TagAndProbe/Run2018/94_pre3"
tool.Register()

tool.GenScript()