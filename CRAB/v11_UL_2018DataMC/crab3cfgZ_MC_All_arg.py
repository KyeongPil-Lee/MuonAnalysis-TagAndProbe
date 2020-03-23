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

config.Data.allowNonValidInputDataset = True

version = '_v20200324_'
# 'MultiCRAB' part
if __name__ == '__main__':
    
    from CRABAPI.RawCommand import crabCommand

    # -- Madgraph
    config.General.requestName = 'TnPTreeZ'+version+'UL18MC_DYJetsToLL_M50_Madgraph'
    config.Data.inputDataset = '/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer19UL18RECO-106X_upgrade2018_realistic_v11_L1v1-v1/AODSIM' # -- # events: 203902675
    config.JobType.psetName = '../../test/zmumu/tp_from_aod_MC_arg.py'
    config.JobType.pyCfgParams = ['globalTag=106X_upgrade2018_realistic_v11_L1v1']
    crabCommand('submit', config = config)

    # -- aMC@NLO
    config.General.requestName = 'TnPTreeZ'+version+'UL18MC_DYJetsToLL_M50_aMCNLO'
    config.Data.inputDataset = '/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer19UL18RECO-106X_upgrade2018_realistic_v11_L1v1-v2/AODSIM' # -- # events: 203902675
    config.JobType.psetName = '../../test/zmumu/tp_from_aod_MC_arg.py'
    config.JobType.pyCfgParams = ['globalTag=106X_upgrade2018_realistic_v11_L1v1']
    crabCommand('submit', config = config)

    # -- Powheg
    config.General.requestName = 'TnPTreeZ'+version+'UL18MC_ZToMuMu_M50to120_Powheg'
    config.Data.inputDataset = '/ZToMuMu_NNPDF31_TuneCP5_13TeV-powheg-pythia8_M_50_120/RunIISummer19UL18RECO-106X_upgrade2018_realistic_v11_L1v1-v2/AODSIM' # -- # events: 203902675
    config.JobType.psetName = '../../test/zmumu/tp_from_aod_MC_arg.py'
    config.JobType.pyCfgParams = ['globalTag=106X_upgrade2018_realistic_v11_L1v1']
    crabCommand('submit', config = config)

    



    # config.General.requestName = ''
    # config.Data.inputDataset = ''
    # crabCommand('submit', config = config)
