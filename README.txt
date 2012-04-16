A ZH -> tautau and friends private MC production
================================================

Instructions from Lindsey
------------------------

Forwarded conversationSubject: Instructions------------------------
From: Lindsey Gray <Lindsey.Gray@cern.ch>Date: Wed, Apr 11, 2012 at 4:39 PM
To: "Evan K. Friis" <evan.klose.friis@cern.ch>
You will need to have the following versions of CMSSW:

CMSSW_4_2_8_patch4 -- GEN-SIM / RECO
CMSSW_4_2_9_HLT1_patch1 - DIGI-HLT

step 1: create gen fragment (CMSSW_4_2_8_patch4)

cvs co -r CMSSW_4_2_8_patch4 Configuration/Generator
cp your_card_file.py Configuration/Generator
scram b
cmsDriver.py your_card_file.py -s GEN --conditions START42_V14B::All --eventcontent FEVTSIM --datatier GEN-SIM-RAW --pileup NoPileUp -n 10 --no_exec

You then setup crab with the appropriate config as input... random number seeds
and such are taken care of automatically if you don't specify anything:

CMSSW.generator = pythia

and generate however many events you need and publish this dataset.

step 2: SIM (CMSSW_4_2_8_patch4)
Ok, so you can combine this bit with the GEN step, but 500 events/job is about
the maximum you can do either way.
If you need to generate a large sample (> 500k events) generate the GEN
separately, just my opinion.

cmsDriver.py SIM -s SIM --conditions START42_V14B::All ----eventcontent RAWSIM
--datatier GEN-SIM-RAW --pileup NoPileUp -n 10 --no_exec

setup crab and run again, publish resulting data.

step 3: DIGI -> HLT (CMSSW_4_2_9_HLT1_patch1)

cmsDriver.py DIGI,L1,DIGI2RAW,HLT:GRun --conditions START42_V14B::All --pileup
mix_E7TeV_Fall2011_Reprocess_50ns_PoissonOOTPU_cfi --datamix NODATAMIXER
--eventcontent RAWSIM --datatier GEN-SIM-RAW -n 10 --no_exec

same thing again with crab

step 4: RECO (CMSSW_4_2_8_patch4)

cmsDriver.py REDIGI -s RAW2DIGI,L1Reco,RECO --conditions START42_V14B::All
--pileup NoPileUp --datamix NODATAMIXER --eventcontent AODSIM --datatier AODSIM
-n 10 --no_exec

and finally the same thing again with crab.

Combining steps together is something I can certainly *not* recommend since it
ends up just giving your jobs a larger failure rate. 
Even if publishing 4 datasets into DBS is a bit of a pain in the ass.

-Lindsey
----------
From: Lindsey Gray <Lindsey.Gray@cern.ch>Date: Wed, Apr 11, 2012 at 4:41 PM
To: "Evan K. Friis" <evan.klose.friis@cern.ch>
Minor correction:

cp your_card_file.py Configuration/Generator -> cp your_card_file.py
Configuration/Generator/python

very important otherwise cmsDriver.py dies.

-Lindsey



