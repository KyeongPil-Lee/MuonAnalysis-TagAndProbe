# TnP tree for UL16 validation

GT for correct samples

```
106X_mcRun2_asymptotic_v11
106X_mcRun2_asymptotic_preVFP_v5
```

GT for wrong samples

```
106X_mcRun2_asymptotic_v10
106X_mcRun2_asymptotic_preVFP_v3
```



## Sample

* Reference: 
  * preVFP: https://dmytro.web.cern.ch/dmytro/cmsprodmon/workflows.php?prep_id=CMSSW_10_6_8__UL16hltval_preVFP_v5-1581427861-ZMM_13UP16
  * postVFP: https://dmytro.web.cern.ch/dmytro/cmsprodmon/workflows.php?prep_id=CMSSW_10_6_8__UL16hltval_postVFP_v11-1581436204-ZMM_13UP16



**preVFP**

```
/RelValZMM_13UP16/CMSSW_10_6_8-PU25ns_106X_mcRun2_asymptotic_preVFP_v5_UL16hltval_preVFP_v5-v1/AODSIM
```

* Example file

  ```
  /store/relval/CMSSW_10_6_8/RelValZMM_13UP16/AODSIM/PU25ns_106X_mcRun2_asymptotic_preVFP_v5_UL16hltval_preVFP_v5-v1/10000/9801AEB1-310A-8044-9550-FB3EC43A7022.root
  ```



**postVFP**

```
/RelValZMM_13UP16/CMSSW_10_6_8-PU25ns_106X_mcRun2_asymptotic_v11_UL16hltval_postVFP_v11-v1/AODSIM
```





Wrong sample (preVFP) (just for x-check)

```
/RelValZMM_13UP16/CMSSW_10_6_8-PU25ns_106X_mcRun2_asymptotic_preVFP_v3_UL16hltval_preVFP-v1/AODSIM
```



### Working area (lxplus)

```
/afs/cern.ch/user/k/kplee/work/private/MuonPOGTnP/CMSSW_slc7/CMSSW_10_6_8/src/MuonAnalysis/TagAndProbe
```



Test run

```
cd /afs/cern.ch/user/k/kplee/work/private/MuonPOGTnP/CMSSW_slc7/CMSSW_10_6_8/src/MuonAnalysis/TagAndProbe/test/zmumu
cmsenv
voms-proxy-init --voms cms

cmsRun tp_from_aod_MC_arg.py \
globalTag=106X_mcRun2_asymptotic_preVFP_v5 \
inputFile=/store/relval/CMSSW_10_6_8/RelValZMM_13UP16/AODSIM/PU25ns_106X_mcRun2_asymptotic_preVFP_v5_UL16hltval_preVFP_v5-v1/10000/9801AEB1-310A-8044-9550-FB3EC43A7022.root \
>&tp_from_aod_MC_arg.log&
tail -f tp_from_aod_MC_arg.log
```



CRAB directory

```
cd /afs/cern.ch/user/k/kplee/work/private/MuonPOGTnP/CMSSW_slc7/CMSSW_10_6_8/src/MuonAnalysis/TagAndProbe/CRAB/v09_Val_UL16/CRABDir
crab status crab_TnPTreeZ_v20200219_RelValZMM_13UP16_UL16_HighStat_v2
crab status crab_TnPTreeZ_v20200219_RelValZMM_13UP16_UL16_HighStat_WrongL1_v2
```

* ```config.Data.allowNonValidInputDataset = True``` is used (19th Feb. 2020)