#!/bin/bash

cd /afs/cern.ch/user/k/kplee/work/private/MuonPOGTnP/CMSSW_slc7/CMSSW_10_6_11_CANDIDATE3/src

cmsenv

git cms-merge-topic HuguesBrun:updateL3MuonCollectionsToMatch
git clone git@github.com:KyeongPil-Lee/MuonAnalysis-TagAndProbe.git MuonAnalysis/TagAndProbe -b 102X
git cms-addpkg PhysicsTools/PatAlgos

vi PhysicsTools/PatAlgos/plugins/PATMuonProducer.cc
# -- change the line:
# -- bool simInfoIsAvailalbe = iEvent.getByToken(simInfo_,simInfo); ->
# -- bool simInfoIsAvailalbe=false;

git cms-addpkg MuonAnalysis/MuonAssociators

cp /afs/cern.ch/user/k/kplee/work/private/MuonPOGTnP/CMSSW_slc7/CMSSW_10_6_8/src/MuonAnalysis/MuonAssociators/python/patMuonsWithTrigger_cff.py \
MuonAnalysis/MuonAssociators/python/patMuonsWithTrigger_cff.py

scram b -j 4 >&scram.log&
tail -f scram.log

# -- test
cmsRun tp_from_aod_MC_arg.py \
globalTag=106X_mcRun2_asymptotic_v12 \
inputFile=/store/relval/CMSSW_10_6_11_CANDIDATE3/RelValZMM_13UP16/AODSIM/PU25ns_106X_mcRun2_asymptotic_v12_hltul16_post-v1/10000/FF3E17D6-17BC-5F47-A6C7-4D5256735124.root \
>&tp_from_aod_MC_arg.log&