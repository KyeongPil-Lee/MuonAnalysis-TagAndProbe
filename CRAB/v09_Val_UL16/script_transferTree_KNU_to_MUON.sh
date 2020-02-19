#!bin/bash

echo "**************"
echo "Correct sample"
rsync -avz --progress -e 'ssh -p 50001' \
/u/user/kplee/SE_UserHome/SingleMuon/crab_TnPTreeZ_v20200219_RelValZMM_13UP16_UL16_HighStat/*/*/*.root \
kplee@147.47.50.161:/scratch/kplee/TagProbe/TnPTree/2020

echo "transfer: finished"

echo "hadd: start"
ssh -p 50001 kplee@147.47.50.161 "hadd /scratch/kplee/TagProbe/TnPTree/2020/TnPTreeZ_RelValZMM_13UP16_UL16_HighStat.root /scratch/kplee/TagProbe/TnPTree/2020/*.root"
echo "hadd: done"
echo "**************"

echo "**************"
echo "Wrong sample"
rsync -avz --progress -e 'ssh -p 50001' \
/u/user/kplee/SE_UserHome/SingleMuon/crab_TnPTreeZ_v20200219_RelValZMM_13UP16_UL16_HighStat_WrongL1/*/*/*.root \
kplee@147.47.50.161:/scratch/kplee/TagProbe/TnPTree/2020/UL16_WrongL1

echo "transfer: finished"

echo "hadd: start"
ssh -p 50001 kplee@147.47.50.161 "hadd /scratch/kplee/TagProbe/TnPTree/2020/TnPTreeZ_RelValZMM_13UP16_UL16_HighStat_WrongL1.root /scratch/kplee/TagProbe/TnPTree/2020/UL16_WrongL1/*.root"
echo "hadd: done"
echo "**************"
