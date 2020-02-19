from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = ''
config.General.workArea = 'CRABDir'

config.JobType.pluginName = 'Analysis'
# config.JobType.psetName = '../../test/zmumu/tp_from_aod_MC_102X_v15.py'

config.Data.inputDataset = ''

config.Data.inputDBS = 'global'
# config.Data.splitting = 'Automatic'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = False

# config.Site.storageSite = 'T3_KR_KISTI'
config.Site.storageSite = 'T2_KR_KNU'

# config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/ReReco/Final/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt'
# FirstRun = 271036
# LastRun = 284044
# config.Data.runRange = '%d-%d' % (FirstRun, LastRun)


version = '_v20200219_'
# 'MultiCRAB' part
if __name__ == '__main__':
    
    from CRABAPI.RawCommand import crabCommand

    # config.General.requestName = 'TnPTreeZ'+version+'RelValZMM_13UP16_UL16_HighStat'
    # config.Data.inputDataset = '/RelValZMM_13UP16/CMSSW_10_6_8-PU25ns_106X_mcRun2_asymptotic_preVFP_v5_UL16hltval_preVFP_v5-v1/AODSIM'
    # config.Data.allowNonValidInputDataset = True
    # config.JobType.psetName = '../../test/zmumu/tp_from_aod_MC_arg.py'
    # config.JobType.pyCfgParams = ['globalTag=106X_mcRun2_asymptotic_preVFP_v5']
    # crabCommand('submit', config = config)

    config.General.requestName = 'TnPTreeZ'+version+'RelValZMM_13UP16_UL16_HighStat_WrongL1'
    config.Data.inputDataset = '/RelValZMM_13UP16/CMSSW_10_6_8-PU25ns_106X_mcRun2_asymptotic_preVFP_v3_UL16hltval_preVFP-v1/AODSIM'
    config.Data.allowNonValidInputDataset = True
    config.JobType.psetName = '../../test/zmumu/tp_from_aod_MC_arg.py'
    config.JobType.pyCfgParams = ['globalTag=106X_mcRun2_asymptotic_preVFP_v3']
    crabCommand('submit', config = config)

    # config.General.requestName = ''
    # config.Data.inputDataset = ''
    # crabCommand('submit', config = config)
