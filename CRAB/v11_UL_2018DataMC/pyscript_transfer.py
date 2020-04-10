from MuonAnalysis.TagAndProbe.ROOTFileTransfer import *

tool = TransferTool()
tool.user = 'kplee'
tool.host = 'lxplus.cern.ch'
tool.port = 22
tool.do_hadd = False

tool.dic_input_to_outputPath = {
    # GetCRABOutputDir("crab_TnPTreeZ_v20200324_12Nov2019_SingleMuon_Run2018A_GoldenJSON")  : "/eos/cms/store/group/phys_muon/TagAndProbe/ULRereco/2018/102X/SingleMuon_Run2018A_98Percent",
    # GetCRABOutputDir("crab_TnPTreeZ_v20200324_12Nov2019_SingleMuon_Run2018B_GoldenJSON") : "/eos/cms/store/group/phys_muon/TagAndProbe/ULRereco/2018/102X/SingleMuon_Run2018B_80Percent",
    # "/pnfs/knu.ac.kr/data/cms/store/user/kplee/SingleMuon/crab_TnPTreeZ_v20200324_12Nov2019_SingleMuon_Run2018D_GoldenJSON" : "/eos/cms/store/group/phys_muon/TagAndProbe/ULRereco/2018/102X/SingleMuon_Run2018D_98Percent",

    # "/u/user/kplee/SE_UserHome/SingleMuon/crab_TnPTreeZ_v20200404_12Nov2019_SingleMuon_Run2018B_GoldenJSON" : "/eos/cms/store/group/phys_muon/TagAndProbe/ULRereco/2018/102X/SingleMuon_Run2018B_80Percent",

    "/u/user/kplee/SE_UserHome/SingleMuon/crab_TnPTreeZ_v20200404_12Nov2019_SingleMuon_Run2018A_GoldenJSON" : "/eos/cms/store/group/phys_muon/TagAndProbe/ULRereco/2018/102X/SingleMuon_Run2018A_98Percent",
    "/u/user/kplee/SE_UserHome/SingleMuon/crab_TnPTreeZ_v20200406_12Nov2019_SingleMuon_Run2018D_GoldenJSON" : "/eos/cms/store/group/phys_muon/TagAndProbe/ULRereco/2018/102X/SingleMuon_Run2018D_98Percent",}

tool.Transfer()


# path_preVFP  = GetCRABOutputDir("crab_TnPTreeZ_v20200324_12Nov2019_SingleMuon_Run2018A_GoldenJSON")
# path_postVFP = GetCRABOutputDir("crab_TnPTreeZ_v20200324_12Nov2019_SingleMuon_Run2018B_GoldenJSON")

# tool.dic_input_to_mergedFileName = {
#     path_preVFP  : "dummay.root",
#     path_postVFP : "TnPTreeZ_RelValZMM_13UP16_UL16_HighStat_L1FixMarch_postVFP.root",
# }

# tool.dic_input_to_outputPath = {
#     path_preVFP  : "/scratch/kplee/TagProbe/TnPTree/2020",
#     path_postVFP : "/scratch/kplee/TagProbe/TnPTree/2020",
# }
# tool.Transfer()