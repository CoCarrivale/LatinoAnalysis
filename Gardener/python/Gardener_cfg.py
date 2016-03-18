
eosProdBase= '/eos/cms/'
eosTargBaseIn = '/eos/user/x/xjanssen/HWW2015/'
eosTargBaseOut= '/eos/user/x/xjanssen/HWW2015/'


# ---- production to run on
# .... .... this is defined by mkGardener in "-p" "--prods" option

Productions= {

#### 74x / 21Oct & 21OctBis tags / miniAOD v2

  '21Oct_25ns_MC'   : {
                        'isData'  : False ,
                        'samples' : 'LatinoTrees/AnalysisStep/test/crab/samples/samples_spring15_miniaodv2_25ns.py' , 
                        'dirExt'  : 'LatinoTrees' ,
                      #  'dirExt'  : 'split' ,
                        'gDocID'  : '1wH73CYA_T4KMkl1Cw-xLTj8YG7OPqayDnP53N-lZwFQ' ,
                        #'puData'  : '/afs/cern.ch/user/x/xjanssen/public/MyDataPileupHistogram.root',
                        'puData'  : '/afs/cern.ch/user/x/xjanssen/public/Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON_v2_from256630_PileupHistogram.root' ,
                        #'bigSamples': ['DYJetsToLL_M-10to50'] ,
                      } ,

  '21Oct_Run2015D_05Oct2015' : {
                        'isData'  : True ,
                        'samples' : 'LatinoTrees/AnalysisStep/test/crab/samples/samples_dataD_05Oct2015_25ns.py' ,
                        #'dirExt'  : 'Run2015D_05Oct2015' ,
                        'dirExt'  : 'split' ,
                      } ,

  '21Oct_Run2015D_PromptReco' : {
                        'isData'  : True ,
                        'samples' : 'LatinoTrees/AnalysisStep/test/crab/samples/samples_dataD_PromptReco_25ns.py' ,
                        #'dirExt'  : 'Run2015D_PromptReco' ,
                        'dirExt'  : 'split' ,
                      } ,

  '21OctBis_Run2015D_05Oct2015' : {
                        'isData'  : True ,
                        'samples' : 'LatinoTrees/AnalysisStep/test/crab/samples/samples_dataD_05Oct2015_25ns_21OctBis.py',
                        #'dirExt'  : 'Run2015D_PromptReco' ,
                        'dirExt'  : 'split2' ,
                      } ,

  '21OctBis_Run2015D_PromptReco_0716pb' : {
                        'isData'  : True ,
                        'samples' : 'LatinoTrees/AnalysisStep/test/crab/samples/samples_dataD_PromptReco_25ns_21OctBis_0716pb.py' ,
                        'dirExt'  : 'split2' ,
                      } ,

  '21OctBis_Run2015D_PromptReco_0851pb' : {
                        'isData'  : True ,
                        'samples' : 'LatinoTrees/AnalysisStep/test/crab/samples/samples_dataD_PromptReco_25ns_21OctBis_0851pb.py' ,
                        'dirExt'  : 'split2' ,
                      } ,

#### 76x / StarWars tag / miniAOD v1

  '08Jan_25ns_mAODv1_MC'   : {
                        'isData'  : False ,
                        'samples' : 'LatinoTrees/AnalysisStep/test/crab/samples/samples_fall15_miniaod_25ns.py' ,
                        'dirExt'  : 'LatinoTrees' ,
                        'gDocID'  : '1wH73CYA_T4KMkl1Cw-xLTj8YG7OPqayDnP53N-lZwFQ' ,
                        'puData'  : '/afs/cern.ch/user/x/xjanssen/public/Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON_v2_from256630_PileupHistogram.root' ,
                      } ,

#### 76x / StarWars tag (v2) / miniAOD v2

  '18Jan_25ns_mAODv2_MC_TEST'   : {
                        'isData'  : False ,
                        'samples' : 'LatinoTrees/AnalysisStep/test/crab/samples/samples_fall15_miniaodv2_25ns.py' ,
                        'dir'     : '/store/group/phys_higgs/cmshww/amassiro/RunII/18Jan/MC/25ns/',
                        'dirExt'  : 'LatinoTrees' ,
                        #'gDocID'  : '1wH73CYA_T4KMkl1Cw-xLTj8YG7OPqayDnP53N-lZwFQ' ,
                        'puData'  : '/afs/cern.ch/user/x/xjanssen/public/Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON_v2_from256630_PileupHistogram.root' ,
                      } ,


#### 76x / StarWars tag (v3) / miniAOD v2

  '22Jan_25ns_mAODv2_MC'   : {
                        'isData'  : False ,
                        'samples' : 'LatinoTrees/AnalysisStep/test/crab/samples/samples_fall15_miniaodv2_25ns.py' ,
                        'dirExt'  : 'LatinoTrees' ,
                        #'gDocID'  : '1wH73CYA_T4KMkl1Cw-xLTj8YG7OPqayDnP53N-lZwFQ' ,
                        'puData'  : '/afs/cern.ch/user/x/xjanssen/public/Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON_v2_from256630_PileupHistogram.root' ,
                      } ,

  '22Jan_Run2015D_16Dec2015' : {
                        'isData'  : True ,
                        'samples' : 'LatinoTrees/AnalysisStep/test/crab/samples/samples_dataD_16Dec2015-v1_25ns_StarWars.py' ,
                        'dirExt'  : 'LatinoTrees' ,
                        'reName'  : { 
                                       'DoubleEG_Run2015D_25ns-16Dec2015-v2'       : 'Run2015D_16Dec2015_DoubleEG' ,
                                       'DoubleMuon_Run2015D_25ns-16Dec2015-v1'     : 'Run2015D_16Dec2015_DoubleMuon' ,
                                       'MuonEG_Run2015D_25ns-16Dec2015-v1'         : 'Run2015D_16Dec2015_MuonEG' , 
                                       'SingleElectron_Run2015D_25ns-16Dec2015-v1' : 'Run2015D_16Dec2015_SingleElectron' ,
                                       'SingleMuon_Run2015D_25ns-16Dec2015-v1'     : 'Run2015D_16Dec2015_SingleMuon' ,
                                      #'MET_Run2015D_25ns-16Dec2015-v1'            : 'Run2015D_16Dec2015_MET' ,
                                      #'SinglePhoton_Run2015D_25ns-16Dec2015-v1'   : 'Run2015D_16Dec2015_SinglePhoton' ,
                                    }
                      } ,

  '22Jan_Run2015C_16Dec2015' : {
                        'isData'  : True ,
                        'samples' : 'LatinoTrees/AnalysisStep/test/crab/samples/samples_dataC_16Dec2015-v1_25ns_StarWars.py',
                        'dirExt'  : 'LatinoTrees' ,
                        'reName'  : {
                                       'DoubleEG_Run2015C_25ns-16Dec2015-v1'       : 'Run2015C_16Dec2015_DoubleEG' ,
                                       'DoubleMuon_Run2015C_25ns-16Dec2015-v1'     : 'Run2015C_16Dec2015_DoubleMuon' ,
                                       'MuonEG_Run2015C_25ns-16Dec2015-v1'         : 'Run2015C_16Dec2015_MuonEG' ,
                                       'SingleElectron_Run2015C_25ns-16Dec2015-v1' : 'Run2015C_16Dec2015_SingleElectron' ,
                                       'SingleMuon_Run2015C_25ns-16Dec2015-v1'     : 'Run2015C_16Dec2015_SingleMuon' ,
                                   }
                      } ,

  '03Mar_Run2015D_16Dec2015' : {
                        'isData'  : True ,
                        'samples' : 'LatinoTrees/AnalysisStep/test/crab/samples/samples_dataD_16Dec2015-v1_25ns_StarWars.py' ,
                        'dirExt'  : 'LatinoTrees' ,
                        'reName'  : {
                                       'DoubleEG_Run2015D_25ns-16Dec2015-v2'       : 'Run2015D_16Dec2015_DoubleEG' ,
                                       'DoubleMuon_Run2015D_25ns-16Dec2015-v1'     : 'Run2015D_16Dec2015_DoubleMuon' ,
                                       'MuonEG_Run2015D_25ns-16Dec2015-v1'         : 'Run2015D_16Dec2015_MuonEG' ,
                                       'SingleElectron_Run2015D_25ns-16Dec2015-v1' : 'Run2015D_16Dec2015_SingleElectron' ,
                                       'SingleMuon_Run2015D_25ns-16Dec2015-v1'     : 'Run2015D_16Dec2015_SingleMuon' ,
                                      #'MET_Run2015D_25ns-16Dec2015-v1'            : 'Run2015D_16Dec2015_MET' ,
                                      #'SinglePhoton_Run2015D_25ns-16Dec2015-v1'   : 'Run2015D_16Dec2015_SinglePhoton' ,
                                    }
                      } ,

  '03Mar_Run2015C_16Dec2015' : {
                        'isData'  : True ,
                        'samples' : 'LatinoTrees/AnalysisStep/test/crab/samples/samples_dataC_16Dec2015-v1_25ns_StarWars.py',
                        'dirExt'  : 'LatinoTrees' ,
                        'reName'  : {
                                       'DoubleEG_Run2015C_25ns-16Dec2015-v1'       : 'Run2015C_16Dec2015_DoubleEG' ,
                                       'DoubleMuon_Run2015C_25ns-16Dec2015-v1'     : 'Run2015C_16Dec2015_DoubleMuon' ,
                                       'MuonEG_Run2015C_25ns-16Dec2015-v1'         : 'Run2015C_16Dec2015_MuonEG' ,
                                       'SingleElectron_Run2015C_25ns-16Dec2015-v1' : 'Run2015C_16Dec2015_SingleElectron' ,
                                       'SingleMuon_Run2015C_25ns-16Dec2015-v1'     : 'Run2015C_16Dec2015_SingleMuon' ,
                                   }
                      } ,


}



# ---- Steps
# .... .... this is defined by mkGardener in "-s" "--steps" option
# .... .... if it is a "chain", it means that the intermediate steps are NOT saved
# .... ....    e.g. 'puadder','baseW','wwNLL' ---> only after all steps the folder will be saved on eos

Steps= {

# ... Chains

  'MC' :       {
                  'isChain'    : True ,
                  'do4MC'      : True , 
                  'do4Data'    : False,
                  'subTargets' : ['puadder','baseW','wwNLL']
                },

  'MCl2sel' :       {
                  'isChain'    : True ,
                  'do4MC'      : True ,
                  'do4Data'    : False,
                  'subTargets' : ['puadder','baseW','wwNLL','l2sel','genVariables']
                },

  'MCl2loose' :       {
                  'isChain'    : True ,
                  'do4MC'      : True ,
                  'do4Data'    : False,
                  'subTargets' : ['l2loose','puadder','baseW','wwNLL','genVariables'],
#                 'onlySample' : [
#                                 # DY 
#                                 'DYJetsToLL_M-10to50','DYJetsToLL_M-50','DYJetsToLL_M-10to50ext3',
#                                 # Top
#                                 'TTTo2L2Nu',
#                                 'ST_t-channel_antitop','ST_t-channel_top',
#                                 'ST_tW_antitop','ST_tW_top',
#                                 # VV (including WW) 
#                                 'WWTo2L2Nu','GluGluWWTo2L2Nu_MCFM','GluGluWWTo2L2NuHiggs_MCFM',
#                                 'WZTo3LNu',
#                                 'ZZ','Zg',
#                                 'ZZTo2L2Nu','ZZTo2L2Q','ZZTo4L',
#                                 'Wg_AMCNLOFXFX',
#                                 # VVV
#                                 'WZZ','ZZZ','WWZ',
#                                 # Higgs 
#                                 'GluGluHToTauTau_M125', 'GluGluHToWWTo2L2Nu_M125','GluGluHToWWTo2L2NuPowheg_M125',
#                                 'GluGluHToWWTo2L2Nu_alternative_M125','VBFHToWWTo2L2Nu_alternative_M125',
#                                 'HWminusJ_HToTauTau_M125', 'HWminusJ_HToWW_M125',
#                                 'HWplusJ_HToTauTau_M125', 'HWplusJ_HToWW_M125',
#                                 'HZJ_HToTauTau_M125', 'HZJ_HToWW_M125',
#                                 'VBFHToTauTau_M125', 'VBFHToWWTo2L2Nu_M125',
#                                 'ggZH_HToWW_M125', # missing ggZHToTauTau
#                                 # PS
#                                 'GluGluHToWWTo2L2NuHerwigPS_M125','VBFHToWWTo2L2NuHerwigPS_M125','WWTo2L2NuHerwigPS',
#                                 # UE
#                                 'GluGluHToWWTo2L2Nu_M125_CUETDown',
#                                 'GluGluHToWWTo2L2Nu_M125_CUETUp',
#                                 'VBFHToWWTo2L2Nu_M125_CUETDown',
#                                 'VBFHToWWTo2L2Nu_M125_CUETUp',
#                                 'WWTo2L2Nu_CUETDown',
#                                 'WWTo2L2Nu_CUETUp',
#                                ] ,

                },

  'MCl1loose' :       {
                  'isChain'    : True ,
                  'do4MC'      : True ,
                  'do4Data'    : False,
                  'subTargets' : ['l1loose','puadder','baseW','wwNLL','genVariables'],
                  'onlySample' : [
                                  #### DY 
                                  'DYJetsToLL_M-10to50','DYJetsToLL_M-50','DYJetsToLL_M-10to50ext3',',DYJetsToLL_M-50-LO',
                                  ####
                                  'WJetsToLNu','WJetsToLNu_HT100_200','WJetsToLNu_HT200_400','WJetsToLNu_HT400_600','WJetsToLNu_HT600_800',
                                  'WJetsToLNu_HT800_1200','WJetsToLNu_HT1200_2500','WJetsToLNu_HT2500_inf',
                                  ####
                                  'QCD_Pt-15to20_EMEnriched', 'QCD_Pt-20to30_EMEnriched', 'QCD_Pt-30to50_EMEnriched', 'QCD_Pt-50to80_EMEnriched',
                                  'QCD_Pt-20toInf_MuEnrichedPt15',

                                  #### Top
                                  #'TTTo2L2Nu',
                                  #'ST_t-channel_antitop','ST_t-channel_top',
                                  #'ST_tW_antitop','ST_tW_top',
                                  #### VV (including WW) 
                                  #'WWTo2L2Nu','GluGluWWTo2L2Nu_MCFM','GluGluWWTo2L2NuHiggs_MCFM',
                                  #'WZTo3LNu',
                                  #'ZZ','Zg',
                                  #'ZZTo2L2Nu','ZZTo2L2Q','ZZTo4L',
                                  #'Wg_AMCNLOFXFX',
                                  ### VVV
                                  #'WZZ','ZZZ','WWZ',
                                  #### Higgs 
                                  #'GluGluHToTauTau_M125', 'GluGluHToWWTo2L2Nu_M125','GluGluHToWWTo2L2NuPowheg_M125',
                                  #'GluGluHToWWTo2L2Nu_alternative_M125','VBFHToWWTo2L2Nu_alternative_M125',
                                  #'HWminusJ_HToTauTau_M125', 'HWminusJ_HToWW_M125',
                                  #'HWplusJ_HToTauTau_M125', 'HWplusJ_HToWW_M125',
                                  #'HZJ_HToTauTau_M125', 'HZJ_HToWW_M125',
                                  #'VBFHToTauTau_M125', 'VBFHToWWTo2L2Nu_M125',
                                  #'ggZH_HToWW_M125', # missing ggZHToTauTau
                                  # PS
                                  #'GluGluHToWWTo2L2NuHerwigPS_M125','VBFHToWWTo2L2NuHerwigPS_M125','WWTo2L2NuHerwigPS',
                                  # UE
                                  #'GluGluHToWWTo2L2Nu_M125_CUETDown',
                                  #'GluGluHToWWTo2L2Nu_M125_CUETUp',
                                  #'VBFHToWWTo2L2Nu_M125_CUETDown',
                                  #'VBFHToWWTo2L2Nu_M125_CUETUp',
                                  #'WWTo2L2Nu_CUETDown',
                                  #'WWTo2L2Nu_CUETUp',
                                 ] ,

                },

  'MCWgStarsel' : {
                  'isChain'    : True ,
                  'do4MC'      : True ,
                  'do4Data'    : False,
                  'subTargets' : ['do_WgStarsel','puadder','baseW','wwNLL','genVariables'],
                  'onlySample' : [
                                   'Wg500','Wg_AMCNLOFXFX','WZTo3LNu',
                                 ]
                },

  'WgStarsel' : {
                  'isChain'    : True ,
                  'do4MC'      : False ,
                  'do4Data'    : True,
                  'subTargets' : ['do_WgStarsel'],
                  'onlySample' : [
                                   'Run2015C_16Dec2015_DoubleMuon' , 'Run2015C_16Dec2015_SingleElectron' , 'Run2015C_16Dec2015_SingleMuon',
                                   'Run2015D_16Dec2015_DoubleMuon' , 'Run2015D_16Dec2015_SingleElectron' , 'Run2015D_16Dec2015_SingleMuon',
                                 ]
                },


  'bSFL2Eff'   :   {
                  'isChain'    : True ,
                  'do4MC'      : True ,
                  'do4Data'    : True ,
                  'subTargets' : ['bPogSF','TrigEff','IdIsoSC'],
                },
      

  'EpTCorr'       :  {
                  'isChain'    : True ,
                  'do4MC'      : True ,
                  'do4Data'    : True ,
                  'subTargets' : ['do_lpTCorrMC','do_lpTCorrData','l2kin'],
                },

  'bSFL2pTEff'   :   {
                  'isChain'    : True ,
                  'do4MC'      : True ,
                  'do4Data'    : True ,
                  'subTargets' : ['do_lpTCorrMC','do_lpTCorrData','bPogSF','TrigEff','IdIsoSC','l2kin'],
                  'onlySample' : [
                                  # DY 
                                  'DYJetsToLL_M-10to50','DYJetsToLL_M-50','DYJetsToLL_M-10to50ext3', 'DYJetsToLL_M-50-LO' ,
                                  # Top
                                  'TTTo2L2Nu',
                                  'ST_t-channel_antitop','ST_t-channel_top',
                                  'ST_tW_antitop','ST_tW_top',
                                  # VV (including WW) 
                                  'WWTo2L2Nu','GluGluWWTo2L2Nu_MCFM','GluGluWWTo2L2NuHiggs_MCFM',
                                  'WZTo3LNu',
                                  'ZZ','Zg',
                                  'ZZTo2L2Nu','ZZTo2L2Q','ZZTo4L',
                                  'Wg_AMCNLOFXFX',
                                  # VVV
                                  'WZZ','ZZZ','WWZ',
                                  # Higgs 
                                  'GluGluHToTauTau_M125', 'GluGluHToWWTo2L2Nu_M125','GluGluHToWWTo2L2NuPowheg_M125',
                                  'GluGluHToWWTo2L2Nu_alternative_M125','VBFHToWWTo2L2Nu_alternative_M125',
                                  'HWminusJ_HToTauTau_M125', 'HWminusJ_HToWW_M125',
                                  'HWplusJ_HToTauTau_M125', 'HWplusJ_HToWW_M125',
                                  'HZJ_HToTauTau_M125', 'HZJ_HToWW_M125',
                                  'VBFHToTauTau_M125', 'VBFHToWWTo2L2Nu_M125',
                                  'ggZH_HToWW_M125', # missing ggZHToTauTau
                                  # PS
                                  'GluGluHToWWTo2L2NuHerwigPS_M125','VBFHToWWTo2L2NuHerwigPS_M125','WWTo2L2NuHerwigPS',
                                  # UE
                                  'GluGluHToWWTo2L2Nu_M125_CUETDown',
                                  'GluGluHToWWTo2L2Nu_M125_CUETUp',
                                  'VBFHToWWTo2L2Nu_M125_CUETDown',
                                  'VBFHToWWTo2L2Nu_M125_CUETUp',
                                  'WWTo2L2Nu_CUETDown',
                                  'WWTo2L2Nu_CUETUp',
				  # VBS
				  'WpWpJJ_EWK','WpWpJJ_EWK_QCD','WpWpJJ_QCD','WW_DoubleScattering','WLLJJToLNu_M-4to60_EWK_QCD','WLLJJToLNu_M-60_EWK_QCD',
                                 ] ,
                },



  'L2Eff'  :   {
                  'isChain'    : True ,
                  'do4MC'      : True ,
                  'do4Data'    : False,
                  'subTargets' : ['TrigEff','IdIsoSC'],
#                 'onlySample' : ['DYJetsToLL_M-10to50','DYJetsToLL_M-50','WJetsToLNu','TTTo2L2Nu','TTJets',
#                                 'ST_t-channel','ST_tW_antitop','ST_tW_top','WWTo2L2Nu','WZTo3LNu',
#                                 'WZZ','ZZZ','GluGluWWTo2L2Nu_MCFM',
#                                 'GluGluHToTauTau_M125', 'GluGluHToWWTo2L2Nu_M125',
#                                 'HWminusJ_HToTauTau_M125', 'HWminusJ_HToWW_M125',
#                                 'HWplusJ_HToTauTau_M125', 'HWplusJ_HToWW_M125',
#                                 'HZJ_HToTauTau_M125', 'HZJ_HToWW_M125',
#                                 'VBFHToTauTau_M125', 'VBFHToWWTo2L2Nu_M125',
#                                 'Wg','ZZTo4L','WWZ',
#                                ] ,
                 },

  'JESup'     :  {
                  'isChain'    : True ,
                  'do4MC'      : True ,
                  'do4Data'    : False,
                  'subTargets' : ['do_JESup','bPogSF','l2kin'],
                  'onlySample' : [
                                  # DY 
                                  'DYJetsToLL_M-10to50','DYJetsToLL_M-50','DYJetsToLL_M-10to50ext3',
                                  # Top
                                  'TTTo2L2Nu',
                                  'ST_t-channel_antitop','ST_t-channel_top',
                                  'ST_tW_antitop','ST_tW_top',
                                  # VV (including WW) 
                                  'WWTo2L2Nu','GluGluWWTo2L2Nu_MCFM','GluGluWWTo2L2NuHiggs_MCFM',
                                  'WZTo3LNu',
                                  'ZZ','Zg',
                                  'ZZTo2L2Nu','ZZTo2L2Q','ZZTo4L',
                                  'Wg_AMCNLOFXFX',
                                  # VVV
                                  'WZZ','ZZZ','WWZ',
                                  # Higgs 
                                  'GluGluHToTauTau_M125', 'GluGluHToWWTo2L2Nu_M125','GluGluHToWWTo2L2NuPowheg_M125',
                                  'GluGluHToWWTo2L2Nu_alternative_M125','VBFHToWWTo2L2Nu_alternative_M125',
                                  'HWminusJ_HToTauTau_M125', 'HWminusJ_HToWW_M125',
                                  'HWplusJ_HToTauTau_M125', 'HWplusJ_HToWW_M125',
                                  'HZJ_HToTauTau_M125', 'HZJ_HToWW_M125',
                                  'VBFHToTauTau_M125', 'VBFHToWWTo2L2Nu_M125',
                                  'ggZH_HToWW_M125', # missing ggZHToTauTau
                                 ] ,
                },

  'JESdo'     :  {
                  'isChain'    : True ,
                  'do4MC'      : True ,
                  'do4Data'    : False,
                  'subTargets' : ['do_JESdo','bPogSF','l2kin'],
                  'onlySample' : [
                                  # DY 
                                  'DYJetsToLL_M-10to50','DYJetsToLL_M-50','DYJetsToLL_M-10to50ext3',
                                  # Top
                                  'TTTo2L2Nu',
                                  'ST_t-channel_antitop','ST_t-channel_top',
                                  'ST_tW_antitop','ST_tW_top',
                                  # VV (including WW) 
                                  'WWTo2L2Nu','GluGluWWTo2L2Nu_MCFM','GluGluWWTo2L2NuHiggs_MCFM',
                                  'WZTo3LNu',
                                  'ZZ','Zg',
                                  'ZZTo2L2Nu','ZZTo2L2Q','ZZTo4L',
                                  'Wg_AMCNLOFXFX',
                                  # VVV
                                  'WZZ','ZZZ','WWZ',
                                  # Higgs 
                                  'GluGluHToTauTau_M125', 'GluGluHToWWTo2L2Nu_M125','GluGluHToWWTo2L2NuPowheg_M125',
                                  'GluGluHToWWTo2L2Nu_alternative_M125','VBFHToWWTo2L2Nu_alternative_M125',
                                  'HWminusJ_HToTauTau_M125', 'HWminusJ_HToWW_M125',
                                  'HWplusJ_HToTauTau_M125', 'HWplusJ_HToWW_M125',
                                  'HZJ_HToTauTau_M125', 'HZJ_HToWW_M125',
                                  'VBFHToTauTau_M125', 'VBFHToWWTo2L2Nu_M125',
                                  'ggZH_HToWW_M125', # missing ggZHToTauTau
                                 ] ,
                },


  'JESMaxup'     :  {
                  'isChain'    : True ,
                  'do4MC'      : True ,
                  'do4Data'    : False,
                  'subTargets' : ['do_JESMaxup','bPogSF','l2kin'],
                  'onlySample' : [
                                  # DY 
                                  'DYJetsToLL_M-10to50','DYJetsToLL_M-50','DYJetsToLL_M-10to50ext3',
                                  # Top
                                  'TTTo2L2Nu',
                                  'ST_t-channel_antitop','ST_t-channel_top',
                                  'ST_tW_antitop','ST_tW_top',
                                  # VV (including WW) 
                                  'WWTo2L2Nu','GluGluWWTo2L2Nu_MCFM','GluGluWWTo2L2NuHiggs_MCFM',
                                  'WZTo3LNu',
                                  'ZZ','Zg',
                                  'ZZTo2L2Nu','ZZTo2L2Q','ZZTo4L',
                                  'Wg_AMCNLOFXFX',
                                  # VVV
                                  'WZZ','ZZZ','WWZ',
                                  # Higgs 
                                  'GluGluHToTauTau_M125', 'GluGluHToWWTo2L2Nu_M125','GluGluHToWWTo2L2NuPowheg_M125',
                                  'GluGluHToWWTo2L2Nu_alternative_M125','VBFHToWWTo2L2Nu_alternative_M125',
                                  'HWminusJ_HToTauTau_M125', 'HWminusJ_HToWW_M125',
                                  'HWplusJ_HToTauTau_M125', 'HWplusJ_HToWW_M125',
                                  'HZJ_HToTauTau_M125', 'HZJ_HToWW_M125',
                                  'VBFHToTauTau_M125', 'VBFHToWWTo2L2Nu_M125',
                                  'ggZH_HToWW_M125', # missing ggZHToTauTau
                                 ] ,
                },

  'JESMaxdo'     :  {
                  'isChain'    : True ,
                  'do4MC'      : True ,
                  'do4Data'    : False,
                  'subTargets' : ['do_JESMaxdo','bPogSF','l2kin'],
                  'onlySample' : [
                                  # DY 
                                  'DYJetsToLL_M-10to50','DYJetsToLL_M-50','DYJetsToLL_M-10to50ext3',
                                  # Top
                                  'TTTo2L2Nu',
                                  'ST_t-channel_antitop','ST_t-channel_top',
                                  'ST_tW_antitop','ST_tW_top',
                                  # VV (including WW) 
                                  'WWTo2L2Nu','GluGluWWTo2L2Nu_MCFM','GluGluWWTo2L2NuHiggs_MCFM',
                                  'WZTo3LNu',
                                  'ZZ','Zg',
                                  'ZZTo2L2Nu','ZZTo2L2Q','ZZTo4L',
                                  'Wg_AMCNLOFXFX',
                                  # VVV
                                  'WZZ','ZZZ','WWZ',
                                  # Higgs 
                                  'GluGluHToTauTau_M125', 'GluGluHToWWTo2L2Nu_M125','GluGluHToWWTo2L2NuPowheg_M125',
                                  'GluGluHToWWTo2L2Nu_alternative_M125','VBFHToWWTo2L2Nu_alternative_M125',
                                  'HWminusJ_HToTauTau_M125', 'HWminusJ_HToWW_M125',
                                  'HWplusJ_HToTauTau_M125', 'HWplusJ_HToWW_M125',
                                  'HZJ_HToTauTau_M125', 'HZJ_HToWW_M125',
                                  'VBFHToTauTau_M125', 'VBFHToWWTo2L2Nu_M125',
                                  'ggZH_HToWW_M125', # missing ggZHToTauTau
                                 ] ,
                },

  'lpTCorr' : {
                 'isChain'    : True ,
                  'do4MC'      : True ,
                  'do4Data'    : False,
                  'subTargets' : ['do_lpTCorrMC','do_lpTCorrData','l2kin'],
               },



  'LepElepTup':  {
                  'isChain'    : True ,
                  'do4MC'      : True ,
                  'do4Data'    : False,
                  'subTargets' : ['do_LepElepTup','TrigEff','IdIsoSC','l2kin'],
                  'onlySample' : [
                                  # DY 
                                  'DYJetsToLL_M-10to50','DYJetsToLL_M-50','DYJetsToLL_M-10to50ext3',
                                  # Top
                                  'TTTo2L2Nu',
                                  'ST_t-channel_antitop','ST_t-channel_top',
                                  'ST_tW_antitop','ST_tW_top',
                                  # VV (including WW) 
                                  'WWTo2L2Nu','GluGluWWTo2L2Nu_MCFM','GluGluWWTo2L2NuHiggs_MCFM','GluGluHToWWTo2L2NuPowheg_M125',
                                  'WZTo3LNu',
                                  'ZZ','Zg',
                                  'ZZTo2L2Nu','ZZTo2L2Q','ZZTo4L',
                                  'Wg_AMCNLOFXFX',
                                  # VVV
                                  'WZZ','ZZZ','WWZ','WWW',
                                  # Higgs 
                                  'GluGluHToTauTau_M125', 'GluGluHToWWTo2L2Nu_M125','GluGluHToWWTo2L2NuPowheg_M125',
                                  'GluGluHToWWTo2L2Nu_alternative_M125','VBFHToWWTo2L2Nu_alternative_M125',
                                  'HWminusJ_HToTauTau_M125', 'HWminusJ_HToWW_M125',
                                  'HWplusJ_HToTauTau_M125', 'HWplusJ_HToWW_M125',
                                  'HZJ_HToTauTau_M125', 'HZJ_HToWW_M125',
                                  'VBFHToTauTau_M125', 'VBFHToWWTo2L2Nu_M125',
                                  'ggZH_HToWW_M125', # missing ggZHToTauTau
                                 ] ,
              },

  'LepElepTdo':  {
                  'isChain'    : True ,
                  'do4MC'      : True ,
                  'do4Data'    : False,
                  'subTargets' : ['do_LepElepTdo','TrigEff','IdIsoSC','l2kin'],
                  'onlySample' : [
                                  # DY 
                                  'DYJetsToLL_M-10to50','DYJetsToLL_M-50','DYJetsToLL_M-10to50ext3',
                                  # Top
                                  'TTTo2L2Nu',
                                  'ST_t-channel_antitop','ST_t-channel_top',
                                  'ST_tW_antitop','ST_tW_top',
                                  # VV (including WW) 
                                  'WWTo2L2Nu','GluGluWWTo2L2Nu_MCFM','GluGluWWTo2L2NuHiggs_MCFM',
                                  'WZTo3LNu',
                                  'ZZ','Zg',
                                  'ZZTo2L2Nu','ZZTo2L2Q','ZZTo4L',
                                  'Wg_AMCNLOFXFX',
                                  # VVV
                                  'WZZ','ZZZ','WWZ','WWW',
                                  # Higgs 
                                  'GluGluHToTauTau_M125', 'GluGluHToWWTo2L2Nu_M125','GluGluHToWWTo2L2NuPowheg_M125',
                                  'GluGluHToWWTo2L2Nu_alternative_M125','VBFHToWWTo2L2Nu_alternative_M125',
                                  'HWminusJ_HToTauTau_M125', 'HWminusJ_HToWW_M125',
                                  'HWplusJ_HToTauTau_M125', 'HWplusJ_HToWW_M125',
                                  'HZJ_HToTauTau_M125', 'HZJ_HToWW_M125',
                                  'VBFHToTauTau_M125', 'VBFHToWWTo2L2Nu_M125',
                                  'ggZH_HToWW_M125', # missing ggZHToTauTau
                                 ] ,
              },


  'LepMupTup':  {
                  'isChain'    : True ,
                  'do4MC'      : True ,
                  'do4Data'    : False,
                  'subTargets' : ['do_LepMupTup','TrigEff','IdIsoSC','l2kin'],
                  'onlySample' : [
                                  # DY 
                                  'DYJetsToLL_M-10to50','DYJetsToLL_M-50','DYJetsToLL_M-10to50ext3',
                                  # Top
                                  'TTTo2L2Nu',
                                  'ST_t-channel_antitop','ST_t-channel_top',
                                  'ST_tW_antitop','ST_tW_top',
                                  # VV (including WW) 
                                  'WWTo2L2Nu','GluGluWWTo2L2Nu_MCFM','GluGluWWTo2L2NuHiggs_MCFM',
                                  'WZTo3LNu',
                                  'ZZ','Zg',
                                  'ZZTo2L2Nu','ZZTo2L2Q','ZZTo4L',
                                  'Wg_AMCNLOFXFX',
                                  # VVV
                                  'WZZ','ZZZ','WWZ','WWW',
                                  # Higgs 
                                  'GluGluHToTauTau_M125', 'GluGluHToWWTo2L2Nu_M125','GluGluHToWWTo2L2NuPowheg_M125',
                                  'GluGluHToWWTo2L2Nu_alternative_M125','VBFHToWWTo2L2Nu_alternative_M125',
                                  'HWminusJ_HToTauTau_M125', 'HWminusJ_HToWW_M125',
                                  'HWplusJ_HToTauTau_M125', 'HWplusJ_HToWW_M125',
                                  'HZJ_HToTauTau_M125', 'HZJ_HToWW_M125',
                                  'VBFHToTauTau_M125', 'VBFHToWWTo2L2Nu_M125',
                                  'ggZH_HToWW_M125', # missing ggZHToTauTau
                                 ] ,
              },

  'LepMupTdo':  {
                  'isChain'    : True ,
                  'do4MC'      : True ,
                  'do4Data'    : False,
                  'subTargets' : ['do_LepMupTdo','TrigEff','IdIsoSC','l2kin'],
                  'onlySample' : [
                                  # DY 
                                  'DYJetsToLL_M-10to50','DYJetsToLL_M-50','DYJetsToLL_M-10to50ext3',
                                  # Top
                                  'TTTo2L2Nu',
                                  'ST_t-channel_antitop','ST_t-channel_top',
                                  'ST_tW_antitop','ST_tW_top',
                                  # VV (including WW) 
                                  'WWTo2L2Nu','GluGluWWTo2L2Nu_MCFM','GluGluWWTo2L2NuHiggs_MCFM',
                                  'GluGluHToWWTo2L2Nu_alternative_M125','VBFHToWWTo2L2Nu_alternative_M125',
                                  'WZTo3LNu',
                                  'ZZ','Zg',
                                  'ZZTo2L2Nu','ZZTo2L2Q','ZZTo4L',
                                  'Wg_AMCNLOFXFX',
                                  # VVV
                                  'WZZ','ZZZ','WWZ','WWW',
                                  # Higgs 
                                  'GluGluHToTauTau_M125', 'GluGluHToWWTo2L2Nu_M125','GluGluHToWWTo2L2NuPowheg_M125',
                                  'GluGluHToWWTo2L2Nu_alternative_M125','VBFHToWWTo2L2Nu_alternative_M125',
                                  'HWminusJ_HToTauTau_M125', 'HWminusJ_HToWW_M125',
                                  'HWplusJ_HToTauTau_M125', 'HWplusJ_HToWW_M125',
                                  'HZJ_HToTauTau_M125', 'HZJ_HToWW_M125',
                                  'VBFHToTauTau_M125', 'VBFHToWWTo2L2Nu_M125',
                                  'ggZH_HToWW_M125', # missing ggZHToTauTau
                                 ] ,
              },
                  
                  

   'METup':  {
                  'isChain'    : True ,
                  'do4MC'      : True ,
                  'do4Data'    : False,
                  'subTargets' : ['do_METup','l2kin'],
                  'onlySample' : [
                                  # DY 
                                  'DYJetsToLL_M-10to50','DYJetsToLL_M-50','DYJetsToLL_M-10to50ext3',
                                  # Top
                                  'TTTo2L2Nu',
                                  'ST_t-channel_antitop','ST_t-channel_top',
                                  'ST_tW_antitop','ST_tW_top',
                                  # VV (including WW) 
                                  'WWTo2L2Nu','GluGluWWTo2L2Nu_MCFM','GluGluWWTo2L2NuHiggs_MCFM',
                                  'WZTo3LNu',
                                  'ZZ','Zg',
                                  'ZZTo2L2Nu','ZZTo2L2Q','ZZTo4L',
                                  'Wg_AMCNLOFXFX',
                                  # VVV
                                  'WZZ','ZZZ','WWZ','WWW',
                                  # Higgs 
                                  'GluGluHToTauTau_M125', 'GluGluHToWWTo2L2Nu_M125','GluGluHToWWTo2L2NuPowheg_M125',
                                  'GluGluHToWWTo2L2Nu_alternative_M125','VBFHToWWTo2L2Nu_alternative_M125',
                                  'HWminusJ_HToTauTau_M125', 'HWminusJ_HToWW_M125',
                                  'HWplusJ_HToTauTau_M125', 'HWplusJ_HToWW_M125',
                                  'HZJ_HToTauTau_M125', 'HZJ_HToWW_M125',
                                  'VBFHToTauTau_M125', 'VBFHToWWTo2L2Nu_M125',
                                  'ggZH_HToWW_M125', # missing ggZHToTauTau
                                 ] ,
              },

   'METdo':  {
                  'isChain'    : True ,
                  'do4MC'      : True ,
                  'do4Data'    : False,
                  'subTargets' : ['do_METdo','l2kin'],
                  'onlySample' : [
                                  # DY 
                                  'DYJetsToLL_M-10to50','DYJetsToLL_M-50','DYJetsToLL_M-10to50ext3',
                                  # Top
                                  'TTTo2L2Nu',
                                  'ST_t-channel_antitop','ST_t-channel_top',
                                  'ST_tW_antitop','ST_tW_top',
                                  # VV (including WW) 
                                  'WWTo2L2Nu','GluGluWWTo2L2Nu_MCFM','GluGluWWTo2L2NuHiggs_MCFM',
                                  'GluGluHToWWTo2L2Nu_alternative_M125','VBFHToWWTo2L2Nu_alternative_M125',
                                  'WZTo3LNu',
                                  'ZZ','Zg',
                                  'ZZTo2L2Nu','ZZTo2L2Q','ZZTo4L',
                                  'Wg_AMCNLOFXFX',
                                  # VVV
                                  'WZZ','ZZZ','WWZ','WWW',
                                  # Higgs 
                                  'GluGluHToTauTau_M125', 'GluGluHToWWTo2L2Nu_M125','GluGluHToWWTo2L2NuPowheg_M125',
                                  'HWminusJ_HToTauTau_M125', 'HWminusJ_HToWW_M125',
                                  'HWplusJ_HToTauTau_M125', 'HWplusJ_HToWW_M125',
                                  'HZJ_HToTauTau_M125', 'HZJ_HToWW_M125',
                                  'VBFHToTauTau_M125', 'VBFHToWWTo2L2Nu_M125',
                                  'ggZH_HToWW_M125', # missing ggZHToTauTau
                                 ] ,
              },

# ... Individual Steps

  'mcwghtcount':{ 
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'command'    : 'gardener.py mcweightscounter '
                },

# 'mcweights' : {
#                 'isChain'    : False ,
#                 'do4MC'      : True  ,
#                 'do4Data'    : False ,
#                 'command'    : 'gardener.py mcweightsfiller '
#               } ,

  'puadder'   : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'command'    : 'gardener.py puadder --data=RPLME_puData --HistName=pileup --branch=puW --kind=trpu '
                } ,

  'baseW'     : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'command'    : 'gardener.py adder -v \'baseW/F=RPLME_baseW\' -v \'Xsec/F=RPLME_XSection\' '

                } ,

  'wwNLL'     : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'onlySample' : ['WWTo2L2Nu','WWTo2L2NuHerwigPS','WWTo2L2Nu_CUETUp','WWTo2L2Nu_CUETDown'] ,
                  'command'    : 'gardener.py wwNLLcorrections -m \'powheg\' --cmssw RPLME_CMSSW'
                },

  'genVariables'  : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'command'    : 'gardener.py genvariablesfiller ',
                  'onlySample' : [
                                  # DY 
                                  'DYJetsToLL_M-10to50','DYJetsToLL_M-50','DYJetsToLL_M-10to50ext3',
                                  ]

                },

  'l2sel'    : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'command'    : 'gardener.py l2selfiller --kind 1 --cmssw RPLME_CMSSW'
               },

  'l2kin'    : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'command'    : 'gardener.py l2kinfiller --cmssw RPLME_CMSSW'
               },

  'l2loose'    : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'command'    : 'gardener.py l2selfiller --kind 2 --cmssw RPLME_CMSSW --selection 1'
               },

  'l2tight'    : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'command'    : 'gardener.py filter -f \'std_vector_lepton_isTightLepton[0]>0.5 && std_vector_lepton_isTightLepton[1]>0.5\' '
               },

  'l1loose'    : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'command'    : 'gardener.py l1selfiller --kind 2 --cmssw RPLME_CMSSW'
               },

  'do_WgStarsel' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'command'    : 'gardener.py l2selfiller --kind 3 --cmssw RPLME_CMSSW'
               },


  'IdIsoSC'  : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'command'    : 'gardener.py idisofiller'
               },

  'TrigEff'  : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'command'    : 'gardener.py efftfiller'
               },


  'hadd'     : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'bigSamples' : ['DYJetsToLL_M-50','DY2JetsToLL','ZZTo2L2Q','DYJetsToLL_M-50-LO'],
               },

  'do_lpTCorrMC'  : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'command'    : 'gardener.py letPtCorrector --isData=0 '
                } ,

  'do_lpTCorrData'  : {
                  'isChain'    : False ,
                  'do4MC'      : False  ,
                  'do4Data'    : True ,
                  'command'    : 'gardener.py letPtCorrector --isData=1 '
                } ,


  'do_JESup'    : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'command'    : 'gardener.py JESTreeMaker -k 1 '
                } ,

  'do_JESdo'    : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'command'    : 'gardener.py JESTreeMaker -k -1 '
                } ,
  
  'do_JESMaxup'    : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'command'    : 'gardener.py JESTreeMaker -k 1 --maxUncertainty '
                } ,

  'do_JESMaxdo'    : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'command'    : 'gardener.py JESTreeMaker -k -1 --maxUncertainty'
                } ,

 
  'bPogSF'   :{
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'command'    : 'gardener.py btagPogScaleFactors '
              },

  'do_LepElepTup'    : {
                   'isChain'    : False ,
                   'do4MC'      : True  ,
                   'do4Data'    : False ,
                   'command'    : 'gardener.py LeppTScalerTreeMaker --lepFlavourToChange ele    -v 1.0'
                 } ,
  
  'do_LepElepTdo'    : {
                   'isChain'    : False ,
                   'do4MC'      : True  ,
                   'do4Data'    : False ,
                   'command'    : 'gardener.py LeppTScalerTreeMaker --lepFlavourToChange ele   -v -1.0'
                 } ,
  
  'do_LepMupTup'    : {
                   'isChain'    : False ,
                   'do4MC'      : True  ,
                   'do4Data'    : False ,
                   'command'    : 'gardener.py LeppTScalerTreeMaker --lepFlavourToChange mu    -v 1.0'
                 } ,
  
  'do_LepMupTdo'    : {
                   'isChain'    : False ,
                   'do4MC'      : True  ,
                   'do4Data'    : False ,
                   'command'    : 'gardener.py LeppTScalerTreeMaker --lepFlavourToChange mu   -v -1.0'
                 } ,
  
  'do_METup'        : {
                   'isChain'    : False ,
                   'do4MC'      : True  ,
                   'do4Data'    : False ,
                   'command'    : 'gardener.py metUncertainty --kind=Up --cmssw=RPLME_CMSSW --lepton no   --jetresolution no   --unclustered no  '
                 } ,
  
  'do_METdo'        : {
                   'isChain'    : False ,
                   'do4MC'      : True  ,
                   'do4Data'    : False ,
                   'command'    : 'gardener.py metUncertainty --kind=Dn --cmssw=RPLME_CMSSW --lepton no   --jetresolution no   --unclustered no '
                 } ,
  
   # fix datasets names
  'fixdataset_Herwig_nuisance':  {
               'isChain'    : False ,
               'do4MC'      : True ,
               'do4Data'    : False,
               'onlySample' : [
                               #  qqWW
                               'WWTo2L2NuHerwigPS',
                               # ggH
                               'GluGluHToWWTo2L2NuHerwigPS_M125' ,
                               # VBF
                               'VBFHToWWTo2L2NuHerwigPS_M125'
                              ] ,
               'command'    : 'gardener.py adder -v \'dataset/F=42\'  '
           },


  'wwSel'    : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'command'    : 'gardener.py filter -f \' mll>12 && std_vector_lepton_pt[0]>20 && std_vector_lepton_pt[1]>10 && std_vector_lepton_pt[2]<10 && metPfType1 > 20 && ptll > 30 && (std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -11*13) \' '
           },

}

