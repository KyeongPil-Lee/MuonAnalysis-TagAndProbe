from MuonAnalysis.TagAndProbe.TransferToEOSTool import *

tool = TransferToEOSTool()
# -- common settings
# tool.scriptName = "script_mergeAndTrasnferToEOS.sh"
tool.scriptName = "script_mergeAndTrasnferToEOS_JPsi.sh"
tool.xrdProtocol = "root://eoscms.cern.ch"

# -- individual settings

# -- Z MC tree
tool.SEPath = "/pnfs/knu.ac.kr/data/cms/store/user/kplee/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8"

tool.crabDir = "crab_TnPTreeZ_v20190211_102XAutumn18_DYJetsToLL_M50_MadgraphMLM"
tool.treeName = "TnPTreeZ_102XAutumn18_DYJetsToLL_M50_MadgraphMLM.root"
tool.eosPath = "/eos/cms/store/group/phys_muon/TagAndProbe/Run2018/102X"
tool.Register()

# -- SingleMuon tree
tool.SEPath = "/pnfs/knu.ac.kr/data/cms/store/user/kplee/SingleMuon"

tool.crabDir = "crab_TnPTreeZ_v20190211_17Sep2018_SingleMuon_Run2018Av2_GoldenJSON"
tool.treeName = "TnPTreeZ_17Sep2018_SingleMuon_Run2018Av2_GoldenJSON.root"
tool.eosPath = "/eos/cms/store/group/phys_muon/TagAndProbe/Run2018/102X"
tool.Register()

tool.crabDir = "crab_TnPTreeZ_v20190211_17Sep2018_SingleMuon_Run2018Bv1_GoldenJSON"
tool.treeName = "TnPTreeZ_17Sep2018_SingleMuon_Run2018Bv1_GoldenJSON.root"
tool.eosPath = "/eos/cms/store/group/phys_muon/TagAndProbe/Run2018/102X"
tool.Register()

tool.crabDir = "crab_TnPTreeZ_v20190211_17Sep2018_SingleMuon_Run2018Cv1_GoldenJSON"
tool.treeName = "TnPTreeZ_17Sep2018_SingleMuon_Run2018Cv1_GoldenJSON.root"
tool.eosPath = "/eos/cms/store/group/phys_muon/TagAndProbe/Run2018/102X"
tool.Register()

tool.crabDir = "crab_TnPTreeZ_v20190211_SingleMuon_Run2018Dv2_GoldenJSON"
tool.treeName = "TnPTreeZ_SingleMuon_Run2018Dv2_GoldenJSON.root"
tool.eosPath = "/eos/cms/store/group/phys_muon/TagAndProbe/Run2018/102X"
tool.Register()

# # -- J/Psi MC tree
# tool.SEPath = "/pnfs/knu.ac.kr/data/cms/store/user/kplee/JpsiToMuMu_JpsiPt8_TuneCP5_13TeV-pythia8"

# tool.crabDir = "crab_TnPTreeJPsi_v20190211_102XAutumn18_JpsiToMuMu_JpsiPt8_Pythia8"
# tool.treeName = "TnPTreeJPsi_102XAutumn18_JpsiToMuMu_JpsiPt8_Pythia8.root"
# tool.eosPath = "/eos/cms/store/group/phys_muon/TagAndProbe/Run2018/102X"
# tool.Register()

# # -- Charmonium tree, 2018 data
# tool.SEPath = "/pnfs/knu.ac.kr/data/cms/store/user/kplee/Charmonium"

# tool.crabDir = "crab_TnPTreeJPsi_v20190211_17Sep2018_Charmonium_Run2018Av1_GoldenJSON"
# tool.treeName = "TnPTreeJPsi_17Sep2018_Charmonium_Run2018Av1_GoldenJSON.root"
# tool.eosPath = "/eos/cms/store/group/phys_muon/TagAndProbe/Run2018/102X"
# tool.Register()

# tool.crabDir = "crab_TnPTreeJPsi_v20190211_17Sep2018_Charmonium_Run2018Bv1_GoldenJSON"
# tool.treeName = "TnPTreeJPsi_17Sep2018_Charmonium_Run2018Bv1_GoldenJSON.root"
# tool.eosPath = "/eos/cms/store/group/phys_muon/TagAndProbe/Run2018/102X"
# tool.Register()

# tool.crabDir = "crab_TnPTreeJPsi_v20190211_17Sep2018_Charmonium_Run2018Cv1_GoldenJSON"
# tool.treeName = "TnPTreeJPsi_17Sep2018_Charmonium_Run2018Cv1_GoldenJSON.root"
# tool.eosPath = "/eos/cms/store/group/phys_muon/TagAndProbe/Run2018/102X"
# tool.Register()

# tool.crabDir = "crab_TnPTreeJPsi_v20190211_Charmonium_Run2018Dv2_GoldenJSON"
# tool.treeName = "TnPTreeJPsi_Charmonium_Run2018Dv2_GoldenJSON.root"
# tool.eosPath = "/eos/cms/store/group/phys_muon/TagAndProbe/Run2018/102X"
# tool.Register()


tool.GenScript()