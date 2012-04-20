import FWCore.ParameterSet.Config as cms

#FileNames = cms.untracked.vstring('dataset:/RelValMinBias/CMSSW_4_2_0_pre4-START42_V1-v1/GEN-SIM-DIGI-RAW-HLTDEBUG')

FileNames = cms.untracked.vstring('/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/06D5C882-754F-E011-BC8C-0024E85A3EE0.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/06EB17EF-804F-E011-AFBC-0022198273C0.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/088BC57A-0F4F-E011-A2BD-0022198273D0.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/0A4F437B-074F-E011-8486-002219826F40.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/0AE0A6C8-014F-E011-A436-0022198266CB.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/0C73ECC6-004F-E011-9DF4-0024E85A406E.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/14AF46FB-0A4F-E011-8AA4-0024E85A3F71.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/165721C6-014F-E011-8633-0024E85A3EDC.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/18F33891-7B4F-E011-BC21-0024E85A4076.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/1A908223-014F-E011-9776-0024E85A3F04.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/1E1E0301-844F-E011-9C22-0024E85A3EF0.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/1EC31E54-0C4F-E011-B55F-0024E85A3EF0.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/20AE76CD-0C4F-E011-8599-002219826F44.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/2204B9D7-0D4F-E011-8692-002219826F4D.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/22F278F1-814F-E011-8663-00221981B444.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/247C1B94-064F-E011-82F0-0024E85A3F71.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/247E409F-064F-E011-8BDC-0024E85A407A.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/2611A17D-054F-E011-972F-002219826F27.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/2634930D-014F-E011-BCE0-0024E85A4FEF.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/26FCEEF6-7A4F-E011-9AFD-00221981B434.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/2EB31A54-0B4F-E011-BED4-00221981B40C.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/32C004C7-014F-E011-9824-0024E85A5147.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/346FAD23-824F-E011-831B-002219826F48.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/347B8BC5-734F-E011-829C-002219826F27.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/348B82C4-594F-E011-ADC2-00221981B45C.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/34BC158E-0D4F-E011-85B9-0024E85A3F5D.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/364AEC5C-054F-E011-BF4A-0024E85A08F8.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/3A6CFF18-064F-E011-8D82-0024E87BA5F7.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/3EA6AD1E-824F-E011-9004-0024E85A4FDB.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/4024DD36-0B4F-E011-86DC-00221981B45C.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/467BF1B5-064F-E011-89FE-0024E850EE63.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/467FD793-024F-E011-95B1-002219826F44.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/4A154D5E-054F-E011-9820-0024E850EE63.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/4AC0A83C-754F-E011-B680-0024E85A3EE4.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/4C2511A4-024F-E011-A41E-0022198273BC.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/4CAA6C3F-7C4F-E011-BC63-0022198273C0.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/506D3AB7-014F-E011-9956-0024E85A4FE7.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/5AC9C35F-CD4F-E011-88E7-0024E85A5271.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/622148D3-7A4F-E011-A3CC-0024E85A3EDC.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/62FFB884-844F-E011-A872-002219826F4D.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/68414A6F-7A4F-E011-BA35-0024E85A4FDB.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/68AA9E50-044F-E011-AFD4-0024E85A514B.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/6CA22674-074F-E011-908D-0022198273C8.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/6E329A93-054F-E011-8E72-0022198266CB.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/6E8761CC-004F-E011-BDA6-0024E85A4FC3.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/72D815F1-814F-E011-B15E-0024E85A4066.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/74E0DBE1-024F-E011-9F8B-0024E85A407A.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/761997A5-074F-E011-890D-00221981B43C.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/76AE039C-A54F-E011-A829-0024E85A4FD7.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/7CB9A95F-854F-E011-9391-0024E85A5269.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/804E1208-814F-E011-A1F5-00221981B410.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/8458D51A-074F-E011-923E-0024E85A3F71.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/863FD463-854F-E011-BD11-0024E85A4BEC.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/882835FD-0E4F-E011-9200-00221981AF36.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/8AE44A2A-094F-E011-A455-0024E85A3EE0.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/8C6EB41B-094F-E011-B00A-002219826F44.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/8C77D5B7-014F-E011-AED2-002219826F27.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/8CBD5F78-074F-E011-9647-00221981B40C.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/8E5229E3-AE4F-E011-BC62-0024E850DF90.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/90A0B85B-7A4F-E011-9FEB-002219826F48.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/96A182AC-8A4F-E011-8E5A-0024E85A3F04.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/984D657C-754F-E011-9CEF-0024E85A4076.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/9AEEDBB6-804F-E011-A8AD-00221981B410.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/9E614C2C-014F-E011-9CD6-0024E85A4C18.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/A0040BDF-CB4F-E011-A8EB-0022198273C0.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/A496FD7A-024F-E011-894D-0024E85A3EDC.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/A4C48AF4-544F-E011-A340-002219813E38.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/A6162B0A-874F-E011-A1DA-0022198273E8.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/A62E78BF-804F-E011-88F0-00221981B434.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/A668261E-214F-E011-BF1A-0024E85A4072.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/A88EA568-5C4F-E011-8888-0024E85A4EBB.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/AC4C9A4B-774F-E011-A007-0024E85A4FDB.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/ACAA4C26-054F-E011-99CB-00221981B410.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/ACAB3F9F-8D4F-E011-9D3D-002219826F4D.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/B0141FDF-A14F-E011-A955-0024E85A4FD7.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/B03D8796-864F-E011-B1E1-0024E85A3F04.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/B43A6FBF-014F-E011-B18F-00221981B44C.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/B4BDC964-4650-E011-9174-00221981B40C.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/B63F6D2F-734F-E011-80E5-0024E85A407A.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/B88D8C68-754F-E011-BF6C-002219813E38.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/B8D432B0-094F-E011-830C-002219826F23.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/C8923709-014F-E011-86C7-0024E85A3EE4.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/CA511582-024F-E011-93C6-0024E85A514B.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/CAC479D5-A94F-E011-AA33-00221981B45C.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/CE634C99-024F-E011-B1BE-0024E85A4FDB.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/D0373AEA-834F-E011-8E24-0022198273BC.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/D28C0383-024F-E011-BA0D-0024E85A4FDB.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/D83B8850-874F-E011-94BD-002219826F40.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/D873C4D4-024F-E011-8A5D-0024E85A3F71.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/DAB45E84-5C4F-E011-BA62-0022198273BC.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/DC42D869-CC4F-E011-AA79-0024E85A3EDC.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/DEFF14D1-0A4F-E011-B028-0024E85A3F71.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/E081C112-074F-E011-9C73-002219826F48.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/E241A0B1-854F-E011-AF44-0024E85A514B.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/E25FAE9A-7A4F-E011-9C65-0024E856F89A.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/E4B064BB-004F-E011-B574-002219813E38.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/EE8717C0-804F-E011-BA31-002219826F48.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/F07078C2-734F-E011-989A-0024E85A405A.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/F0D93F50-0B4F-E011-9C25-002219826F44.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/F0EC27FC-774F-E011-A540-0024E85A0928.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/F4135846-0A4F-E011-876F-0024E85A514B.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/F4749F1E-754F-E011-9C51-0024E850DF90.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/F4E3998C-024F-E011-846E-0024E85A4BEC.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/F8437401-814F-E011-8691-0024E85A3F71.root',
                                  '/store/mc/Summer11/MinBias_TuneZ2_7TeV-pythia6/GEN-SIM/START311_V2-v2/0001/FE44A4C3-0F4F-E011-9A56-0024E85A4FB7.root')