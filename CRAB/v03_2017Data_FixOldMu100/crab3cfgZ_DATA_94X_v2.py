from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = ''
config.General.workArea = 'CRABDir'

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '../../test/zmumu/tp_from_aod_Data_94X_dataRun2_ReReco_EOY17_v2.py'
# config.JobType.numCores = 4
# config.JobType.maxMemoryMB = 2500
# config.JobType.maxJobRuntimeMin = 2000

config.Data.inputDataset = ''
# config.Data.useParent = True

config.Data.inputDBS = 'global'
# config.Data.splitting = 'Automatic'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 100

config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = False
# config.Data.ignoreLocality = True
# config.Site.whitelist = ['T2_KR_*', 'T2_US_*', 'T2_IT_*', 'T3_IT_*'] # -- mandatory for ignoreLocality option
# config.Site.storageSite = 'T3_KR_KISTI'
config.Site.storageSite = 'T2_KR_KNU'

config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/ReReco/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt'

version = '_v20190510_100LumiPerJob_'
# 'MultiCRAB' part
if __name__ == '__main__':
    
    from CRABAPI.RawCommand import crabCommand

    # config.General.requestName = 'TnPTreeZ'+version+'17Nov2017_SingleMuon_Run2017Bv1_GoldenJSON'
    # config.Data.inputDataset = '/SingleMuon/Run2017B-17Nov2017-v1/AOD'
    # crabCommand('submit', config = config)

    # config.General.requestName = 'TnPTreeZ'+version+'17Nov2017_SingleMuon_Run2017Cv1_GoldenJSON'
    # config.Data.inputDataset = '/SingleMuon/Run2017C-17Nov2017-v1/AOD'
    # crabCommand('submit', config = config)

    # config.General.requestName = 'TnPTreeZ'+version+'17Nov2017_SingleMuon_Run2017Dv1_GoldenJSON'
    # config.Data.inputDataset = '/SingleMuon/Run2017D-17Nov2017-v1/AOD'
    # crabCommand('submit', config = config)

    # config.General.requestName = 'TnPTreeZ'+version+'17Nov2017_SingleMuon_Run2017Ev1_GoldenJSON'
    # config.Data.inputDataset = '/SingleMuon/Run2017E-17Nov2017-v1/AOD'
    # crabCommand('submit', config = config)

    config.General.requestName = 'TnPTreeZ'+version+'17Nov2017_SingleMuon_Run2017Fv1_GoldenJSON'
    config.Data.inputDataset = '/SingleMuon/Run2017F-17Nov2017-v1/AOD'
    crabCommand('submit', config = config)

