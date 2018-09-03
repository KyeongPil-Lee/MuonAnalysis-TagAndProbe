## Motivation

Reproduction of J/Psi TnP trees (2016 legacy rereco) with ID flag for the tag

Details: https://its.cern.ch/jira/browse/CMSMUONS-148



## Dataset

### Data

```
/Charmonium/Run2016B-07Aug17_ver2-v1/AOD
/Charmonium/Run2016C-07Aug17-v1/AOD
/Charmonium/Run2016D-07Aug17-v1/AOD
/Charmonium/Run2016E-07Aug17-v1/AOD
/Charmonium/Run2016F-07Aug17-v1/AOD
/Charmonium/Run2016G-07Aug17-v1/AOD
/Charmonium/Run2016H-07Aug17-v1/AOD
```

* **JSON**

  ```
  /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/ReReco/Final/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt
  ```

* **Global tag**: 80X_dataRun2_2016LegacyRepro_v4
  * for all samples

* **CMSSW**: CMSSW_8_0_29



### MC

```
/JpsiToMuMu_JpsiPt8_TuneCUEP8M1_13TeV-pythia8/RunIISpring16DR80-PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/AODSIM
```

* **Global tag**: 80X_mcRun2_asymptotic_2016_v3
* **CMSSW**: sample is produced under CMSSW_8_0_3_patch2
  * But ntple production is under CMSSW_8_0_29 (same with Legacy rereco data)



## CRAB

### Status check

```
cd /afs/cern.ch/user/k/kplee/work/private/MuonPOGTnP/CMSSW/CMSSW_8_0_29/src/MuonAnalysis/TagAndProbe/test/jpsi/CRAB/v01/TagProbe

crab status crab_TagProbe_v20180903_LegacyRerecoWithIDFlag_Charmonium_Run2016Bver2_GoldenJSON;
crab status crab_TagProbe_v20180903_LegacyRerecoWithIDFlag_Charmonium_Run2016C_GoldenJSON;
crab status crab_TagProbe_v20180903_LegacyRerecoWithIDFlag_Charmonium_Run2016D_GoldenJSON;
crab status crab_TagProbe_v20180903_LegacyRerecoWithIDFlag_Charmonium_Run2016E_GoldenJSON;
crab status crab_TagProbe_v20180903_LegacyRerecoWithIDFlag_Charmonium_Run2016F_GoldenJSON;
crab status crab_TagProbe_v20180903_LegacyRerecoWithIDFlag_Charmonium_Run2016G_GoldenJSON;
crab status crab_TagProbe_v20180903_LegacyRerecoWithIDFlag_Charmonium_Run2016H_GoldenJSON;
crab status crab_TagProbe_v20180903_LegacyRerecoWithIDFlag_JpsiToMuMu_JpsiPt8_Pythia8;
```



## Troubleshooting

### Error in CRAB

* Dashboard: [link](http://dashb-cms-job.cern.ch/dashboard/templates/task-analysis/#user=kplee&refresh=0&table=Jobs&p=1&records=25&activemenu=2&status=&site=&tid=180830_090632%3Akplee_crab_TagProbe_v20180830_LegacyRerecoWithIDFlag_Charmonium_Run2016G_GoldenJSON)

```
== CMSSW: ----- Begin Fatal Exception 30-Aug-2018 09:14:10 UTC-----------------------
== CMSSW: An exception of category 'DictionaryNotFound' occurred while
== CMSSW:    [0] Constructing the EventProcessor
== CMSSW:    [1] Constructing module: class=PATTriggerProducer label='patTriggerFull'
== CMSSW: Exception Message:
== CMSSW: No Dictionary for class: 'edm::DetSetVector<CTPPSDiamondDigi>'
== CMSSW: ----- End Fatal Exception -------------------------------------------------
```

* Change the global tag
  * 80X_dataRun2_2016LegacyRepro_v4: no change
* Change the CMSSW version
  * 8_0_25 -> 8_0_29: **it works!**

