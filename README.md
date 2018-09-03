# TnP tree producer

Starting point: cms-analysis/MuonAnalysis-TagAndProbe (80X-v6)

```
git clone https://github.com/cms-analysis/MuonAnalysis-TagAndProbe.git  MuonAnalysis/TagAndProbe -b  80X-v6
```

Updates from 80X-v6

* New code: ```test/jpsi/tp_from_aod_simple_Data/MC_v2.py```, 
  * Changes from ```tp_from_aod_simple_Data/MC.py```
    * Include ```TrackQualityFlags``` and ```MuonIDFlags```  in ```tagFlags```
    * Update global tags & input files accordingly (for legacy rereco datasets)
    * Details: https://its.cern.ch/jira/browse/CMSMUONS-148



## Recipe

```
cmsrel CMSSW_8_0_29 # where the legacy rereco samples are produced
cd CMSSW_8_0_29/src/
cmsenv

git clone git@github.com:KyeongPil-Lee/MuonAnalysis-TagAndProbe.git  MuonAnalysis/TagAndProbe -b  80X-v6.1

scram b -j 4 >&scram.log&
tail -f scram.log
```



