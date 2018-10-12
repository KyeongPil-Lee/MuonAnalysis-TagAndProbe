# TnP Production for CMSMUONS-192

* Reference: https://its.cern.ch/jira/browse/CMSMUONS-192



## Dataset

### Data

* JSON

  ```
  /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/13TeV/PromptReco/Cert_314472-323523_13TeV_PromptReco_Collisions18_JSON.txt
  ```

* Z tree

  * /SingleMuon/Run2018C-PromptReco-v3/AOD
    * 319852 to end: already produced, but not transferred
      * crab_TnPTreeZ_v20180904_SingleMuon_Run2018Cv3_GoldenJSON_from319852ToEnd
  * /SingleMuon/Run2018D-PromptReco-v2/AOD (from start to 323523)

* J/Psi tree

  * /Charmonium/Run2018D-PromptReco-v2/AOD (from 321222 to 323523)



### Recipe

```
# -- if lxplus:
cd /afs/cern.ch/user/k/kplee/work/private/MuonPOGTnP/CMSSW

cmsrel CMSSW_10_2_3
cd CMSSW_10_2_3/src
cmsenv

git cms-merge-topic HuguesBrun:updateL3MuonCollectionsToMatch
git clone git@github.com:KyeongPil-Lee/MuonAnalysis-TagAndProbe.git MuonAnalysis/TagAndProbe -b 101X
git cms-addpkg PhysicsTools/PatAlgos

vi PhysicsTools/PatAlgos/plugins/PATMuonProducer.cc
# -- change the line:
# -- bool simInfoIsAvailalbe = iEvent.getByToken(simInfo_,simInfo); ->
# -- simInfoIsAvailalbe=false;

scram b -j 4 >&scram.log&
tail -f scram.log

cd MuonAnalysis/TagAndProbe/CRAB/v01_CMSMUONS192

```

