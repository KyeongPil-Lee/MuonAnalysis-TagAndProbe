from MuonAnalysis.TagAndProbe.TransferToEOSTool import *

tool = TransferToEOSTool()
# -- common settings
tool.scriptName = "script_mergeAndTrasnferToEOS.sh"
tool.xrdProtocol = "root://eoscms.cern.ch"

# -- individual settings
tool.SEPath = "/pnfs/knu.ac.kr/data/cms/store/user/kplee/JpsiToMuMu_JpsiPt8_TuneCUEP8M1_13TeV-pythia8"

tool.crabDir = "crab_TagProbe_v20181011_LegacyRerecoWithIDFlag_JpsiToMuMu_JpsiPt8_Pythia8"
tool.treeName = "TnPTreeJPsi_80X_JpsiToMuMu_JpsiPt8_Pythia8.root"
tool.eosPath = "/eos/cms/store/group/phys_muon/TagAndProbe/Run2016/80X_v2/jpsi/JpsiToMuMu_JpsiPt8/IDFlag"
tool.Register()

tool.GenScript()