import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/Phys14DR/Tbar_tW-channel-DR_Tune4C_13TeV-CSA14-powheg-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/0AFEB3CA-9D72-E411-8ACC-20CF305B057E.root',
       '/store/mc/Phys14DR/Tbar_tW-channel-DR_Tune4C_13TeV-CSA14-powheg-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/161ADBA3-9D72-E411-811D-002590D0B0D2.root',
       '/store/mc/Phys14DR/Tbar_tW-channel-DR_Tune4C_13TeV-CSA14-powheg-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/185613B5-9D72-E411-BD97-00248CB3209C.root',
       '/store/mc/Phys14DR/Tbar_tW-channel-DR_Tune4C_13TeV-CSA14-powheg-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/1C0A4DC8-9D72-E411-97F6-20CF305B050B.root',
       '/store/mc/Phys14DR/Tbar_tW-channel-DR_Tune4C_13TeV-CSA14-powheg-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/287FC2CC-9D72-E411-8EDD-20CF3027A61B.root',
       '/store/mc/Phys14DR/Tbar_tW-channel-DR_Tune4C_13TeV-CSA14-powheg-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/308AEDAC-9D72-E411-9E59-00259073E510.root',
       '/store/mc/Phys14DR/Tbar_tW-channel-DR_Tune4C_13TeV-CSA14-powheg-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/50AF61CB-9D72-E411-9A9C-20CF3027A5C4.root',
       '/store/mc/Phys14DR/Tbar_tW-channel-DR_Tune4C_13TeV-CSA14-powheg-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/9AE166D1-9D72-E411-BBA1-20CF305B051B.root',
       '/store/mc/Phys14DR/Tbar_tW-channel-DR_Tune4C_13TeV-CSA14-powheg-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/AEE37AC5-9D72-E411-8E35-002590D0AF8C.root',
       '/store/mc/Phys14DR/Tbar_tW-channel-DR_Tune4C_13TeV-CSA14-powheg-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/BC098EC4-9D72-E411-8613-20CF305616E1.root',
       '/store/mc/Phys14DR/Tbar_tW-channel-DR_Tune4C_13TeV-CSA14-powheg-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/C89F48A9-9D72-E411-9D57-E0CB4E29C4C4.root',
       '/store/mc/Phys14DR/Tbar_tW-channel-DR_Tune4C_13TeV-CSA14-powheg-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/CCCCF3B8-9D72-E411-8EC7-E0CB4E4408DE.root',
       '/store/mc/Phys14DR/Tbar_tW-channel-DR_Tune4C_13TeV-CSA14-powheg-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/CE40D3B3-9D72-E411-995B-E0CB4E29C511.root',
       '/store/mc/Phys14DR/Tbar_tW-channel-DR_Tune4C_13TeV-CSA14-powheg-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/E69173B4-9D72-E411-931C-20CF3027A5A6.root',
       '/store/mc/Phys14DR/Tbar_tW-channel-DR_Tune4C_13TeV-CSA14-powheg-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/ECF085A6-9D72-E411-88E1-20CF305B04D1.root',
       '/store/mc/Phys14DR/Tbar_tW-channel-DR_Tune4C_13TeV-CSA14-powheg-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/F04EA6BA-9D72-E411-81D2-E0CB4E19F965.root',
       '/store/mc/Phys14DR/Tbar_tW-channel-DR_Tune4C_13TeV-CSA14-powheg-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/F2298DCE-9D72-E411-BC20-00259074AE80.root',
       '/store/mc/Phys14DR/Tbar_tW-channel-DR_Tune4C_13TeV-CSA14-powheg-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/FA05D7AA-9D72-E411-9ED3-002590D0AF68.root',
       '/store/mc/Phys14DR/Tbar_tW-channel-DR_Tune4C_13TeV-CSA14-powheg-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/10000/22CBF12A-4372-E411-B610-00259073E398.root',
       '/store/mc/Phys14DR/Tbar_tW-channel-DR_Tune4C_13TeV-CSA14-powheg-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/10000/9E83E926-4372-E411-8E83-E0CB4E55366E.root',
       '/store/mc/Phys14DR/Tbar_tW-channel-DR_Tune4C_13TeV-CSA14-powheg-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/10000/D08F3227-4372-E411-8447-002590D0B006.root' ] );


secFiles.extend( [
               ] )

