from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = ''
config.General.workArea = 'TagProbe'

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '../../tp_from_aod_simple_MC.py'

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


version = '_v20181011_LegacyRerecoWithIDFlag_'
# 'MultiCRAB' part
if __name__ == '__main__':
    
    from CRABAPI.RawCommand import crabCommand

    config.General.requestName = 'TagProbe'+version+'JpsiToMuMu_JpsiPt8_Pythia8'
    config.Data.inputDataset = '/JpsiToMuMu_JpsiPt8_TuneCUEP8M1_13TeV-pythia8/RunIISpring16DR80-PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/AODSIM'
    crabCommand('submit', config = config)

    # config.General.requestName = ''
    # config.Data.inputDataset = ''
    # crabCommand('submit', config = config)
