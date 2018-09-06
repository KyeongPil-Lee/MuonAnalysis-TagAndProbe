## Motivation

To monitor the trigger efficiency in 2018



## Dataset

```
/SingleMuon/Run2018C-PromptReco-v3/AOD # -- only from 319852 to end
/SingleMuon/Run2018D-PromptReco-v2/AOD
```



* JSON
  * Cert_314472-321461_13TeV_PromptReco_Collisions18_JSON.txt
    * RunC, v3
    * RunD, v2 (up to 321461)
  * /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/13TeV/DCSOnly/json_DCSONLY.txt
    * RunD, v2 (321462 - 322068) (06 Sep.)

* Global tag
  * RunC v3: 101X_dataRun2_Prompt_v11
  * RunD v2: 102X_dataRun2_Prompt_v4



* CMSSW
  * RunC v3: CMSSW_10_1_9_patch1
  * RunD v2: CMSSW_10_2_1



## CRAB status check

```
cd /afs/cern.ch/user/k/kplee/work/private/MuonPOGTnP/CMSSW/CMSSW_10_1_9_patch1/src/MuonAnalysis/TagAndProbe/test/zmumu/CRAB/v01/CRABDir
crab status crab_TnPTreeZ_v20180904_SingleMuon_Run2018Cv3_GoldenJSON_from319852ToEnd

cd /afs/cern.ch/user/k/kplee/work/private/MuonPOGTnP/CMSSW/CMSSW_10_2_1/src/MuonAnalysis/TagAndProbe/test/zmumu/CRAB/v01/CRABDir
crab status crab_TnPTreeZ_v20180904_SingleMuon_Run2018Dv2_GoldenJSON_Upto321461
```



