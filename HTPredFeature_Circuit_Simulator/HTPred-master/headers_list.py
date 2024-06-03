
def Headers():
   headers = ["Name of file","No. of primary input gates", "No. of primary output gates", "No. of wires",
              "No. of non-primary input gates", "No. of non-primary output gates",

              "No. of 3 or more input gates", "sum CC0", "sum CC1",
              "sum CO", "No. of AND", "No. of OR",

              "No of NOT", "No of NAND", "No of NOR", "No of DFF", "No. of XOR", "NO. OF XNOR", "Sum P0", "Sum P1",
              "P0 >= 0.9", "P0 >= 0.8", "P0 >= 0.7",

              "P0 >= 0.6", "p0 >= 0.5", "p0 >= 0.4", "p0 >= 0.3", "p0 >= 0.2", "p0 >= 0.1", "P1 >= 0.9", "P1 >= 0.8",
              "P1 >= 0.7", "P1 >= 0.6",

              "p1 >= 0.5", "p1 >= 0.4", "p1 >= 0.3", "p1 >= 0.2", "p1 >= 0.1", "SUM P0 * SUM C0",
              "SUM P1 * SUM C1", "Average P0", "Average P1",

              "Average CC0", "Average CC1", "MEDIAN HIGH P0", "MEDIAN HIGH P1", "MEDIAN HIGH CC0", "MEDIAN HIGH CC1",
              "MEDIAN LOW P0", "MEDIAN LOW P1",

              "MEDIAN LOW CC0", "MEDIAN LOW CC1", "NORMALISED P0", "NORMALISED P1", "NORMALISED CC0", "NORMALISED CC1",
              "STANDARD DEVIATION P0",

              "STANDARD DEVIATION P1", "STANDARD DEVIATION CC0", "STANDARD DEVIATION CC1", "HARMONIC MEAN P0",
              "HARMONIC MEAN P1", "HARMONIC MEAN CC0",

              "HARMONIC MEAN CC1", "POPULATION STANDARD DEVIATION P0", "POPULATION STANDARD DEVIATION P1",
              "POPULATION STANDARD DEVIATION CC0",

              "POPULATION STANDARD DEVIATION CC1", "POPULATION VARIANCE P0", "POPULATION VARIANCE P1",
              "POPULATION VARIANCE CC0", "POPULATION VARIANCE CC1",

              "ratio SUM(P0/P1)", "ratio SUM(cc0/cc1)", "GEOMETRIC MEAN P0", "GEOMETRIC MEAN P1", "GEOMETRIC MEAN CC0",
              "GEOMETRIC MEAN CC1",

              "ratio SUM(P0)/SUM(P1)", "ratio SUM(CC0)/SUM(CC1)", "SUM CC1*SUM CC0", "SUM CC1*SUM CO", "SUM CC1*SUM P0",
              "SUM CC0*SUM CO", "SUM CC0*SUM P1", "SUM CO*SUM P0", "SUM CO*SUM P1", "SUM P0*SUM P1",

              "SUM CC0*SUM CC1*SUM P0*SUM P1*SUM CO", "SUM CC0*SUM CC1*SUM P0*SUM P1", "SUM CC0*SUM CC1*SUM P0*SUM CO",
              "SUM CC0*SUM CC1*SUM P1*SUM CO", "SUM CC0*SUM P0*SUM P1*SUM CO", "SUM CC1*SUM P0*SUM P1*SUM CO",
              "Max(P0)", "Min(P0)", "MAX(P1)", "MIN(P1)", "MAX(CC0)", "MIN(CC0)", "MAX(CC1)", "MIN(CC1)", "MAX(CO)",
              "MIN(CO)", "SUM P1 * SUM P0 * SUM CO", "SUM CC0 * SUM P1 * SUM PO", "SUM CC0 * SUM P1 * SUM CO",
              "SUM CC0 * SUM P0 * SUM CO", "SUM CC1 * SUM P1 * SUM PO", "SUM CC1 * SUM P0 * SUM CO", "SUM CC1 * SUM P1 * SUM CO",
              "SUM CC0 * SUM CC1 * SUM P1", "SUM CC0 * SUM CC1 * SUM P0", "SUM CC0 * SUM CC1 * SUM CO" , "co > 100", "Circuit Evaluation Time", "Sum CC(S)",
              "Max CC(S)","Min CC(S)","Average CCS","Median High CCS","Median Low CCS","Normalised CCS","Standard Deviation CCS",
              "Harmonic Mean CCS","Population Standard Deviation CCS","Population Variance","Variance CCS","Geometric Mean CCS",
              "cc0 > 100","cc1 > 100","ccs 1 - 5","ccs 5 - 10","ccs 10 - 15","ccs 15 - 20","ccs 20 - 25","ccs 25 - 30",
              "ccs 30 - 35","ccs 35 - 40","ccs 40 - 45","ccs 45 - 50","ccs 50 - 55","ccs 55 - 60","ccs 60 - 65","ccs 65 - 70",
              "ccs 70 - 75","ccs 75 - 80","ccs 80 - 85","ccs 85 - 90","ccs 90 - 95","ccs 95 - 100","ccs > 100","Number of BUFF"]

   return headers

# print(len(Headers()))