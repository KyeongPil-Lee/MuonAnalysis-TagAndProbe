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


version = '_v20200116_'
# 'MultiCRAB' part
if __name__ == '__main__':
    
    from CRABAPI.RawCommand import crabCommand

    config.General.requestName = 'TnPTreeZ'+version+'RelValZMM_14_106X'
    config.Data.inputDataset = '/RelValZMM_14/CMSSW_10_6_1_patch1-PU_106X_mcRun3_2021_realistic_v3-v1/GEN-SIM-RECO'
    config.JobType.psetName = '../../test/zmumu/tp_from_aod_MC_arg.py'
    config.JobType.pyCfgParams = ["106X_mcRun3_2021_realistic_v3"]
    crabCommand('submit', config = config)

    config.General.requestName = 'TnPTreeZ'+version+'RelValZMM_14_110X_pre11'
    config.Data.inputDataset = '/RelValZMM_14/CMSSW_11_0_0_pre11-PU_110X_mcRun3_2021_realistic_v5-v1/GEN-SIM-RECO'
    config.JobType.psetName = '../../test/zmumu/tp_from_aod_MC_arg.py'
    config.JobType.pyCfgParams = ["110X_mcRun3_2021_realistic_v5"]
    crabCommand('submit', config = config)

    config.General.requestName = 'TnPTreeZ'+version+'RelValZMM_14_110X_pre12'
    config.Data.inputDataset = '/RelValZMM_14/CMSSW_11_0_0_pre12-PU_110X_mcRun3_2021_realistic_v5-v1/GEN-SIM-RECO'
    config.JobType.psetName = '../../test/zmumu/tp_from_aod_MC_arg.py'
    config.JobType.pyCfgParams = ["110X_mcRun3_2021_realistic_v5"]
    crabCommand('submit', config = config)

    config.General.requestName = 'TnPTreeZ'+version+'RelValZMM_14_110X_pre13'
    config.Data.inputDataset = '/RelValZMM_14/CMSSW_11_0_0_pre13-PU_110X_mcRun3_2021_realistic_v6-v1/GEN-SIM-RECO'
    config.JobType.psetName = '../../test/zmumu/tp_from_aod_MC_arg.py'
    config.JobType.pyCfgParams = ["110X_mcRun3_2021_realistic_v6"]
    crabCommand('submit', config = config)

    # config.General.requestName = ''
    # config.Data.inputDataset = ''
    # crabCommand('submit', config = config)
