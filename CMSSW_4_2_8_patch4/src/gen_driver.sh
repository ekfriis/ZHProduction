cat *txt | xargs -n 1 -I {} cmsDriver.py {} -s GEN,SIM --conditions START42_V14B::All --eventcontent FEVT --datatier GEN-SIM-RAW --pileup NoPileUp -n 10 --no_exec
