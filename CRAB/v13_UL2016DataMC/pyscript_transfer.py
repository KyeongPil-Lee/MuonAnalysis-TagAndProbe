from MuonAnalysis.TagAndProbe.ROOTFileTransfer import *

tool = TransferTool()
tool.user = 'kplee'
tool.host = 'lxplus.cern.ch'
tool.port = 22
tool.do_hadd = False

tool.dic_input_to_outputPath = {
    "/u/user/kplee/SE_UserHome/SingleMuon/crab_TnPTreeZ_v20200609_21Feb2020_SingleMuon_Run2016Bver2_HIPM_GoldenJSON" : "/eos/cms/store/group/phys_muon/TagAndProbe/ULRereco/2016/102X/SingleMuon_Run2016Bver2_HIPM",
    "/u/user/kplee/SE_UserHome/SingleMuon/crab_TnPTreeZ_v20200609_21Feb2020_SingleMuon_Run2016C_HIPM_GoldenJSON"     : "/eos/cms/store/group/phys_muon/TagAndProbe/ULRereco/2016/102X/SingleMuon_Run2016C_HIPM",
    "/u/user/kplee/SE_UserHome/SingleMuon/crab_TnPTreeZ_v20200609_21Feb2020_SingleMuon_Run2016D_HIPM_GoldenJSON"     : "/eos/cms/store/group/phys_muon/TagAndProbe/ULRereco/2016/102X/SingleMuon_Run2016D_HIPM",
    "/u/user/kplee/SE_UserHome/SingleMuon/crab_TnPTreeZ_v20200609_21Feb2020_SingleMuon_Run2016E_HIPM_GoldenJSON"     : "/eos/cms/store/group/phys_muon/TagAndProbe/ULRereco/2016/102X/SingleMuon_Run2016E_HIPM",
    "/u/user/kplee/SE_UserHome/SingleMuon/crab_TnPTreeZ_v20200609_21Feb2020_SingleMuon_Run2016F_HIPM_GoldenJSON"     : "/eos/cms/store/group/phys_muon/TagAndProbe/ULRereco/2016/102X/SingleMuon_Run2016F_HIPM",
    "/u/user/kplee/SE_UserHome/SingleMuon/crab_TnPTreeZ_v20200609_21Feb2020_SingleMuon_Run2016F_GoldenJSON"          : "/eos/cms/store/group/phys_muon/TagAndProbe/ULRereco/2016/102X/SingleMuon_Run2016F",
    "/u/user/kplee/SE_UserHome/SingleMuon/crab_TnPTreeZ_v20200609_21Feb2020_SingleMuon_Run2016G_GoldenJSON"          : "/eos/cms/store/group/phys_muon/TagAndProbe/ULRereco/2016/102X/SingleMuon_Run2016G",
    "/u/user/kplee/SE_UserHome/SingleMuon/crab_TnPTreeZ_v20200609_21Feb2020_SingleMuon_Run2016H_GoldenJSON"          : "/eos/cms/store/group/phys_muon/TagAndProbe/ULRereco/2016/102X/SingleMuon_Run2016H",

    '/u/user/kplee/SE_UserHome/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/crab_TnPTreeZ_v20200609_UL16MC_DYJetsToLL_M50_Madgraph' : "/eos/cms/store/group/phys_muon/TagAndProbe/ULRereco/2016/102X/DY_M50_Madgraph",

    # GetCRABOutputDir("crab_TnPTreeZ_v20200324_12Nov2019_SingleMuon_Run2018A_GoldenJSON")  : "/eos/cms/store/group/phys_muon/TagAndProbe/ULRereco/2018/102X/SingleMuon_Run2018A_98Percent",
    # GetCRABOutputDir("crab_TnPTreeZ_v20200324_12Nov2019_SingleMuon_Run2018B_GoldenJSON") : "/eos/cms/store/group/phys_muon/TagAndProbe/ULRereco/2018/102X/SingleMuon_Run2018B_80Percent",
    # "/pnfs/knu.ac.kr/data/cms/store/user/kplee/SingleMuon/crab_TnPTreeZ_v20200324_12Nov2019_SingleMuon_Run2018D_GoldenJSON" : "/eos/cms/store/group/phys_muon/TagAndProbe/ULRereco/2018/102X/SingleMuon_Run2018D_98Percent",

    }

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