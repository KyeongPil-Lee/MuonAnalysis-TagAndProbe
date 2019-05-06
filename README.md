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

git cms-addpkg MuonAnalysis/MuonAssociators

vi MuonAnalysis/MuonAssociators/python/patMuonsWithTrigger_cff.py
# -- add several lines by following the section below ("Update of patMuonsWithTrigger_cff.py")

scram b -j 4 >&scram.log&
tail -f scram.log
```





### Update of patMuonsWithTrigger_cff.py

Several lines should be added & updated to make patMuonsWithTrigger be able to recognize OldMu100

1) Below

```
patTrigger = cms.EDProducer("TriggerObjectFilterByCollection",
    src = cms.InputTag("patTriggerFull"),
    collections = cms.vstring("hltL1extraParticles", "hltGmtStage2Digis", "hltL2MuonCandidates", "hltIterL3MuonCandidates","hltIterL3FromL2MuonCandidates","hltHighPtTkMuonCands", "hltGlbTrkMuonCands", "hltMuTrackJpsiCtfTrackCands", "hltMuTrackJpsiEffCtfTrackCands", "hltMuTkMuJpsiTrackerMuonCands","hltTracksIter"),
)
```

, add the line:

```
patTrigger.collections.append( "hltOldL3MuonCandidates" ) # -- for OldMu100
```



2) below

```
muonMatchHLTL3 = muonTriggerMatchHLT.clone(matchedCuts = cms.string('coll("hltIterL3MuonCandidates")'), maxDeltaR = 0.1, maxDPtRel = 10.0)
```

, add the line:

```
muonMatchHLTOldL3 = muonTriggerMatchHLT.clone(matchedCuts = cms.string('coll("hltOldL3MuonCandidates")'), maxDeltaR = 0.1, maxDPtRel = 10.0)
```



3) Update ```patTriggerMatchers1Mu``` by:

```
patTriggerMatchers1Mu = cms.Sequence(
      #muonMatchHLTL1 +   # keep off by default, since it is slow and usually not needed
      muonMatchHLTL2 +
      muonMatchHLTL3 +
      muonMatchHLTOldL3 +
      muonMatchHLTL3T +
      muonMatchHLTL3fromL2 +
      muonMatchHLTTkMu
)
```



4) Update ```patTriggerMatchers1MuInputTags``` by:

```
patTriggerMatchers1MuInputTags = [
    #cms.InputTag('muonMatchHLTL1','propagatedReco'), # fake, will match if and only if he muon did propagate to station 2
    #cms.InputTag('muonMatchHLTL1'),
    cms.InputTag('muonMatchHLTL2'),
    cms.InputTag('muonMatchHLTL3'),
    cms.InputTag('muonMatchHLTOldL3'),
    cms.InputTag('muonMatchHLTL3T'),
    cms.InputTag('muonMatchHLTL3fromL2'),
    cms.InputTag('muonMatchHLTTkMu'),
]
```



5) Below

```
process.muonMatchHLTL3.resolveAmbiguities = False
```

, add the line

```
process.muonMatchHLTOldL3.resolveAmbiguities = False
```

