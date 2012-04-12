#!/bin/bash 
for mass in `seq 110 5 160`
do
  echo $mass
  tt_psetname=PYTHIA6_Tauola_SM_H_2Tau_zh_mH110_7TeV_cff_py_GEN_SIM.py
  cat crab_gen_template.cfg | sed "s|PSET_NAME|$tt_psetname|g" | sed "s|PUBLISH_NAME|ZH_ZToLL_HToTauTau_M-$mass-7TeV-pythia6|g" > ZH_HTT_${mass}_crab.cfg
  ww_psetname=PYTHIA6_Tauola_SM_H_2W_2lnu_zh_mH110_7TeV_cff_py_GEN_SIM.py
  cat crab_gen_template.cfg | sed "s|PSET_NAME|$ww_psetname|g"  | sed "s|PUBLISH_NAME|ZH_ZToLL_HToWW_WWTo2LNu-$mass-7TeV-pythia6|g" > ZH_HWW_${mass}_crab.cfg
done

