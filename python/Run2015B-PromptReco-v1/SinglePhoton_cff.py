import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/251/096/00000/EAC7605D-5526-E511-A895-02163E011FAB.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/251/161/00000/6E54E224-9C26-E511-B468-02163E0121BD.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/251/162/00000/D83F99AD-4227-E511-8960-02163E0133B5.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/251/163/00000/728A4697-9F26-E511-ADAD-02163E0119C9.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/251/164/00000/80F01937-A426-E511-B2D7-02163E01182A.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/251/167/00000/A6972749-A826-E511-B7C5-02163E013414.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/251/168/00000/3CBFC5DE-BB26-E511-A5C2-02163E0135B4.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/251/244/00000/D8D780D0-7727-E511-A2C5-02163E0137FC.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/251/251/00000/6EED993F-9927-E511-A6A9-02163E01259F.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/251/252/00000/289A42F1-9627-E511-8A00-02163E011C7F.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/251/491/00000/9C464F2A-C628-E511-8923-02163E01463E.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/251/493/00000/6819E5CA-C828-E511-AD4E-02163E0135F3.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/251/497/00000/D43AFD8F-E028-E511-8467-02163E01414A.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/251/498/00000/969A3EAE-EB28-E511-B91A-02163E012601.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/251/499/00000/5EEEB744-F728-E511-8E47-02163E013440.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/251/500/00000/1838372C-2329-E511-8E7B-02163E011BD1.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/251/521/00000/9A3A76CA-6629-E511-8B2E-02163E011EE9.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/251/522/00000/9297A416-5B29-E511-8956-02163E014543.root',
      '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/251/548/00000/16919B06-D329-E511-B79D-02163E01252E.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/251/559/00000/82304EB8-A62C-E511-B4A3-02163E0133F9.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/251/560/00000/7E5EF8F5-DD29-E511-BC88-02163E011DAE.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/251/561/00000/F6777C76-152A-E511-A06F-02163E013553.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/251/562/00000/8210BDF2-422A-E511-AD74-02163E01463E.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/251/562/00000/C4A70AFB-272A-E511-9B44-02163E011955.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/251/604/00000/865C217E-992A-E511-8FD4-02163E0127DF.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/251/612/00000/DE1D52B8-AB2A-E511-AF79-02163E0134CC.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/251/628/00000/404908F7-B52A-E511-AC9A-02163E013830.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/251/638/00000/0E9B99F5-F62A-E511-A7F4-02163E01299A.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/251/642/00000/363CBB73-E82A-E511-B93B-02163E0133A4.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/251/643/00000/26E24212-942C-E511-953D-02163E012044.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/251/643/00000/34B19403-A62C-E511-BC66-02163E0124CC.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/251/716/00000/BCC3BD84-2F2C-E511-96D3-02163E011B19.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/251/721/00000/284B19B0-462C-E511-9BDF-02163E011861.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/251/781/00000/501608D5-AD2C-E511-949F-02163E01420D.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/251/883/00000/2E44F5B7-4E2D-E511-85FC-02163E012377.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/251/883/00000/ACE0E713-362D-E511-ADA8-02163E01360E.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/252/102/00000/C860A95B-D92F-E511-A473-02163E01241A.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/252/116/00000/6EFB7390-7A30-E511-901E-02163E014462.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/252/126/00000/9C91DDFD-D930-E511-852E-02163E0125E8.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/252/489/00000/8E84B579-3434-E511-96BF-02163E014543.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/252/490/00000/8E01C5EB-3534-E511-9010-02163E012283.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/252/492/00000/5EF62604-4734-E511-8F20-02163E011836.root'
 ] );


secFiles.extend( [
               ] )
