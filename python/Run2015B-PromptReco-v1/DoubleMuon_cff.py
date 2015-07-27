import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2015B/DoubleMuon/MINIAOD/PromptReco-v1/000/251/162/00000/12284DB9-4227-E511-A438-02163E013674.root',
       '/store/data/Run2015B/DoubleMuon/MINIAOD/PromptReco-v1/000/251/164/00000/402F0995-A326-E511-86BB-02163E013948.root',
       '/store/data/Run2015B/DoubleMuon/MINIAOD/PromptReco-v1/000/251/167/00000/70C4A781-A826-E511-95B4-02163E013414.root',
       '/store/data/Run2015B/DoubleMuon/MINIAOD/PromptReco-v1/000/251/168/00000/627E9C65-DD26-E511-87FB-02163E013576.root',
       '/store/data/Run2015B/DoubleMuon/MINIAOD/PromptReco-v1/000/251/244/00000/E42FEF61-6E27-E511-B93A-02163E0143C0.root',
       '/store/data/Run2015B/DoubleMuon/MINIAOD/PromptReco-v1/000/251/251/00000/0292F6F9-8A27-E511-9074-02163E012213.root',
       '/store/data/Run2015B/DoubleMuon/MINIAOD/PromptReco-v1/000/251/252/00000/9ADEE140-9C27-E511-919A-02163E011D23.root',
       '/store/data/Run2015B/DoubleMuon/MINIAOD/PromptReco-v1/000/251/493/00000/323EBCB2-D428-E511-86E5-02163E01463E.root',
       '/store/data/Run2015B/DoubleMuon/MINIAOD/PromptReco-v1/000/251/497/00000/826586F3-FC28-E511-89EE-02163E01340A.root',
       '/store/data/Run2015B/DoubleMuon/MINIAOD/PromptReco-v1/000/251/498/00000/20B6D9C3-FE28-E511-BD2D-02163E0117FF.root',
       '/store/data/Run2015B/DoubleMuon/MINIAOD/PromptReco-v1/000/251/499/00000/EA52602B-0929-E511-AB5B-02163E011955.root',
       '/store/data/Run2015B/DoubleMuon/MINIAOD/PromptReco-v1/000/251/500/00000/4897C658-4129-E511-AA73-02163E0135F3.root',
       '/store/data/Run2015B/DoubleMuon/MINIAOD/PromptReco-v1/000/251/521/00000/B4B3A942-6429-E511-8A0C-02163E01413E.root',
       '/store/data/Run2015B/DoubleMuon/MINIAOD/PromptReco-v1/000/251/522/00000/E817E288-5C29-E511-9EDC-02163E011A5A.root',
       '/store/data/Run2015B/DoubleMuon/MINIAOD/PromptReco-v1/000/251/548/00000/2258D2AA-ED29-E511-ACEA-02163E011D37.root',
       '/store/data/Run2015B/DoubleMuon/MINIAOD/PromptReco-v1/000/251/559/00000/B26153C4-A72C-E511-9EA4-02163E012B2A.root',
       '/store/data/Run2015B/DoubleMuon/MINIAOD/PromptReco-v1/000/251/560/00000/DA0DAC6D-DE29-E511-B863-02163E0133B6.root',
       '/store/data/Run2015B/DoubleMuon/MINIAOD/PromptReco-v1/000/251/561/00000/5AC326A0-142A-E511-B70C-02163E0128E3.root',
       '/store/data/Run2015B/DoubleMuon/MINIAOD/PromptReco-v1/000/251/562/00000/B2123D09-2A2A-E511-A6B5-02163E013674.root',
       '/store/data/Run2015B/DoubleMuon/MINIAOD/PromptReco-v1/000/251/562/00000/B6D3043F-712A-E511-B05E-02163E01379D.root',
       '/store/data/Run2015B/DoubleMuon/MINIAOD/PromptReco-v1/000/251/562/00000/D028B76E-702A-E511-AFAF-02163E01360E.root',
       '/store/data/Run2015B/DoubleMuon/MINIAOD/PromptReco-v1/000/251/562/00000/D82023B7-392A-E511-85D4-02163E012601.root',
       '/store/data/Run2015B/DoubleMuon/MINIAOD/PromptReco-v1/000/251/604/00000/92E20DD1-902A-E511-8B3A-02163E012A2C.root',
       '/store/data/Run2015B/DoubleMuon/MINIAOD/PromptReco-v1/000/251/612/00000/E48F3C2B-A42A-E511-A2FB-02163E011C0F.root',
       '/store/data/Run2015B/DoubleMuon/MINIAOD/PromptReco-v1/000/251/638/00000/327469FD-0D2B-E511-96BD-02163E012B30.root',
       '/store/data/Run2015B/DoubleMuon/MINIAOD/PromptReco-v1/000/251/642/00000/684E983C-D12A-E511-B288-02163E0134A9.root',
       '/store/data/Run2015B/DoubleMuon/MINIAOD/PromptReco-v1/000/251/643/00000/1A95440B-CF2C-E511-A850-02163E0138F6.root',
       '/store/data/Run2015B/DoubleMuon/MINIAOD/PromptReco-v1/000/251/643/00000/4C593916-CF2C-E511-9FED-02163E014275.root',
       '/store/data/Run2015B/DoubleMuon/MINIAOD/PromptReco-v1/000/251/643/00000/9A86E40D-CF2C-E511-AD65-02163E0128FE.root',
       '/store/data/Run2015B/DoubleMuon/MINIAOD/PromptReco-v1/000/251/721/00000/283F6D7B-602C-E511-8A31-02163E012A2C.root',
       '/store/data/Run2015B/DoubleMuon/MINIAOD/PromptReco-v1/000/251/721/00000/FCBDFC75-602C-E511-B68A-02163E014376.root',
       '/store/data/Run2015B/DoubleMuon/MINIAOD/PromptReco-v1/000/251/781/00000/D85C9422-9C2C-E511-B8A0-02163E0118E7.root',
       '/store/data/Run2015B/DoubleMuon/MINIAOD/PromptReco-v1/000/251/883/00000/402035C7-AC2D-E511-9D83-02163E0133DE.root',
       '/store/data/Run2015B/DoubleMuon/MINIAOD/PromptReco-v1/000/251/883/00000/44864117-232D-E511-8C15-02163E01463E.root',
       '/store/data/Run2015B/DoubleMuon/MINIAOD/PromptReco-v1/000/251/883/00000/CC542F3F-AC2D-E511-B093-02163E014181.root',
       '/store/data/Run2015B/DoubleMuon/MINIAOD/PromptReco-v1/000/252/116/00000/8A04959A-7A30-E511-8ECE-02163E0137FD.root',
       '/store/data/Run2015B/DoubleMuon/MINIAOD/PromptReco-v1/000/252/126/00000/44AD0FCD-C430-E511-9CE3-02163E0125E8.root',
       '/store/data/Run2015B/DoubleMuon/MINIAOD/PromptReco-v1/000/252/126/00000/86ABE6C2-4D31-E511-AB00-02163E011A04.root'
] );


secFiles.extend( [
               ] )
