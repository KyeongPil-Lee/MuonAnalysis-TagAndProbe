# TnP tree producer

Starting point: cms-analysis/MuonAnalysis-TagAndProbe (80X-v6)

```
git clone https://github.com/cms-analysis/MuonAnalysis-TagAndProbe.git  MuonAnalysis/TagAndProbe -b  80X-v6
```

Updates from 80X-v6

* New code: test/jpsi/tp_from_aod_simple_Data_v2.py
  * Changes from tp_from_aod_simple_Data.py
    * Include ```TrackQualityFlags``` and ```MuonIDFlags```  in ```tagFlags```
    * Details: https://its.cern.ch/jira/browse/CMSMUONS-148



