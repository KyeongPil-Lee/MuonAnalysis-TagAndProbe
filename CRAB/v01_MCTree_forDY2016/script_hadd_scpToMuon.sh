#!bin/bash

hadd TnPTreeZ_Summer16_DYLL_M50_aMCNLO.root \
/u/user/kplee/SE_UserHome/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/crab_TnPTreeZ_v20181028_DYLL_M50_aMCNLO/181028_210606/0000/*.root \
/u/user/kplee/SE_UserHome/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/crab_TnPTreeZ_v20181028_DYLL_M50_aMCNLO/181028_210606/0001/*.root \
/u/user/kplee/SE_UserHome/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/crab_TnPTreeZ_v20181028_DYLL_M50_aMCNLO/181028_210606/0002/*.root \
/u/user/kplee/SE_UserHome/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/crab_TnPTreeZ_v20181028_DYLL_M50_aMCNLO/181028_210606/0003/*.root

echo "hadd: finished"

scp -P 50001 TnPTreeZ_Summer16_DYLL_M50_aMCNLO.root kplee@147.47.50.161:/scratch/kplee/TagProbe/TnPTree/2016

echo "scp: finished"
