from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = ''
config.General.workArea = 'TagProbe'

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '../../tp_from_aod_simple_Data_v2.py'

config.Data.inputDataset = ''

config.Data.inputDBS = 'global'
config.Data.splitting = 'Automatic'
# config.Data.splitting = 'LumiBased'
# config.Data.unitsPerJob = 20
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = False

# config.Site.storageSite = 'T3_KR_KISTI'
config.Site.storageSite = 'T2_KR_KNU'

config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/ReReco/Final/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt'
# FirstRun = 271036
# LastRun = 284044
# config.Data.runRange = '%d-%d' % (FirstRun, LastRun)


version = '_v20180830_LegacyRerecoWithIDFlag_'
# 'MultiCRAB' part
if __name__ == '__main__':
    
    from CRABAPI.RawCommand import crabCommand

    # config.General.requestName = 'TagProbe'+version+'Charmonium_Run2016Bver1_GoldenJSON'
    # config.Data.inputDataset = '/Charmonium/Run2016B-07Aug17_ver1-v1/AOD'
    # crabCommand('submit', config = config)

    config.General.requestName = 'TagProbe'+version+'Charmonium_Run2016Bver2_GoldenJSON'
    config.Data.inputDataset = '/Charmonium/Run2016B-07Aug17_ver2-v1/AOD'
    crabCommand('submit', config = config)

    config.General.requestName = 'TagProbe'+version+'Charmonium_Run2016C_GoldenJSON'
    config.Data.inputDataset = '/Charmonium/Run2016C-07Aug17-v1/AOD'
    crabCommand('submit', config = config)

    config.General.requestName = 'TagProbe'+version+'Charmonium_Run2016D_GoldenJSON'
    config.Data.inputDataset = '/Charmonium/Run2016D-07Aug17-v1/AOD'
    crabCommand('submit', config = config)

    config.General.requestName = 'TagProbe'+version+'Charmonium_Run2016E_GoldenJSON'
    config.Data.inputDataset = '/Charmonium/Run2016E-07Aug17-v1/AOD'
    crabCommand('submit', config = config)

    config.General.requestName = 'TagProbe'+version+'Charmonium_Run2016F_GoldenJSON'
    config.Data.inputDataset = '/Charmonium/Run2016F-07Aug17-v1/AOD'
    crabCommand('submit', config = config)

    config.General.requestName = 'TagProbe'+version+'Charmonium_Run2016G_GoldenJSON'
    config.Data.inputDataset = '/Charmonium/Run2016G-07Aug17-v1/AOD'
    crabCommand('submit', config = config)

    config.General.requestName = 'TagProbe'+version+'Charmonium_Run2016H_GoldenJSON'
    config.Data.inputDataset = '/Charmonium/Run2016H-07Aug17-v1/AOD'
    crabCommand('submit', config = config)

    # config.General.requestName = ''
    # config.Data.inputDataset = ''
    # crabCommand('submit', config = config)
