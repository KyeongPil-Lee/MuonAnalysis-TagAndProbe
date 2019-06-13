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
config.Data.unitsPerJob = 3
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = False

# config.Site.storageSite = 'T3_KR_KISTI'
config.Site.storageSite = 'T2_KR_KNU'

# config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/ReReco/Final/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt'
# FirstRun = 271036
# LastRun = 284044
# config.Data.runRange = '%d-%d' % (FirstRun, LastRun)


version = '_v20190613_'
# 'MultiCRAB' part
if __name__ == '__main__':
    
    from CRABAPI.RawCommand import crabCommand

    config.General.requestName = 'TnPTreeZ'+version+'1060For2018_RelValZMM'
    config.Data.inputDataset = '/RelValZMM_13/CMSSW_10_6_0-PU25ns_106X_upgrade2018_realistic_v4-v1/GEN-SIM-RECO'
    config.JobType.psetName = '../../test/zmumu/tp_from_aod_MC_106X_upgrade2018_realistic_v4.py'
    # config.Data.allowNonValidInputDataset = True # -- current status = Production
    crabCommand('submit', config = config)

    # config.General.requestName = ''
    # config.Data.inputDataset = ''
    # crabCommand('submit', config = config)