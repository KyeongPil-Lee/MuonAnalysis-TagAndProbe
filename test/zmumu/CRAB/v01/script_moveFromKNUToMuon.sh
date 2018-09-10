#!bin/bash

hadd TnPTreeZ_SingleMuon_Run2018Cv3_GoldenJSON_from319852ToEnd.root \
/pnfs/knu.ac.kr/data/cms/store/user/kplee/SingleMuon/crab_TnPTreeZ_v20180904_SingleMuon_Run2018Cv3_GoldenJSON_from319852ToEnd/180904_093401/0000/*.root

hadd TnPTreeZ_SingleMuon_Run2018Dv2_GoldenJSON_Upto321461.root \
/pnfs/knu.ac.kr/data/cms/store/user/kplee/SingleMuon/crab_TnPTreeZ_v20180904_SingleMuon_Run2018Dv2_GoldenJSON_Upto321461/180904_093517/0000/*.root \
/pnfs/knu.ac.kr/data/cms/store/user/kplee/SingleMuon/crab_TnPTreeZ_v20180904_SingleMuon_Run2018Dv2_GoldenJSON_Upto321461/180904_093517/0001/*.root

hadd TnPTreeZ_SingleMuon_Run2018Dv2_DCSOnly_321462_to_322068.root \
/pnfs/knu.ac.kr/data/cms/store/user/kplee/SingleMuon/crab_TnPTreeZ_v20180906_SingleMuon_Run2018Dv2_DCSOnly_321462_to_322068/180906_174333/0000/*.root \
/pnfs/knu.ac.kr/data/cms/store/user/kplee/SingleMuon/crab_TnPTreeZ_v20180906_SingleMuon_Run2018Dv2_DCSOnly_321462_to_322068/180906_174333/0001/*.root

echo "hadd: finished"

scp -P 50001 TnPTreeZ_SingleMuon_Run2018Cv3_GoldenJSON_from319852ToEnd.root kplee@147.47.50.161:/scratch/kplee/TagProbe/101X
scp -P 50001 TnPTreeZ_SingleMuon_Run2018Dv2_GoldenJSON_Upto321461.root kplee@147.47.50.161:/scratch/kplee/TagProbe/101X
scp -P 50001 TnPTreeZ_SingleMuon_Run2018Dv2_DCSOnly_321462_to_322068.root kplee@147.47.50.161:/scratch/kplee/TagProbe/101X

echo "scp: finished"

