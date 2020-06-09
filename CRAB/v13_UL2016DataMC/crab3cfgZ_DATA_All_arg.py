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

config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/ReReco/Final/Cert_271036-284044_13TeV_ReReco_07Aug2017_Collisions16_JSON.txt'

# config.Data.allowNonValidInputDataset = True

version = '_v20200609_'
# 'MultiCRAB' part
if __name__ == '__main__':
    
    from CRABAPI.RawCommand import crabCommand

    config.General.requestName = 'TnPTreeZ'+version+'21Feb2020_SingleMuon_Run2016Bver2_HIPM_GoldenJSON'
    config.Data.inputDataset = '/SingleMuon/Run2016B-21Feb2020_ver2_UL2016_HIPM-v1/AOD'
    config.JobType.psetName = '../../test/zmumu/tp_from_aod_Data_arg.py'
    config.JobType.pyCfgParams = ['globalTag=106X_dataRun2_v27']
    crabCommand('submit', config = config)

    config.General.requestName = 'TnPTreeZ'+version+'21Feb2020_SingleMuon_Run2016C_HIPM_GoldenJSON'
    config.Data.inputDataset = '/SingleMuon/Run2016C-21Feb2020_UL2016_HIPM-v1/AOD'
    config.JobType.psetName = '../../test/zmumu/tp_from_aod_Data_arg.py'
    config.JobType.pyCfgParams = ['globalTag=106X_dataRun2_v27']
    crabCommand('submit', config = config)

    config.General.requestName = 'TnPTreeZ'+version+'21Feb2020_SingleMuon_Run2016D_HIPM_GoldenJSON'
    config.Data.inputDataset = '/SingleMuon/Run2016D-21Feb2020_UL2016_HIPM-v1/AOD'
    config.JobType.psetName = '../../test/zmumu/tp_from_aod_Data_arg.py'
    config.JobType.pyCfgParams = ['globalTag=106X_dataRun2_v27']
    crabCommand('submit', config = config)

    config.General.requestName = 'TnPTreeZ'+version+'21Feb2020_SingleMuon_Run2016E_HIPM_GoldenJSON'
    config.Data.inputDataset = '/SingleMuon/Run2016E-21Feb2020_UL2016_HIPM-v1/AOD'
    config.JobType.psetName = '../../test/zmumu/tp_from_aod_Data_arg.py'
    config.JobType.pyCfgParams = ['globalTag=106X_dataRun2_v27']
    crabCommand('submit', config = config)

    config.General.requestName = 'TnPTreeZ'+version+'21Feb2020_SingleMuon_Run2016F_HIPM_GoldenJSON'
    config.Data.inputDataset = '/SingleMuon/Run2016F-21Feb2020_UL2016_HIPM-v1/AOD'
    config.JobType.psetName = '../../test/zmumu/tp_from_aod_Data_arg.py'
    config.JobType.pyCfgParams = ['globalTag=106X_dataRun2_v27']
    crabCommand('submit', config = config)

    config.General.requestName = 'TnPTreeZ'+version+'21Feb2020_SingleMuon_Run2016F_GoldenJSON'
    config.Data.inputDataset = '/SingleMuon/Run2016F-21Feb2020_UL2016-v1/AOD'
    config.JobType.psetName = '../../test/zmumu/tp_from_aod_Data_arg.py'
    config.JobType.pyCfgParams = ['globalTag=106X_dataRun2_v27']
    crabCommand('submit', config = config)

    config.General.requestName = 'TnPTreeZ'+version+'21Feb2020_SingleMuon_Run2016G_GoldenJSON'
    config.Data.inputDataset = '/SingleMuon/Run2016G-21Feb2020_UL2016-v1/AOD'
    config.JobType.psetName = '../../test/zmumu/tp_from_aod_Data_arg.py'
    config.JobType.pyCfgParams = ['globalTag=106X_dataRun2_v27']
    crabCommand('submit', config = config)

    config.General.requestName = 'TnPTreeZ'+version+'21Feb2020_SingleMuon_Run2016H_GoldenJSON'
    config.Data.inputDataset = '/SingleMuon/Run2016H-21Feb2020_UL2016-v1/AOD'
    config.JobType.psetName = '../../test/zmumu/tp_from_aod_Data_arg.py'
    config.JobType.pyCfgParams = ['globalTag=106X_dataRun2_v27']
    crabCommand('submit', config = config)

