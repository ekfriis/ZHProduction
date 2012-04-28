#!/bin/bash

rm -f multicrab.cfg
touch multicrab.cfg

echo "[MULTICRAB]" >> multicrab.cfg
echo "cfg=reco_crab.cfg" >> multicrab.cfg
echo "" >> multicrab.cfg

for mass in `seq 110 5 160`
do
  # NOTE THAT EVEN THOUGH HTOTAU IS IN DATASET NAME ITS OKAY, CRAB JUST SUCKS
  echo "[crab_reco_WW_$mass]" >> multicrab.cfg
  echo "CMSSW.datasetpath=/ZH_ZToLL_HToWW_WWTo2LNu-$mass-7TeV-pythia6/friis-ZH_ZToLL_HToTauTau_M-110-7TeV-pythia6_crab_digi_WW_$mass-b94ed3ce6183d233f3644e7c7592cbfd/USER" >> multicrab.cfg
  echo "" >> multicrab.cfg

  echo "[crab_reco_TT_$mass]" >> multicrab.cfg
  echo "CMSSW.datasetpath=/ZH_ZToLL_HToTauTau_M-$mass-7TeV-pythia6/friis-ZH_ZToLL_HToTauTau_M-110-7TeV-pythia6_crab_digi_TT_$mass-b94ed3ce6183d233f3644e7c7592cbfd/USER" >> multicrab.cfg
  echo "" >> multicrab.cfg
done

