# TnP tree producer

* Copy of:

  ```
  git clone git@github.com:sscruz/Tnp94.git MuonAnalysis/TagAndProbe -b 94_newSelector
  ```



## Recipe

```
cmsrel CMSSW_10_2_5
cd CMSSW_10_2_5/src
cmsenv

git cms-merge-topic HuguesBrun:updateL3MuonCollectionsToMatch
git clone git@github.com:KyeongPil-Lee/MuonAnalysis-TagAndProbe.git MuonAnalysis/TagAndProbe -b 102X
git cms-addpkg PhysicsTools/PatAlgos

vi PhysicsTools/PatAlgos/plugins/PATMuonProducer.cc
# -- change the line:
# -- bool simInfoIsAvailalbe = iEvent.getByToken(simInfo_,simInfo); ->
# -- simInfoIsAvailalbe=false;

scram b -j 4 >&scram.log&
tail -f scram.log
```

