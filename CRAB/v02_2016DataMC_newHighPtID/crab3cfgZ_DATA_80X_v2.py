from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = ''
config.General.workArea = 'CRABDir'

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '../../test/zmumu/tp_from_aod_Data.py'
# config.JobType.numCores = 4
# config.JobType.maxMemoryMB = 2500
# config.JobType.maxJobRuntimeMin = 2000

config.Data.inputDataset = ''
# config.Data.useParent = True

config.Data.inputDBS = 'global'
# config.Data.splitting = 'Automatic'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 200

config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = False
# config.Data.ignoreLocality = True
# config.Site.whitelist = ['T2_KR_*', 'T2_US_*', 'T2_IT_*', 'T3_IT_*'] # -- mandatory for ignoreLocality option
# config.Site.storageSite = 'T3_KR_KISTI'
config.Site.storageSite = 'T2_KR_KNU'

config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/ReReco/Final/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt'

version = '_v20190509_'
# 'MultiCRAB' part
if __name__ == '__main__':
    
    from CRABAPI.RawCommand import crabCommand

    # config.General.requestName = 'TnPTreeZ'+version+'07Aug17_SingleMuon_Run2016Bver2_GoldenJSON'
    # config.Data.inputDataset = '/SingleMuon/Run2016B-07Aug17_ver2-v1/AOD'
    # crabCommand('submit', config = config)

    # config.General.requestName = 'TnPTreeZ'+version+'07Aug17_SingleMuon_Run2016C_GoldenJSON'
    # config.Data.inputDataset = '/SingleMuon/Run2016C-07Aug17-v1/AOD'
    # crabCommand('submit', config = config)

    config.General.requestName = 'TnPTreeZ'+version+'07Aug17_SingleMuon_Run2016D_GoldenJSON'
    config.Data.inputDataset = '/SingleMuon/Run2016D-07Aug17-v1/AOD'
    crabCommand('submit', config = config)

    # config.General.requestName = 'TnPTreeZ'+version+'07Aug17_SingleMuon_Run2016E_GoldenJSON'
    # config.Data.inputDataset = '/SingleMuon/Run2016E-07Aug17-v1/AOD'
    # crabCommand('submit', config = config)

    # config.General.requestName = 'TnPTreeZ'+version+'07Aug17_SingleMuon_Run2016F_GoldenJSON'
    # config.Data.inputDataset = '/SingleMuon/Run2016F-07Aug17-v1/AOD'
    # crabCommand('submit', config = config)

    config.General.requestName = 'TnPTreeZ'+version+'07Aug17_SingleMuon_Run2016G_GoldenJSON'
    config.Data.inputDataset = '/SingleMuon/Run2016G-07Aug17-v1/AOD'
    crabCommand('submit', config = config)

    config.General.requestName = 'TnPTreeZ'+version+'07Aug17_SingleMuon_Run2016H_GoldenJSON'
    config.Data.inputDataset = '/SingleMuon/Run2016H-07Aug17-v1/AOD'
    crabCommand('submit', config = config)
