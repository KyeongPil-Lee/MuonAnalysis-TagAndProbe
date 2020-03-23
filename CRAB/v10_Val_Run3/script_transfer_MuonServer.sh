#!/bin/bash

rsync -avz --progress -e 'ssh -p 50001' \
/u/user/kplee/SE_UserHome/DYToLL_M-50_TuneCP5_14TeV-pythia8/crab_TnPTreeZ_v20200323_DYLL_M50_Pythia8_FlatPU30to80_Winter20/*/*/ \
kplee@147.47.50.161:/scratch/kplee/TagProbe/TnPTree/2020/Run3/TnPTreeZ_DYLL_M50_Pythia8_FlatPU30to80_Winter20

echo "hadd: start"
ssh -p 50001 kplee@147.47.50.161 "hadd /scratch/kplee/TagProbe/TnPTree/2020/Run3/TnPTreeZ_DYLL_M50_Pythia8_FlatPU30to80_Winter20.root /scratch/kplee/TagProbe/TnPTree/2020/Run3/TnPTreeZ_DYLL_M50_Pythia8_FlatPU30to80_Winter20/*.root"
echo "hadd: done"
echo "**************"