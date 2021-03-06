import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/Phys14DR/T_tW-channel-DR_Tune4C_13TeV-CSA14-powheg-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/1E9DD9C1-8E7A-E411-87DD-1CC1DE04FF50.root',
       '/store/mc/Phys14DR/T_tW-channel-DR_Tune4C_13TeV-CSA14-powheg-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/3C999DBB-8E7A-E411-A218-1CC1DE1D1E3C.root',
       '/store/mc/Phys14DR/T_tW-channel-DR_Tune4C_13TeV-CSA14-powheg-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/3E092BBC-8E7A-E411-BD6A-1CC1DE1D03FC.root',
       '/store/mc/Phys14DR/T_tW-channel-DR_Tune4C_13TeV-CSA14-powheg-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/563D4EBB-8E7A-E411-A87A-1CC1DE1CDF30.root',
       '/store/mc/Phys14DR/T_tW-channel-DR_Tune4C_13TeV-CSA14-powheg-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/5E152ABE-8E7A-E411-A649-1CC1DE051038.root',
       '/store/mc/Phys14DR/T_tW-channel-DR_Tune4C_13TeV-CSA14-powheg-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/687E24C9-8E7A-E411-96BB-78E7D1E4B772.root',
       '/store/mc/Phys14DR/T_tW-channel-DR_Tune4C_13TeV-CSA14-powheg-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/AA10E6C4-8E7A-E411-B73C-1CC1DE0570A0.root',
       '/store/mc/Phys14DR/T_tW-channel-DR_Tune4C_13TeV-CSA14-powheg-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/AA26E5B9-8E7A-E411-91F2-1CC1DE1CEFC8.root',
       '/store/mc/Phys14DR/T_tW-channel-DR_Tune4C_13TeV-CSA14-powheg-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/D45C47C0-8E7A-E411-A890-1CC1DE0503C0.root',
       '/store/mc/Phys14DR/T_tW-channel-DR_Tune4C_13TeV-CSA14-powheg-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/10000/0A182E14-8B7A-E411-BA19-00266CFFC598.root',
       '/store/mc/Phys14DR/T_tW-channel-DR_Tune4C_13TeV-CSA14-powheg-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/10000/20C29FBA-8A7A-E411-88EE-C4346BC84780.root',
       '/store/mc/Phys14DR/T_tW-channel-DR_Tune4C_13TeV-CSA14-powheg-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/10000/22782E14-8B7A-E411-8CFD-00266CFFC598.root',
       '/store/mc/Phys14DR/T_tW-channel-DR_Tune4C_13TeV-CSA14-powheg-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/10000/28F84314-8B7A-E411-8342-00266CFFC598.root',
       '/store/mc/Phys14DR/T_tW-channel-DR_Tune4C_13TeV-CSA14-powheg-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/10000/4070225B-8A7A-E411-A357-C4346BC84780.root',
       '/store/mc/Phys14DR/T_tW-channel-DR_Tune4C_13TeV-CSA14-powheg-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/10000/40A03814-8B7A-E411-8FCD-00266CFFC598.root',
       '/store/mc/Phys14DR/T_tW-channel-DR_Tune4C_13TeV-CSA14-powheg-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/10000/92278BE3-8A7A-E411-B1F4-00266CFFBCD0.root',
       '/store/mc/Phys14DR/T_tW-channel-DR_Tune4C_13TeV-CSA14-powheg-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/10000/92802E14-8B7A-E411-824F-00266CFFC598.root',
       '/store/mc/Phys14DR/T_tW-channel-DR_Tune4C_13TeV-CSA14-powheg-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/10000/9A772F14-8B7A-E411-A2F4-00266CFFC598.root',
       '/store/mc/Phys14DR/T_tW-channel-DR_Tune4C_13TeV-CSA14-powheg-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/10000/9C784971-897A-E411-9B55-1CC1DE050110.root',
       '/store/mc/Phys14DR/T_tW-channel-DR_Tune4C_13TeV-CSA14-powheg-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/10000/A2A51D65-897A-E411-8364-00266CFFBC64.root',
       '/store/mc/Phys14DR/T_tW-channel-DR_Tune4C_13TeV-CSA14-powheg-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/10000/B4A52D14-8B7A-E411-8529-00266CFFC598.root' ] );


secFiles.extend( [
               ] )

