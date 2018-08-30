### Dataset

* [DAS link](https://cmsweb.cern.ch/das/request?view=list&limit=50&instance=prod%2Fglobal&input=%2FCharmonium%2FRun2018*-PromptReco-v*%2FAOD)

```
/Charmonium/Run2018A-PromptReco-v1/AOD
/Charmonium/Run2018A-PromptReco-v2/AOD 
/Charmonium/Run2018A-PromptReco-v3AOD
/Charmonium/Run2018B-PromptReco-v1/AOD
/Charmonium/Run2018B-PromptReco-v2/AOD
/Charmonium/Run2018C-PromptReco-v1/AOD
/Charmonium/Run2018C-PromptReco-v2/AOD
/Charmonium/Run2018C-PromptReco-v3/AOD
/Charmonium/Run2018D-PromptReco-v2/AOD
```

* Global tags
  * 101X_dataRun2_Prompt_v9
    * RunA-v1, v2
  * 101X_dataRun2_Prompt_v10
    * RunA-v3, RunB-v1
  * 101X_dataRun2_Prompt_v11
    * RunB-v2, RunC-v1,v2,v3
  * RunD, v2: 102X_dataRun2_Prompt_v4



* The latest CMSSW
  * CMSSW_10_1_9
    * RunC-v3 and below
  * CMSSW_10_2_1
    * RunD-v2

### JSON

```
/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/13TeV/PromptReco/Cert_314472-321221_13TeV_PromptReco_Collisions18_JSON.txt
```



### CRAB status check

* 101X

  ```
  cd /afs/cern.ch/user/k/kplee/work/private/MuonPOGTnP/CMSSW/CMSSW_10_1_9_patch1/src/MuonAnalysis/TagAndProbe/test/jpsi/CRAB/v01/CRABDir
  
  # crab status crab_TnPTreeJPsi_v20180828_Charmonium_Run2018Av1_GoldenJSON;
  # crab status crab_TnPTreeJPsi_v20180828_Charmonium_Run2018Av2_GoldenJSON;
  # crab status crab_TnPTreeJPsi_v20180828_Charmonium_Run2018Av3_GoldenJSON;
  # crab status crab_TnPTreeJPsi_v20180828_Charmonium_Run2018Bv1_GoldenJSON;
  # crab status crab_TnPTreeJPsi_v20180828_Charmonium_Run2018Bv2_GoldenJSON;
  # crab status crab_TnPTreeJPsi_v20180828_Charmonium_Run2018Cv1_GoldenJSON;
  # crab status crab_TnPTreeJPsi_v20180828_Charmonium_Run2018Cv2_GoldenJSON;
  # crab status crab_TnPTreeJPsi_v20180828_Charmonium_Run2018Cv3_GoldenJSON;
  ```

* 102X

  ```
  cd /afs/cern.ch/user/k/kplee/work/private/MuonPOGTnP/CMSSW/CMSSW_10_2_1/src/MuonAnalysis/TagAndProbe/test/jpsi/CRAB/v01/CRABDir
  # crab status crab_TnPTreeJPsi_v20180828_Charmonium_Run2018Dv2_GoldenJSON_Upto321221
  ```

* All of them are finished (within 1 days)



### Transferring

```
python genScript_mergeAndTrasnferToEOS.py
source script_mergeAndTrasnferToEOS.sh >&script_mergeAndTrasnferToEOS.log&
```



### Fix typo

Remove "v20180828" in the tree name



