#!/bin/bash

rm -f multicrab.cfg
touch multicrab.cfg

echo "[MULTICRAB]" >> multicrab.cfg
echo "cfg=digi_crab.cfg" >> multicrab.cfg
echo "" >> multicrab.cfg

for mass in `seq 110 5 160`
do
  echo "[crab_digi_WW_$mass]" >> multicrab.cfg
  echo "CMSSW.datasetpath=/ZH_ZToLL_HToWW_WWTo2LNu-$mass-7TeV-pythia6/friis-ZH_ZToLL_HToWW_WWTo2LNu-$mass-7TeV-pythia6-6ce0bad598f569ccbf493e88b5e333e7/USER" >> multicrab.cfg
  echo "USER.publish_data_name=ZH_ZToLL_HToWW_WWTo2LNu-$mass-7TeV-pythia6" >> multicrab.cfg
  echo "" >> multicrab.cfg

  echo "[crab_digi_TT_$mass]" >> multicrab.cfg
  echo "CMSSW.datasetpath=/ZH_ZToLL_HToTauTau_M-$mass-7TeV-pythia6/friis-ZH_ZToLL_HToTauTau_M-$mass-7TeV-pythia6-a80cb94964a5eab22807f871801e3473/USER" >> multicrab.cfg
  echo "USER.publish_data_name=ZH_ZToLL_HToTauTau_M-$mass-7TeV-pythia6" >> multicrab.cfg
  echo "" >> multicrab.cfg
done

