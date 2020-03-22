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
config.Data.unitsPerJob = 5
# config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB()) # -- do not use as SiteDB was gone
config.Data.outLFNDirBase = '/store/user/kplee/'
config.Data.publication = False

# config.Site.storageSite = 'T3_KR_KISTI'
config.Site.storageSite = 'T2_KR_KNU'

# config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/ReReco/Final/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt'
# FirstRun = 271036
# LastRun = 284044
# config.Data.runRange = '%d-%d' % (FirstRun, LastRun)


version = '_v20200322_'
# 'MultiCRAB' part
if __name__ == '__main__':
    
    from CRABAPI.RawCommand import crabCommand

    config.General.requestName = 'TnPTreeZ'+version+'DYLL_M50_Pythia8_FlatPU30to80_Winter20'
    config.Data.inputDataset = '/DYToLL_M-50_TuneCP5_14TeV-pythia8/Run3Winter20DRMiniAOD-DRFlatPU30to80_110X_mcRun3_2021_realistic_v6-v2/AODSIM'
    config.Data.allowNonValidInputDataset = True
    config.JobType.psetName = '../../test/zmumu/tp_from_aod_MC_arg.py'
    config.JobType.pyCfgParams = ['globalTag=110X_mcRun3_2021_realistic_v6'] # -- CMSSW: CMSSW_11_0_0_patch1
    crabCommand('submit', config = config)



    # config.General.requestName = ''
    # config.Data.inputDataset = ''
    # crabCommand('submit', config = config)
