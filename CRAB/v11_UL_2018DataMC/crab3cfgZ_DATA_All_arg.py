from CRABClient.UserUtilities import config

config = config()

config.General.requestName = ''
config.General.workArea = 'CRABDir'

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = ''

config.Data.inputDataset = ''
# config.Data.useParent = True

config.Data.inputDBS = 'global'
# config.Data.splitting = 'Automatic'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 50

config.Data.outLFNDirBase = '/store/user/kplee/'
config.Data.publication = False
# config.Data.ignoreLocality = True
# config.Site.whitelist = ['T2_KR_*', 'T2_US_*', 'T2_IT_*', 'T3_IT_*'] # -- mandatory for ignoreLocality option
# config.Site.storageSite = 'T3_KR_KISTI'
config.Site.storageSite = 'T2_KR_KNU'

config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/13TeV/ReReco/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt'

config.Data.allowNonValidInputDataset = True # -- RunD is under production

version = '_v20200324_'
# 'MultiCRAB' part
if __name__ == '__main__':
    
    from CRABAPI.RawCommand import crabCommand

    config.General.requestName = 'TnPTreeZ'+version+'12Nov2019_SingleMuon_Run2018A_GoldenJSON'
    config.Data.inputDataset = '/SingleMuon/Run2018A-12Nov2019_UL2018-v2/AOD'
    config.JobType.psetName = '../../test/zmumu/tp_from_aod_Data_arg.py'
    config.JobType.pyCfgParams = ['globalTag=106X_dataRun2_v24']
    crabCommand('submit', config = config)

    config.General.requestName = 'TnPTreeZ'+version+'12Nov2019_SingleMuon_Run2018B_GoldenJSON'
    config.Data.inputDataset = '/SingleMuon/Run2018B-12Nov2019_UL2018-v2/AOD'
    config.JobType.psetName = '../../test/zmumu/tp_from_aod_Data_arg.py'
    config.JobType.pyCfgParams = ['globalTag=106X_dataRun2_v24']
    crabCommand('submit', config = config)

    config.General.requestName = 'TnPTreeZ'+version+'12Nov2019_SingleMuon_Run2018C_GoldenJSON'
    config.Data.inputDataset = '/SingleMuon/Run2018C-12Nov2019_UL2018-v2/AOD'
    config.JobType.psetName = '../../test/zmumu/tp_from_aod_Data_arg.py'
    config.JobType.pyCfgParams = ['globalTag=106X_dataRun2_v24']
    crabCommand('submit', config = config)


    config.General.requestName = 'TnPTreeZ'+version+'12Nov2019_SingleMuon_Run2018D_GoldenJSON'
    config.Data.inputDataset = '/SingleMuon/Run2018D-12Nov2019_UL2018-v4/AOD'
    config.JobType.psetName = '../../test/zmumu/tp_from_aod_Data_arg.py'
    config.JobType.pyCfgParams = ['globalTag=106X_dataRun2_v24']
    crabCommand('submit', config = config)

