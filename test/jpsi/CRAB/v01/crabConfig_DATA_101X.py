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


config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/13TeV/PromptReco/Cert_314472-321221_13TeV_PromptReco_Collisions18_JSON.txt'
# config.Data.runRange = '305636-305636'

version = '_v20180828_'
# 'MultiCRAB' part
if __name__ == '__main__':
    
    from CRABAPI.RawCommand import crabCommand

    # -- Run2018A
    config.General.requestName = 'TnPTreeJPsi'+version+'Charmonium_Run2018Av1_GoldenJSON'
    config.Data.inputDataset = '/Charmonium/Run2018A-PromptReco-v1/AOD'
    config.JobType.psetName = '../../tp_from_aod_simple_Data_CtoF_101X_v9.py'
    crabCommand('submit', config = config)

    config.General.requestName = 'TnPTreeJPsi'+version+'Charmonium_Run2018Av2_GoldenJSON'
    config.Data.inputDataset = '/Charmonium/Run2018A-PromptReco-v2/AOD'
    config.JobType.psetName = '../../tp_from_aod_simple_Data_CtoF_101X_v9.py'
    crabCommand('submit', config = config)

    config.General.requestName = 'TnPTreeJPsi'+version+'Charmonium_Run2018Av3_GoldenJSON'
    config.Data.inputDataset = '/Charmonium/Run2018A-PromptReco-v3/AOD'
    config.JobType.psetName = '../../tp_from_aod_simple_Data_CtoF_101X_v10.py'
    crabCommand('submit', config = config)

    # -- Run2018B
    config.General.requestName = 'TnPTreeJPsi'+version+'Charmonium_Run2018Bv1_GoldenJSON'
    config.Data.inputDataset = '/Charmonium/Run2018B-PromptReco-v1/AOD'
    config.JobType.psetName = '../../tp_from_aod_simple_Data_CtoF_101X_v10.py'
    crabCommand('submit', config = config)

    config.General.requestName = 'TnPTreeJPsi'+version+'Charmonium_Run2018Bv2_GoldenJSON'
    config.Data.inputDataset = '/Charmonium/Run2018B-PromptReco-v2/AOD'
    config.JobType.psetName = '../../tp_from_aod_simple_Data_CtoF_101X_v11.py'
    crabCommand('submit', config = config)

    # -- Run2018C
    config.General.requestName = 'TnPTreeJPsi'+version+'Charmonium_Run2018Cv1_GoldenJSON'
    config.Data.inputDataset = '/Charmonium/Run2018C-PromptReco-v1/AOD'
    config.JobType.psetName = '../../tp_from_aod_simple_Data_CtoF_101X_v11.py'
    crabCommand('submit', config = config)

    config.General.requestName = 'TnPTreeJPsi'+version+'Charmonium_Run2018Cv2_GoldenJSON'
    config.Data.inputDataset = '/Charmonium/Run2018C-PromptReco-v2/AOD'
    config.JobType.psetName = '../../tp_from_aod_simple_Data_CtoF_101X_v11.py'
    crabCommand('submit', config = config)

    config.General.requestName = 'TnPTreeJPsi'+version+'Charmonium_Run2018Cv3_GoldenJSON'
    config.Data.inputDataset = '/Charmonium/Run2018C-PromptReco-v3/AOD'
    config.JobType.psetName = '../../tp_from_aod_simple_Data_CtoF_101X_v11.py'
    crabCommand('submit', config = config)