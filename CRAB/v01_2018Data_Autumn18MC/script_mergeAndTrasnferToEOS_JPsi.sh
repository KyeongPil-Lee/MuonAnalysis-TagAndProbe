#!bin/bash

hadd TnPTreeJPsi_102XAutumn18_JpsiToMuMu_JpsiPt8_Pythia8.root \
/pnfs/knu.ac.kr/data/cms/store/user/kplee/JpsiToMuMu_JpsiPt8_TuneCP5_13TeV-pythia8/crab_TnPTreeJPsi_v20190211_102XAutumn18_JpsiToMuMu_JpsiPt8_Pythia8/190211_152028/0000/*.root
echo "[TnPTreeJPsi_102XAutumn18_JpsiToMuMu_JpsiPt8_Pythia8.root] is produced"

xrdcp TnPTreeJPsi_102XAutumn18_JpsiToMuMu_JpsiPt8_Pythia8.root root://eoscms.cern.ch//eos/cms/store/group/phys_muon/TagAndProbe/Run2018/102X
echo "[xrdcp is finished: TnPTreeJPsi_102XAutumn18_JpsiToMuMu_JpsiPt8_Pythia8.root -> /eos/cms/store/group/phys_muon/TagAndProbe/Run2018/102X]"



hadd TnPTreeJPsi_17Sep2018_Charmonium_Run2018Av1_GoldenJSON.root \
/pnfs/knu.ac.kr/data/cms/store/user/kplee/Charmonium/crab_TnPTreeJPsi_v20190211_17Sep2018_Charmonium_Run2018Av1_GoldenJSON/190211_151909/0000/*.root
echo "[TnPTreeJPsi_17Sep2018_Charmonium_Run2018Av1_GoldenJSON.root] is produced"

xrdcp TnPTreeJPsi_17Sep2018_Charmonium_Run2018Av1_GoldenJSON.root root://eoscms.cern.ch//eos/cms/store/group/phys_muon/TagAndProbe/Run2018/102X
echo "[xrdcp is finished: TnPTreeJPsi_17Sep2018_Charmonium_Run2018Av1_GoldenJSON.root -> /eos/cms/store/group/phys_muon/TagAndProbe/Run2018/102X]"



hadd TnPTreeJPsi_17Sep2018_Charmonium_Run2018Bv1_GoldenJSON.root \
/pnfs/knu.ac.kr/data/cms/store/user/kplee/Charmonium/crab_TnPTreeJPsi_v20190211_17Sep2018_Charmonium_Run2018Bv1_GoldenJSON/190211_151925/0000/*.root
echo "[TnPTreeJPsi_17Sep2018_Charmonium_Run2018Bv1_GoldenJSON.root] is produced"

xrdcp TnPTreeJPsi_17Sep2018_Charmonium_Run2018Bv1_GoldenJSON.root root://eoscms.cern.ch//eos/cms/store/group/phys_muon/TagAndProbe/Run2018/102X
echo "[xrdcp is finished: TnPTreeJPsi_17Sep2018_Charmonium_Run2018Bv1_GoldenJSON.root -> /eos/cms/store/group/phys_muon/TagAndProbe/Run2018/102X]"



hadd TnPTreeJPsi_17Sep2018_Charmonium_Run2018Cv1_GoldenJSON.root \
/pnfs/knu.ac.kr/data/cms/store/user/kplee/Charmonium/crab_TnPTreeJPsi_v20190211_17Sep2018_Charmonium_Run2018Cv1_GoldenJSON/190211_151940/0000/*.root
echo "[TnPTreeJPsi_17Sep2018_Charmonium_Run2018Cv1_GoldenJSON.root] is produced"

xrdcp TnPTreeJPsi_17Sep2018_Charmonium_Run2018Cv1_GoldenJSON.root root://eoscms.cern.ch//eos/cms/store/group/phys_muon/TagAndProbe/Run2018/102X
echo "[xrdcp is finished: TnPTreeJPsi_17Sep2018_Charmonium_Run2018Cv1_GoldenJSON.root -> /eos/cms/store/group/phys_muon/TagAndProbe/Run2018/102X]"



hadd TnPTreeJPsi_Charmonium_Run2018Dv2_GoldenJSON.root \
/pnfs/knu.ac.kr/data/cms/store/user/kplee/Charmonium/crab_TnPTreeJPsi_v20190211_Charmonium_Run2018Dv2_GoldenJSON/190211_151958/0000/*.root
echo "[TnPTreeJPsi_Charmonium_Run2018Dv2_GoldenJSON.root] is produced"

xrdcp TnPTreeJPsi_Charmonium_Run2018Dv2_GoldenJSON.root root://eoscms.cern.ch//eos/cms/store/group/phys_muon/TagAndProbe/Run2018/102X
echo "[xrdcp is finished: TnPTreeJPsi_Charmonium_Run2018Dv2_GoldenJSON.root -> /eos/cms/store/group/phys_muon/TagAndProbe/Run2018/102X]"



echo "All jobs are finished"
