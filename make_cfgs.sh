#!/bin/bash

# Generate ZH->ZWW and ZH->Ztautau cffs

output=CMSSW_4_2_8_patch4/src/Configuration/Generator/python/

for mass in `seq 110 5 160` 
do
  cat zh_tt_template.py | sed "s|HIGGSMASS|$mass|" > $output/PYTHIA6_Tauola_SM_H_2Tau_zh_mH${mass}_7TeV_cff.py
done

for mass in `seq 110 5 160` 
do
  cat zh_ww_template.py | sed "s|HIGGSMASS|$mass|" > $output/PYTHIA6_Tauola_SM_H_2W_2lnu_zh_mH${mass}_7TeV_cff.py
done
