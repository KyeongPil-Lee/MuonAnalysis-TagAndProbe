# TnP Tree Producer

C++/python codes are not changed from https://github.com/GLP90/Tnp94 (94_newSelector branch)

* Same with 94_pre3 recipe in the [twiki](https://twiki.cern.ch/twiki/bin/viewauth/CMS/MuonTagAndProbeTreesRun2#Current_working_recipe_94X)



To keep all CRAB configuration to be submitted



## Recipe

```
cmsrel CMSSW_10_1_9_patch1
cd CMSSW_10_1_9_patch1/src
cmsenv

git cms-merge-topic HuguesBrun:updateL3MuonCollectionsToMatch
git clone git@github.com:KyeongPil-Lee/Tnp94.git MuonAnalysis/TagAndProbe -b 101X
git cms-addpkg PhysicsTools/PatAlgos

vi PhysicsTools/PatAlgos/plugins/PATMuonProducer.cc
# -- change the line:
# -- bool simInfoIsAvailalbe = iEvent.getByToken(simInfo_,simInfo); ->
# -- simInfoIsAvailalbe=false;

scram b -j 4 >&scram.log&
tail -f scram.log
```

