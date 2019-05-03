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
* New code: ```plugins/MuonHighPt.cc```
  * Module for adding new high-pT ID
    * Backported from 102X branch
* Updated code: ```python/common_modules.py```, ```test/zmumu/tp_from_aod_data.py```, ```test/zmumu/tp_from_aod_MC.py```
  * Add new high-pT muon ID variable to tag and probe, respectively
  * Set global tags & input files accordingly (legacy rereco)



## Recipe

```
cmsrel CMSSW_8_0_29 # where the legacy rereco samples are produced
cd CMSSW_8_0_29/src/
cmsenv

# -- add expectedNnumberOfMatchedStations variable to muon object (for new high pT ID)
git cms-addpkg DataFormats/MuonReco
vi DataFormats/MuonReco/interface/Muon.h
# -- add the line: https://github.com/cms-sw/cmssw/blob/CMSSW_10_2_X/DataFormats/MuonReco/interface/Muon.h#L247

vi DataFormats/MuonReco/src/Muon.cc
# -- add the lines: https://github.com/cms-sw/cmssw/blob/CMSSW_10_2_X/DataFormats/MuonReco/src/Muon.cc#L136-L153

git clone git@github.com:KyeongPil-Lee/MuonAnalysis-TagAndProbe.git  MuonAnalysis/TagAndProbe -b  80X-v6.1

scram b -j 4 >&scram.log&
tail -f scram.log
```



