from MuonAnalysis.TagAndProbe.TransferToEOSTool import *

tool = TransferToEOSTool()
# -- common settings
tool.scriptName = "script_mergeAndTrasnferToEOS.sh"
tool.xrdProtocol = "root://eoscms.cern.ch"

# -- individual settings

# -- J/Psi trees
tool.SEPath = "/pnfs/knu.ac.kr/data/cms/store/user/kplee/Charmonium"

tool.crabDir = "crab_TnPTreeJPsi_v20180828_Charmonium_Run2018Av1_GoldenJSON"
tool.treeName = "TnPTreeJPsi_v20180828_Charmonium_Run2018Av1_GoldenJSON.root"
tool.eosPath = "/eos/cms/store/group/phys_muon/TagAndProbe/Run2018/94_pre3"
tool.Register()

tool.crabDir = "crab_TnPTreeJPsi_v20180828_Charmonium_Run2018Av2_GoldenJSON"
tool.treeName = "TnPTreeJPsi_v20180828_Charmonium_Run2018Av2_GoldenJSON.root"
tool.eosPath = "/eos/cms/store/group/phys_muon/TagAndProbe/Run2018/94_pre3"
tool.Register()

tool.crabDir = "crab_TnPTreeJPsi_v20180828_Charmonium_Run2018Av3_GoldenJSON"
tool.treeName = "TnPTreeJPsi_v20180828_Charmonium_Run2018Av3_GoldenJSON.root"
tool.eosPath = "/eos/cms/store/group/phys_muon/TagAndProbe/Run2018/94_pre3"
tool.Register()

tool.crabDir = "crab_TnPTreeJPsi_v20180828_Charmonium_Run2018Bv1_GoldenJSON"
tool.treeName = "TnPTreeJPsi_v20180828_Charmonium_Run2018Bv1_GoldenJSON.root"
tool.eosPath = "/eos/cms/store/group/phys_muon/TagAndProbe/Run2018/94_pre3"
tool.Register()

tool.crabDir = "crab_TnPTreeJPsi_v20180828_Charmonium_Run2018Bv2_GoldenJSON"
tool.treeName = "TnPTreeJPsi_v20180828_Charmonium_Run2018Bv2_GoldenJSON.root"
tool.eosPath = "/eos/cms/store/group/phys_muon/TagAndProbe/Run2018/94_pre3"
tool.Register()

tool.crabDir = "crab_TnPTreeJPsi_v20180828_Charmonium_Run2018Cv1_GoldenJSON"
tool.treeName = "TnPTreeJPsi_v20180828_Charmonium_Run2018Cv1_GoldenJSON.root"
tool.eosPath = "/eos/cms/store/group/phys_muon/TagAndProbe/Run2018/94_pre3"
tool.Register()

tool.crabDir = "crab_TnPTreeJPsi_v20180828_Charmonium_Run2018Cv2_GoldenJSON"
tool.treeName = "TnPTreeJPsi_v20180828_Charmonium_Run2018Cv2_GoldenJSON.root"
tool.eosPath = "/eos/cms/store/group/phys_muon/TagAndProbe/Run2018/94_pre3"
tool.Register()

tool.crabDir = "crab_TnPTreeJPsi_v20180828_Charmonium_Run2018Cv3_GoldenJSON"
tool.treeName = "TnPTreeJPsi_v20180828_Charmonium_Run2018Cv3_GoldenJSON.root"
tool.eosPath = "/eos/cms/store/group/phys_muon/TagAndProbe/Run2018/94_pre3"
tool.Register()

tool.crabDir = "crab_TnPTreeJPsi_v20180828_Charmonium_Run2018Dv2_GoldenJSON_Upto321221"
tool.treeName = "TnPTreeJPsi_v20180828_Charmonium_Run2018Dv2_GoldenJSON_Upto321221.root"
tool.eosPath = "/eos/cms/store/group/phys_muon/TagAndProbe/Run2018/94_pre3"
tool.Register()

tool.GenScript()