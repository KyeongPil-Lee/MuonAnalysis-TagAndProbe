from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = ''
config.General.workArea = 'CRABDir'

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = ''
# config.JobType.numCores = 4
# config.JobType.maxMemoryMB = 2500
# config.JobType.maxJobRuntimeMin = 2000

config.Data.inputDataset = ''
# config.Data.useParent = True

config.Data.inputDBS = 'global'
config.Data.splitting = 'Automatic'
# config.Data.unitsPerJob = 3
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = False
# config.Data.ignoreLocality = True
# config.Site.whitelist = ['T2_KR_*', 'T2_US_*', 'T2_IT_*', 'T3_IT_*'] # -- mandatory for ignoreLocality option
# config.Site.storageSite = 'T3_KR_KISTI'
config.Site.storageSite = 'T2_KR_KNU'

# config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/13TeV/PromptReco/Cert_314472-323523_13TeV_PromptReco_Collisions18_JSON.txt'
config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/13TeV/PromptReco/Cert_314472-324209_13TeV_PromptReco_Collisions18_JSON.txt'
# config.Data.runRange = '305636-305636'

version = '_v20181018_'
# 'MultiCRAB' part
if __name__ == '__main__':
    
    from CRABAPI.RawCommand import crabCommand

    config.General.requestName = 'TnPTreeZ'+version+'SingleMuon_Run2018Dv2_GoldenJSON_323524_to_324209'
    config.Data.inputDataset = '/SingleMuon/Run2018D-PromptReco-v2/AOD'
    config.JobType.psetName = '../../test/zmumu/tp_from_aod_Data_102X_v4.py'
    config.Data.runRange = '323524-324209'
    crabCommand('submit', config = config)
