from MuonAnalysis.TagAndProbe.ROOTFileTransfer import *

tool = TransferTool()
tool.user = 'kplee'
tool.host = '147.47.242.67'
tool.port = 1240

tool.dic_input_to_outputPath = {
    GetCRABOutputDir("crab_TnPTreeZ_v20200331_RelValZMM_13UP16_UL16_HighStat_L1Fix_preFVP") : "/home/kplee/Temp"
}
tool.Transfer()