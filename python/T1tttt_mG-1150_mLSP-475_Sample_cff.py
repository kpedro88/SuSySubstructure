import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/user/whitbeck/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1100to1400_mLSP-25to500_50GeVX50GeV_Binning/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1150_mLSP-475_B2Gpattuples/6a48e960161f4ab4cc640d464b9b3a3e/genParticlesForJets_10_1_nj6.root',
       '/store/user/whitbeck/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1100to1400_mLSP-25to500_50GeVX50GeV_Binning/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1150_mLSP-475_B2Gpattuples/6a48e960161f4ab4cc640d464b9b3a3e/genParticlesForJets_11_1_FBF.root',
       '/store/user/whitbeck/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1100to1400_mLSP-25to500_50GeVX50GeV_Binning/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1150_mLSP-475_B2Gpattuples/6a48e960161f4ab4cc640d464b9b3a3e/genParticlesForJets_12_1_Jwb.root',
       '/store/user/whitbeck/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1100to1400_mLSP-25to500_50GeVX50GeV_Binning/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1150_mLSP-475_B2Gpattuples/6a48e960161f4ab4cc640d464b9b3a3e/genParticlesForJets_13_1_IyG.root',
       '/store/user/whitbeck/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1100to1400_mLSP-25to500_50GeVX50GeV_Binning/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1150_mLSP-475_B2Gpattuples/6a48e960161f4ab4cc640d464b9b3a3e/genParticlesForJets_14_1_6VT.root',
       '/store/user/whitbeck/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1100to1400_mLSP-25to500_50GeVX50GeV_Binning/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1150_mLSP-475_B2Gpattuples/6a48e960161f4ab4cc640d464b9b3a3e/genParticlesForJets_15_1_72t.root',
       '/store/user/whitbeck/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1100to1400_mLSP-25to500_50GeVX50GeV_Binning/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1150_mLSP-475_B2Gpattuples/6a48e960161f4ab4cc640d464b9b3a3e/genParticlesForJets_16_1_Nk9.root',
       '/store/user/whitbeck/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1100to1400_mLSP-25to500_50GeVX50GeV_Binning/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1150_mLSP-475_B2Gpattuples/6a48e960161f4ab4cc640d464b9b3a3e/genParticlesForJets_17_1_Rcb.root',
       '/store/user/whitbeck/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1100to1400_mLSP-25to500_50GeVX50GeV_Binning/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1150_mLSP-475_B2Gpattuples/6a48e960161f4ab4cc640d464b9b3a3e/genParticlesForJets_18_1_Bh3.root',
       '/store/user/whitbeck/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1100to1400_mLSP-25to500_50GeVX50GeV_Binning/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1150_mLSP-475_B2Gpattuples/6a48e960161f4ab4cc640d464b9b3a3e/genParticlesForJets_19_1_S9t.root',
       '/store/user/whitbeck/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1100to1400_mLSP-25to500_50GeVX50GeV_Binning/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1150_mLSP-475_B2Gpattuples/6a48e960161f4ab4cc640d464b9b3a3e/genParticlesForJets_1_1_tXo.root',
       '/store/user/whitbeck/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1100to1400_mLSP-25to500_50GeVX50GeV_Binning/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1150_mLSP-475_B2Gpattuples/6a48e960161f4ab4cc640d464b9b3a3e/genParticlesForJets_20_1_dO3.root',
       '/store/user/whitbeck/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1100to1400_mLSP-25to500_50GeVX50GeV_Binning/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1150_mLSP-475_B2Gpattuples/6a48e960161f4ab4cc640d464b9b3a3e/genParticlesForJets_21_1_vTg.root',
       '/store/user/whitbeck/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1100to1400_mLSP-25to500_50GeVX50GeV_Binning/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1150_mLSP-475_B2Gpattuples/6a48e960161f4ab4cc640d464b9b3a3e/genParticlesForJets_22_1_DWs.root',
       '/store/user/whitbeck/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1100to1400_mLSP-25to500_50GeVX50GeV_Binning/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1150_mLSP-475_B2Gpattuples/6a48e960161f4ab4cc640d464b9b3a3e/genParticlesForJets_23_1_LwT.root',
       '/store/user/whitbeck/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1100to1400_mLSP-25to500_50GeVX50GeV_Binning/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1150_mLSP-475_B2Gpattuples/6a48e960161f4ab4cc640d464b9b3a3e/genParticlesForJets_24_1_How.root',
       '/store/user/whitbeck/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1100to1400_mLSP-25to500_50GeVX50GeV_Binning/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1150_mLSP-475_B2Gpattuples/6a48e960161f4ab4cc640d464b9b3a3e/genParticlesForJets_25_1_pwf.root',
       '/store/user/whitbeck/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1100to1400_mLSP-25to500_50GeVX50GeV_Binning/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1150_mLSP-475_B2Gpattuples/6a48e960161f4ab4cc640d464b9b3a3e/genParticlesForJets_26_1_g5Q.root',
       '/store/user/whitbeck/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1100to1400_mLSP-25to500_50GeVX50GeV_Binning/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1150_mLSP-475_B2Gpattuples/6a48e960161f4ab4cc640d464b9b3a3e/genParticlesForJets_27_1_OW1.root',
       '/store/user/whitbeck/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1100to1400_mLSP-25to500_50GeVX50GeV_Binning/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1150_mLSP-475_B2Gpattuples/6a48e960161f4ab4cc640d464b9b3a3e/genParticlesForJets_28_1_l70.root',
       '/store/user/whitbeck/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1100to1400_mLSP-25to500_50GeVX50GeV_Binning/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1150_mLSP-475_B2Gpattuples/6a48e960161f4ab4cc640d464b9b3a3e/genParticlesForJets_29_1_iYh.root',
       '/store/user/whitbeck/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1100to1400_mLSP-25to500_50GeVX50GeV_Binning/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1150_mLSP-475_B2Gpattuples/6a48e960161f4ab4cc640d464b9b3a3e/genParticlesForJets_2_1_l10.root',
       '/store/user/whitbeck/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1100to1400_mLSP-25to500_50GeVX50GeV_Binning/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1150_mLSP-475_B2Gpattuples/6a48e960161f4ab4cc640d464b9b3a3e/genParticlesForJets_30_1_9Vz.root',
       '/store/user/whitbeck/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1100to1400_mLSP-25to500_50GeVX50GeV_Binning/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1150_mLSP-475_B2Gpattuples/6a48e960161f4ab4cc640d464b9b3a3e/genParticlesForJets_31_1_3vV.root',
       '/store/user/whitbeck/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1100to1400_mLSP-25to500_50GeVX50GeV_Binning/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1150_mLSP-475_B2Gpattuples/6a48e960161f4ab4cc640d464b9b3a3e/genParticlesForJets_32_1_0i7.root',
       '/store/user/whitbeck/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1100to1400_mLSP-25to500_50GeVX50GeV_Binning/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1150_mLSP-475_B2Gpattuples/6a48e960161f4ab4cc640d464b9b3a3e/genParticlesForJets_33_1_Xv3.root',
       '/store/user/whitbeck/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1100to1400_mLSP-25to500_50GeVX50GeV_Binning/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1150_mLSP-475_B2Gpattuples/6a48e960161f4ab4cc640d464b9b3a3e/genParticlesForJets_34_1_ZNr.root',
       '/store/user/whitbeck/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1100to1400_mLSP-25to500_50GeVX50GeV_Binning/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1150_mLSP-475_B2Gpattuples/6a48e960161f4ab4cc640d464b9b3a3e/genParticlesForJets_35_1_tMx.root',
       '/store/user/whitbeck/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1100to1400_mLSP-25to500_50GeVX50GeV_Binning/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1150_mLSP-475_B2Gpattuples/6a48e960161f4ab4cc640d464b9b3a3e/genParticlesForJets_36_1_jtp.root',
       '/store/user/whitbeck/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1100to1400_mLSP-25to500_50GeVX50GeV_Binning/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1150_mLSP-475_B2Gpattuples/6a48e960161f4ab4cc640d464b9b3a3e/genParticlesForJets_37_1_uqD.root',
       '/store/user/whitbeck/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1100to1400_mLSP-25to500_50GeVX50GeV_Binning/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1150_mLSP-475_B2Gpattuples/6a48e960161f4ab4cc640d464b9b3a3e/genParticlesForJets_38_1_qoM.root',
       '/store/user/whitbeck/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1100to1400_mLSP-25to500_50GeVX50GeV_Binning/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1150_mLSP-475_B2Gpattuples/6a48e960161f4ab4cc640d464b9b3a3e/genParticlesForJets_39_1_rff.root',
       '/store/user/whitbeck/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1100to1400_mLSP-25to500_50GeVX50GeV_Binning/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1150_mLSP-475_B2Gpattuples/6a48e960161f4ab4cc640d464b9b3a3e/genParticlesForJets_3_1_8Vo.root',
       '/store/user/whitbeck/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1100to1400_mLSP-25to500_50GeVX50GeV_Binning/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1150_mLSP-475_B2Gpattuples/6a48e960161f4ab4cc640d464b9b3a3e/genParticlesForJets_40_1_nHA.root',
       '/store/user/whitbeck/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1100to1400_mLSP-25to500_50GeVX50GeV_Binning/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1150_mLSP-475_B2Gpattuples/6a48e960161f4ab4cc640d464b9b3a3e/genParticlesForJets_41_1_1va.root',
       '/store/user/whitbeck/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1100to1400_mLSP-25to500_50GeVX50GeV_Binning/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1150_mLSP-475_B2Gpattuples/6a48e960161f4ab4cc640d464b9b3a3e/genParticlesForJets_42_1_54q.root',
       '/store/user/whitbeck/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1100to1400_mLSP-25to500_50GeVX50GeV_Binning/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1150_mLSP-475_B2Gpattuples/6a48e960161f4ab4cc640d464b9b3a3e/genParticlesForJets_43_1_ef3.root',
       '/store/user/whitbeck/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1100to1400_mLSP-25to500_50GeVX50GeV_Binning/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1150_mLSP-475_B2Gpattuples/6a48e960161f4ab4cc640d464b9b3a3e/genParticlesForJets_44_1_9PF.root',
       '/store/user/whitbeck/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1100to1400_mLSP-25to500_50GeVX50GeV_Binning/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1150_mLSP-475_B2Gpattuples/6a48e960161f4ab4cc640d464b9b3a3e/genParticlesForJets_45_1_M4S.root',
       '/store/user/whitbeck/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1100to1400_mLSP-25to500_50GeVX50GeV_Binning/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1150_mLSP-475_B2Gpattuples/6a48e960161f4ab4cc640d464b9b3a3e/genParticlesForJets_46_1_Fpg.root',
       '/store/user/whitbeck/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1100to1400_mLSP-25to500_50GeVX50GeV_Binning/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1150_mLSP-475_B2Gpattuples/6a48e960161f4ab4cc640d464b9b3a3e/genParticlesForJets_47_1_URk.root',
       '/store/user/whitbeck/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1100to1400_mLSP-25to500_50GeVX50GeV_Binning/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1150_mLSP-475_B2Gpattuples/6a48e960161f4ab4cc640d464b9b3a3e/genParticlesForJets_48_1_4Cc.root',
       '/store/user/whitbeck/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1100to1400_mLSP-25to500_50GeVX50GeV_Binning/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1150_mLSP-475_B2Gpattuples/6a48e960161f4ab4cc640d464b9b3a3e/genParticlesForJets_49_1_IFw.root',
       '/store/user/whitbeck/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1100to1400_mLSP-25to500_50GeVX50GeV_Binning/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1150_mLSP-475_B2Gpattuples/6a48e960161f4ab4cc640d464b9b3a3e/genParticlesForJets_4_1_zPr.root',
       '/store/user/whitbeck/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1100to1400_mLSP-25to500_50GeVX50GeV_Binning/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1150_mLSP-475_B2Gpattuples/6a48e960161f4ab4cc640d464b9b3a3e/genParticlesForJets_50_1_uz7.root',
       '/store/user/whitbeck/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1100to1400_mLSP-25to500_50GeVX50GeV_Binning/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1150_mLSP-475_B2Gpattuples/6a48e960161f4ab4cc640d464b9b3a3e/genParticlesForJets_51_1_uqR.root',
       '/store/user/whitbeck/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1100to1400_mLSP-25to500_50GeVX50GeV_Binning/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1150_mLSP-475_B2Gpattuples/6a48e960161f4ab4cc640d464b9b3a3e/genParticlesForJets_52_1_1Eg.root',
       '/store/user/whitbeck/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1100to1400_mLSP-25to500_50GeVX50GeV_Binning/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1150_mLSP-475_B2Gpattuples/6a48e960161f4ab4cc640d464b9b3a3e/genParticlesForJets_53_1_Hwq.root',
       '/store/user/whitbeck/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1100to1400_mLSP-25to500_50GeVX50GeV_Binning/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1150_mLSP-475_B2Gpattuples/6a48e960161f4ab4cc640d464b9b3a3e/genParticlesForJets_54_1_5gu.root',
       '/store/user/whitbeck/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1100to1400_mLSP-25to500_50GeVX50GeV_Binning/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1150_mLSP-475_B2Gpattuples/6a48e960161f4ab4cc640d464b9b3a3e/genParticlesForJets_55_1_PV4.root',
       '/store/user/whitbeck/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1100to1400_mLSP-25to500_50GeVX50GeV_Binning/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1150_mLSP-475_B2Gpattuples/6a48e960161f4ab4cc640d464b9b3a3e/genParticlesForJets_56_1_TUH.root',
       '/store/user/whitbeck/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1100to1400_mLSP-25to500_50GeVX50GeV_Binning/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1150_mLSP-475_B2Gpattuples/6a48e960161f4ab4cc640d464b9b3a3e/genParticlesForJets_57_1_bK2.root',
       '/store/user/whitbeck/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1100to1400_mLSP-25to500_50GeVX50GeV_Binning/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1150_mLSP-475_B2Gpattuples/6a48e960161f4ab4cc640d464b9b3a3e/genParticlesForJets_58_1_nxR.root',
       '/store/user/whitbeck/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1100to1400_mLSP-25to500_50GeVX50GeV_Binning/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1150_mLSP-475_B2Gpattuples/6a48e960161f4ab4cc640d464b9b3a3e/genParticlesForJets_59_1_GdS.root',
       '/store/user/whitbeck/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1100to1400_mLSP-25to500_50GeVX50GeV_Binning/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1150_mLSP-475_B2Gpattuples/6a48e960161f4ab4cc640d464b9b3a3e/genParticlesForJets_5_1_cYa.root',
       '/store/user/whitbeck/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1100to1400_mLSP-25to500_50GeVX50GeV_Binning/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1150_mLSP-475_B2Gpattuples/6a48e960161f4ab4cc640d464b9b3a3e/genParticlesForJets_60_1_hzM.root',
       '/store/user/whitbeck/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1100to1400_mLSP-25to500_50GeVX50GeV_Binning/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1150_mLSP-475_B2Gpattuples/6a48e960161f4ab4cc640d464b9b3a3e/genParticlesForJets_61_1_blW.root',
       '/store/user/whitbeck/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1100to1400_mLSP-25to500_50GeVX50GeV_Binning/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1150_mLSP-475_B2Gpattuples/6a48e960161f4ab4cc640d464b9b3a3e/genParticlesForJets_62_1_NlT.root',
       '/store/user/whitbeck/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1100to1400_mLSP-25to500_50GeVX50GeV_Binning/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1150_mLSP-475_B2Gpattuples/6a48e960161f4ab4cc640d464b9b3a3e/genParticlesForJets_6_1_7Zy.root',
       '/store/user/whitbeck/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1100to1400_mLSP-25to500_50GeVX50GeV_Binning/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1150_mLSP-475_B2Gpattuples/6a48e960161f4ab4cc640d464b9b3a3e/genParticlesForJets_7_1_muT.root',
       '/store/user/whitbeck/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1100to1400_mLSP-25to500_50GeVX50GeV_Binning/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1150_mLSP-475_B2Gpattuples/6a48e960161f4ab4cc640d464b9b3a3e/genParticlesForJets_8_1_18Q.root',
       '/store/user/whitbeck/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1100to1400_mLSP-25to500_50GeVX50GeV_Binning/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1150_mLSP-475_B2Gpattuples/6a48e960161f4ab4cc640d464b9b3a3e/genParticlesForJets_9_1_MQy.root' ] );


secFiles.extend( [
               ] )

