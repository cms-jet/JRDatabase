#!/bin/bash
# Read a string with spaces using for loop
for algo in AK8PFchs AK8PFPuppi AK4PFPuppi AK4PF AK8PF
do
    echo "Cloning AK4PFchs to " $algo

    cp Summer19UL17_JRV3_MC_EtaResolution_AK4PFchs.txt Summer19UL17_JRV3_MC_EtaResolution_$algo.txt
    cp Summer19UL17_JRV3_MC_PhiResolution_AK4PFchs.txt Summer19UL17_JRV3_MC_PhiResolution_$algo.txt
    cp Summer19UL17_JRV3_MC_PtResolution_AK4PFchs.txt Summer19UL17_JRV3_MC_PtResolution_$algo.txt
    cp Summer19UL17_JRV3_MC_SF_AK4PFchs.txt Summer19UL17_JRV3_MC_SF_$algo.txt

done

