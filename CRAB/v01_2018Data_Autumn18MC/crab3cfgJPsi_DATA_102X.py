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

config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/13TeV/PromptReco/Cert_314472-325175_13TeV_PromptReco_Collisions18_JSON.txt'

version = '_v20190211_'
# 'MultiCRAB' part
if __name__ == '__main__':
    
    from CRABAPI.RawCommand import crabCommand

    config.General.requestName = 'TnPTreeJPsi'+version+'17Sep2018_Charmonium_Run2018Av1_GoldenJSON'
    config.Data.inputDataset = '/Charmonium/Run2018A-17Sep2018-v1/AOD'
    config.JobType.psetName = '../../test/jpsi/tp_from_aod_simple_Data_CtoF_102X_Sep2018Rereco_v1.py'
    crabCommand('submit', config = config)

    config.General.requestName = 'TnPTreeJPsi'+version+'17Sep2018_Charmonium_Run2018Bv1_GoldenJSON'
    config.Data.inputDataset = '/Charmonium/Run2018B-17Sep2018-v1/AOD'
    config.JobType.psetName = '../../test/jpsi/tp_from_aod_simple_Data_CtoF_102X_Sep2018Rereco_v1.py'
    crabCommand('submit', config = config)

    config.General.requestName = 'TnPTreeJPsi'+version+'17Sep2018_Charmonium_Run2018Cv1_GoldenJSON'
    config.Data.inputDataset = '/Charmonium/Run2018C-17Sep2018-v1/AOD'
    config.JobType.psetName = '../../test/jpsi/tp_from_aod_simple_Data_CtoF_102X_Sep2018Rereco_v1.py'
    crabCommand('submit', config = config)

    config.General.requestName = 'TnPTreeJPsi'+version+'Charmonium_Run2018Dv2_GoldenJSON'
    config.Data.inputDataset = '/Charmonium/Run2018D-PromptReco-v2/AOD'
    config.JobType.psetName = '../../test/jpsi/tp_from_aod_simple_Data_CtoF_102X_Prompt_v11.py'
    crabCommand('submit', config = config)

