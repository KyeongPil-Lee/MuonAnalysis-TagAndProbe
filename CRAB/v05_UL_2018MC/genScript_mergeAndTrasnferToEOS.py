from MuonAnalysis.TagAndProbe.TransferToEOSTool import *

tool = TransferToEOSTool()
# -- common settings
tool.scriptName = "script_mergeAndTrasnferToEOS.sh"
tool.xrdProtocol = "root://eoscms.cern.ch"

# -- individual settings

# # -- Z MC tree
tool.SEPath = "/pnfs/knu.ac.kr/data/cms/store/user/kplee/RelValZMM_13"

tool.crabDir = "crab_TnPTreeZ_v20190613_1060For2018_RelValZMM"
tool.treeName = "TnPTreeZ_1060For2018_RelValZMM.root"
tool.eosPath = "None"
tool.Register()

tool.GenScript()