import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/Phys14DR/SMS-T1qqqq_2J_mGl-1400_mLSP-100_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_tsg_PHYS14_25_V1-v1/00000/DEDF48DE-F56B-E411-973A-002590DB9262.root',
       '/store/mc/Phys14DR/SMS-T1qqqq_2J_mGl-1400_mLSP-100_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_tsg_PHYS14_25_V1-v1/00000/ECB8D1D7-F56B-E411-9F3D-0025907FD40C.root',
       '/store/mc/Phys14DR/SMS-T1qqqq_2J_mGl-1400_mLSP-100_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_tsg_PHYS14_25_V1-v1/10000/4650836E-666C-E411-9994-D8D385FF6C5E.root',
       '/store/mc/Phys14DR/SMS-T1qqqq_2J_mGl-1400_mLSP-100_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_tsg_PHYS14_25_V1-v1/10000/4E1A7C71-666C-E411-8F87-003048F0E1EA.root',
       '/store/mc/Phys14DR/SMS-T1qqqq_2J_mGl-1400_mLSP-100_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_tsg_PHYS14_25_V1-v1/10000/8CA18A25-666C-E411-A06F-002590DB91F0.root' ] );


secFiles.extend( [
               ] )

