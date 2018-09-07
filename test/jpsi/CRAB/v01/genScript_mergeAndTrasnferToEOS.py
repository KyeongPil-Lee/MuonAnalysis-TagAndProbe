from MuonAnalysis.TagAndProbe.TransferToEOSTool import *

tool = TransferToEOSTool()
# -- common settings
tool.scriptName = "script_mergeAndTrasnferToEOS.sh"
tool.xrdProtocol = "root://eoscms.cern.ch"

# -- individual settings

# -- J/Psi trees
tool.SEPath = "/pnfs/knu.ac.kr/data/cms/store/user/kplee/Charmonium"

tool.crabDir = "crab_TagProbe_v20180903_LegacyRerecoWithIDFlag_Charmonium_Run2016Bver2_GoldenJSON"
tool.treeName = "TnPTreeJPsi_LegacyRereco07Aug17_Charmonium_Run2016Bver2_GoldenJSON.root"
tool.eosPath = "/eos/cms/store/group/phys_muon/TagAndProbe/Run2016/80X_v6/IDFlag"
tool.Register()

tool.crabDir = "crab_TagProbe_v20180903_LegacyRerecoWithIDFlag_Charmonium_Run2016C_GoldenJSON"
tool.treeName = "TnPTreeJPsi_LegacyRereco07Aug17_Charmonium_Run2016C_GoldenJSON.root"
tool.eosPath = "/eos/cms/store/group/phys_muon/TagAndProbe/Run2016/80X_v6/IDFlag"
tool.Register()

tool.crabDir = "crab_TagProbe_v20180903_LegacyRerecoWithIDFlag_Charmonium_Run2016D_GoldenJSON"
tool.treeName = "TnPTreeJPsi_LegacyRereco07Aug17_Charmonium_Run2016D_GoldenJSON.root"
tool.eosPath = "/eos/cms/store/group/phys_muon/TagAndProbe/Run2016/80X_v6/IDFlag"
tool.Register()

tool.crabDir = "crab_TagProbe_v20180903_LegacyRerecoWithIDFlag_Charmonium_Run2016E_GoldenJSON"
tool.treeName = "TnPTreeJPsi_LegacyRereco07Aug17_Charmonium_Run2016E_GoldenJSON.root"
tool.eosPath = "/eos/cms/store/group/phys_muon/TagAndProbe/Run2016/80X_v6/IDFlag"
tool.Register()

tool.crabDir = "crab_TagProbe_v20180903_LegacyRerecoWithIDFlag_Charmonium_Run2016F_GoldenJSON"
tool.treeName = "TnPTreeJPsi_LegacyRereco07Aug17_Charmonium_Run2016F_GoldenJSON.root"
tool.eosPath = "/eos/cms/store/group/phys_muon/TagAndProbe/Run2016/80X_v6/IDFlag"
tool.Register()

tool.crabDir = "crab_TagProbe_v20180903_LegacyRerecoWithIDFlag_Charmonium_Run2016G_GoldenJSON"
tool.treeName = "TnPTreeJPsi_LegacyRereco07Aug17_Charmonium_Run2016G_GoldenJSON.root"
tool.eosPath = "/eos/cms/store/group/phys_muon/TagAndProbe/Run2016/80X_v6/IDFlag"
tool.Register()

tool.crabDir = "crab_TagProbe_v20180903_LegacyRerecoWithIDFlag_Charmonium_Run2016H_GoldenJSON"
tool.treeName = "TnPTreeJPsi_LegacyRereco07Aug17_Charmonium_Run2016H_GoldenJSON.root"
tool.eosPath = "/eos/cms/store/group/phys_muon/TagAndProbe/Run2016/80X_v6/IDFlag"
tool.Register()

tool.GenScript()