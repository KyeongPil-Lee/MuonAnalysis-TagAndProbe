from MuonAnalysis.TagAndProbe.TransferToEOSTool import *

tool = TransferToEOSTool()
# -- common settings
tool.scriptName = "script_mergeAndTrasnferToEOS.sh"
tool.xrdProtocol = "root://eoscms.cern.ch"

# -- individual settings

# # -- SingleMuon trees
tool.SEPath = "/pnfs/knu.ac.kr/data/cms/store/user/kplee/SingleMuon"

tool.crabDir = "crab_TnPTreeZ_v20181105_17Sep2018_SingleMuon_Run2018Av2_GoldenJSON"
tool.treeName = "TnPTreeZ_17Sep2018_SingleMuon_Run2018Av2_GoldenJSON.root"
tool.eosPath = "/eos/cms/store/group/phys_muon/TagAndProbe/Run2018/94_pre3"
tool.Register()

tool.crabDir = "crab_TnPTreeZ_v20181105_17Sep2018_SingleMuon_Run2018Bv1_GoldenJSON"
tool.treeName = "TnPTreeZ_17Sep2018_SingleMuon_Run2018Bv1_GoldenJSON.root"
tool.eosPath = "/eos/cms/store/group/phys_muon/TagAndProbe/Run2018/94_pre3"
tool.Register()

tool.crabDir = "crab_TnPTreeZ_v20181105_17Sep2018_SingleMuon_Run2018Cv1_GoldenJSON"
tool.treeName = "TnPTreeZ_17Sep2018_SingleMuon_Run2018Cv1_GoldenJSON.root"
tool.eosPath = "/eos/cms/store/group/phys_muon/TagAndProbe/Run2018/94_pre3"
tool.Register()

tool.GenScript()