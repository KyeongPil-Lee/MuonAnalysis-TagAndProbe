from CRABClient.UserUtilities import config
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
config.Data.outLFNDirBase = '/store/user/kplee/'
config.Data.publication = False

# config.Site.storageSite = 'T3_KR_KISTI'
config.Site.storageSite = 'T2_KR_KNU'

# config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/ReReco/Final/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt'
# FirstRun = 271036
# LastRun = 284044
# config.Data.runRange = '%d-%d' % (FirstRun, LastRun)


version = '_v20200331_'
# 'MultiCRAB' part
if __name__ == '__main__':
    
    from CRABAPI.RawCommand import crabCommand

    # config.General.requestName = 'TnPTreeZ'+version+'RelValZMM_13UP16_UL16_HighStat_L1Fix_postFVP'
    # config.Data.inputDataset = '/RelValZMM_13UP16/CMSSW_10_6_11_CANDIDATE3-PU25ns_106X_mcRun2_asymptotic_v12_hltul16_post-v1/AODSIM'
    # config.Data.allowNonValidInputDataset = True
    # config.JobType.psetName = '../../test/zmumu/tp_from_aod_MC_arg.py'
    # config.JobType.pyCfgParams = ['globalTag=106X_mcRun2_asymptotic_v12']
    # crabCommand('submit', config = config)

    config.General.requestName = 'TnPTreeZ'+version+'RelValZMM_13UP16_UL16_HighStat_L1Fix_preFVP'
    config.Data.inputDataset = '/RelValZMM_13UP16/CMSSW_10_6_11_CANDIDATE3-PU25ns_106X_mcRun2_asymptotic_preVFP_v6_hltul16_pre-v1/AODSIM'
    config.Data.allowNonValidInputDataset = True
    config.JobType.psetName = '../../test/zmumu/tp_from_aod_MC_arg.py'
    config.JobType.pyCfgParams = ['globalTag=106X_mcRun2_asymptotic_preVFP_v6']
    crabCommand('submit', config = config)

    

    # config.General.requestName = ''
    # config.Data.inputDataset = ''
    # crabCommand('submit', config = config)
