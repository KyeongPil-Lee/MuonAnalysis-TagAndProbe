from MuonAnalysis.TagAndProbe.ROOTFileTransfer import *

tool = TransferTool()
tool.user = 'kplee'
tool.host = '147.47.50.161'
tool.port = 50001
tool.do_hadd = True

path_preVFP  = GetCRABOutputDir("crab_TnPTreeZ_v20200331_RelValZMM_13UP16_UL16_HighStat_L1Fix_preFVP")
path_postVFP = GetCRABOutputDir("crab_TnPTreeZ_v20200331_RelValZMM_13UP16_UL16_HighStat_L1Fix_postFVP")

tool.dic_input_to_mergedFileName = {
    path_preVFP  : "TnPTreeZ_RelValZMM_13UP16_UL16_HighStat_L1FixMarch_preVFP.root",
    path_postVFP : "TnPTreeZ_RelValZMM_13UP16_UL16_HighStat_L1FixMarch_postVFP.root",
}

tool.dic_input_to_outputPath = {
    path_preVFP  : "/scratch/kplee/TagProbe/TnPTree/2020",
    path_postVFP : "/scratch/kplee/TagProbe/TnPTree/2020",
}
tool.Transfer()


# -- test
# tool.dic_input_to_mergedFileName = {
#     '/pnfs/knu.ac.kr/data/cms/store/user/kplee/RelValZMM_13UP16/crab_TnPTreeZ_v20200331_RelValZMM_13UP16_UL16_HighStat_L1Fix_preFVP' : "TnPTreeZ_RelValZMM_13UP16_UL16_HighStat_L1FixMarch_preVFP.root",
# }

# tool.dic_input_to_outputPath = {
#     '/pnfs/knu.ac.kr/data/cms/store/user/kplee/RelValZMM_13UP16/crab_TnPTreeZ_v20200331_RelValZMM_13UP16_UL16_HighStat_L1Fix_preFVP' : "/home/kplee/Temp/preVFP",
# }
# tool.Transfer()