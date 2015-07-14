import FWCore.ParameterSet.Config as cms
from commandLineParameters import *

process = cms.Process("analysis")

process.options = cms.untracked.PSet(
    SkipEvent = cms.untracked.vstring('ProductNotFound')
    )

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = options.reportEvery

process.options   = cms.untracked.PSet(
    SkipEvent   = cms.untracked.vstring('ProductNotFound'),
    wantSummary = cms.untracked.bool(True)
    )

## configure geometry & conditions
process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')

###############
# tree maker
###############

from AllHadronicSUSY.TreeMaker.makeTreeFromMiniAOD_cff import makeTreeFromMiniAOD
makeTreeFromMiniAOD(process,
                    outFileName="ReducedSelection",
                    reportEveryEvt=options.reportEvery,
                    testFileName="",
                    Global_Tag="PHYS14_25_V2::All",
                    lostlepton=True,
                    tagandprobe=False,
                    numProcessedEvt=options.numEvents,
                    doZinv=True,
                    debugtracks=False,
                    geninfo=False,
                    filtertag="RECO"
                    )

# drop all recoCand stuff and replace with 4-vectors
# --------------------------------------------------
process.TreeMaker2.VarsRecoCand = []

process.goodElectrons4Vec = cms.EDProducer("fourVectorProducer",
                                           particleCollection = cms.untracked.InputTag("LeptonsNew","IdIsoElectron"),
                                           debug = cms.untracked.bool(False)
                                           )

process.goodMuons4Vec = cms.EDProducer("fourVectorProducer",
                                           particleCollection = cms.untracked.InputTag("LeptonsNew","IdIsoMuon"),
                                           debug = cms.untracked.bool(False)
                                           )

process.TreeMaker2.VectorTLorentzVector.append("goodMuons4Vec(Muons)")
process.TreeMaker2.VectorInt.append("LeptonsNew:MuonCharge(MuonCharge)")
process.TreeMaker2.VectorTLorentzVector.append("goodElectrons4Vec(Electrons)")
process.TreeMaker2.VectorInt.append("LeptonsNew:ElectronCharge(ElectronCharge)")

##################################
# DEFINE MODULES FOR ANALYSIS
##################################

###############
# rho stuff
###############

process.TreeMaker2.VarsDouble.append("fixedGridRhoFastjetAll(rho)")

# ==================
# fat jet stuff 
# ==================

#from AWhitbeck.SuSySubstructure.fatJetStudies_cff import *
#fatJetSetup(process) ## define relevant modules and a sequence to be used, process.SumJetMass

# ==================
# ak4 jets
# ==================

process.ak4Jets = cms.EDProducer("fourVectorProducer",
                                   particleCollection = cms.untracked.InputTag("GoodJets"),
                                   debug = cms.untracked.bool(False)
                                   )

process.ak4JetsRaw = cms.EDProducer("fourVectorProducer",
                                    particleCollection = cms.untracked.InputTag("slimmedJets"),
                                    debug = cms.untracked.bool(False)
                                    )

process.TreeMaker2.VectorTLorentzVector.append("ak4Jets")
process.TreeMaker2.VectorTLorentzVector.append("ak4JetsRaw")
#process.TreeMaker2.VectorInt.append("GoodJets:passJetID(ak4Jets_passedJetID)")

process.TreeMaker2.VectorDouble.append("JetsProperties:bDiscriminatorUser(ak4Jets_CSVdisc)")
process.TreeMaker2.VectorDouble.append("JetsProperties:bDiscriminatorMVA(ak4Jets_MVAdisc)")
#process.TreeMaker2.VectorDouble.append("JetsProperties:bDiscriminatorSimpleCSV(ak4Jets_SimpleCSVdisc)")

#process.TreeMaker2.VectorInt.append("JetsProperties:NumBhadrons(ak4Jets_NumBhadrons)")
#process.TreeMaker2.VectorInt.append("JetsProperties:NumChadrons(ak4Jets_NumChadrons)")

process.TreeMaker2.VectorDouble.append("JetsProperties:chargedHadronEnergyFraction(ak4Jets_chargeHadEfrac)")
process.TreeMaker2.VectorDouble.append("JetsProperties:neutralHadronEnergyFraction(ak4Jets_neutralHadEfrac)")
process.TreeMaker2.VectorDouble.append("JetsProperties:photonEnergyFraction(ak4Jets_photonEfrac)")
process.TreeMaker2.VectorInt.append("JetsProperties:chargedHadronMultiplicity(ak4Jets_chargedHadMult)")
process.TreeMaker2.VectorInt.append("JetsProperties:neutralHadronMultiplicity(ak4Jets_neutralHadMult)")
process.TreeMaker2.VectorInt.append("JetsProperties:photonMultiplicity(ak4Jets_photonMult)")
process.TreeMaker2.VectorInt.append("JetsProperties:flavor(ak4Jets_flavor)")

### ak4 gen jets
#process.ak4GenJets = cms.EDProducer("fourVectorProducer",
#                                   particleCollection = cms.untracked.InputTag("slimmedGenJets"),
#                                   debug = cms.untracked.bool(False)
#                                   )

#process.TreeMaker2.VectorTLorentzVector.append("ak4GenJets")

######################
# event filters
######################

process.RA2eventFilter = cms.EDFilter("RA2eventFilter",
                                      HTCollection = cms.untracked.InputTag("htNoPhotons"),
                                      minHT = cms.untracked.double(500.),
                                      MHTCollection = cms.untracked.InputTag("mhtNoPhotons"),
                                      minMHT = cms.untracked.double(200.),
                                      NJetsCollection = cms.untracked.InputTag("nJetsNoPhotons"),
#                                      minNJets = cms.untracked.int(4),
                                      BTagsCollection = cms.untracked.InputTag("BTags"),
#                                      minBTags = cms.untracked.int(0),
                                      minDeltaPhiNCollection = cms.untracked.InputTag("metNoPhotons","minDeltaPhiN"),
                                      debug = cms.untracked.bool(False)
                                      )

## CONFIGURE TFILESERVICE

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string(options.outputFile+"_RA2AnalysisTree.root"),
                                   closeFileFast = cms.untracked.bool(True)
                                   )

##  LOAD DATAFILES
if options.inputFilesConfig!="" :
    process.load("AWhitbeck.SuSySubstructure."+options.inputFilesConfig+"_cff")

if options.files!=[] :   
    readFiles = cms.untracked.vstring()
    readFiles.extend( options.files )
    process.source = cms.Source("PoolSource",
                                fileNames = readFiles )

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(options.numEvents)
)

##  DEFINE SCHEDULE

process.WriteTree = cms.Path( process.Baseline * 
                              process.AdditionalSequence *
                              process.goodElectrons4Vec * 
                              process.goodMuons4Vec *  

                              process.ak4Jets *
                              process.ak4JetsRaw *
                              #process.ak4GenJets *

                              #process.SumJetMass * 
                              
                              process.TreeMaker2 
                              )

#OUPUT CONFIGURATION
#process.out = cms.OutputModule("PoolOutputModule",
#                               fileName = cms.untracked.string('test.root'),
#                               #save only events passing the full path
#                               #SelectEvents = cms.untracked.PSet( SelectEvents = cms.vstring('p') ),
#                               outputCommands = cms.untracked.vstring('drop *','keep *_*photon*_*_*','keep *_*Jets*_*_*'
#                                                                      )
#                               )

#process.outpath = cms.EndPath(process.out)
