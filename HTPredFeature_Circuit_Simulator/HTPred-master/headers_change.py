x = ["Name of file","No. of primary input gates", "No. of primary output gates", "No. of wires",
              "No. of non-primary input gates", "No. of non-primary output gates",

              "No. of 1 input gates", "No. of 2 input gates", "No. of 3 or more input gates", "sum CC0", "sum CC1",
              "sum CO", "No. of AND", "No. of OR",

              "No of NOT", "No of NAND", "No of NOR", "No of DFF", "No. of XOR", "NO. OF XNOR", "Sum P0", "Sum P1",
              "P0 >= 0.9", "P0 >= 0.8", "P0 >= 0.7",

              "P0 >= 0.6", "p0 >= 0.5", "p0 >= 0.4", "p0 >= 0.3", "p0 >= 0.2", "p0 >= 0.1", "P1 >= 0.9", "P1 >= 0.8",
              "P1 >= 0.7", "P1 >= 0.6",

              "p1 >= 0.5", "p1 >= 0.4", "p1 >= 0.3", "p1 >= 0.2", "p1 >= 0.1", "cc0 <= 10", "cc0 <= 9", "cc0 <= 8",
              "cc0 <= 7", "cc0 <= 6",

              "cc0 <= 5", "cc0 <= 4", "cc0 <= 3", "cc0 <= 2", "cc0 <= 1", "cc0 > 10", "cc1 <= 10", "cc1 <= 9",
              "cc1 <= 8", "cc1 <= 7", "cc1 <= 6",

              "cc1 <= 5", "cc1 <= 4", "cc1 <= 3", "cc1 <= 2", "cc1 <= 1", "cc1 > 10", "SUM P0 * SUM C0",
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
              "SUM CC0 * SUM CC1 * SUM P1", "SUM CC0 * SUM CC1 * SUM P0", "SUM CC0 * SUM CC1 * SUM CO" , "co 1 - 5",
              "co 5 - 10", "140. co 10 - 15", "141. co 15 - 20", "142. co 20 - 25",
              "co 25 - 30", "co 30 - 35", "co 35 - 40", "co 40 - 45", "co 45 - 50", "co 50 - 55", "co 55 - 60",
              "co 60 - 65", "co 65 - 70", "co 70 - 75", "co 75 - 80", "co 80 - 85", "co 85 - 90", "co 90 - 95",
              "co 95 - 100", "co > 100", "co 0.1 - 0.2", "co 0.2 - 0.3", "co 0.3 - 0.4", "co 0.4 - 0.5", "co 0.5 - 0.6",
              "co 0.6 - 0.7", "co 0.7 - 0.8", "co 0.8 - 0.9", "co 0.9 - 1.0", "Circuit Evaluation Time", "Sum CC(S)",
              "Max CC(S)","Min CC(S)","Average CCS","Median High CCS","Median Low CCS","Normalised CCS","Standard Deviation CCS",
              "Harmonic Mean CCS","Population Standard Deviation CCS","Population Variance","Variance CCS","Geometric Mean CCS",
              "cc0 1 - 5","cc0 5 - 10","cc0 10 - 15","cc0 15 - 20","cc0 20 - 25","cc0 25 - 30","cc0 30 - 35","cc0 35 - 40",
              "cc0 40 - 45","cc0 45 - 50","cc0 50 - 55","cc0 55 - 60","cc0 60 - 65","cc0 65 - 70","cc0 70 - 75","cc0 75 - 80",
              "cc0 80 - 85","cc0 85 - 90","cc0 90 - 95","cc0 95 - 100","cc0 > 100","cc1 1 - 5","cc1 5 - 10","cc1 10 - 15",
              "cc1 15 - 20","cc1 20 - 25","cc1 25 - 30","cc1 30 - 35","cc1 35 - 40","cc1 40 - 45","cc1 45 - 50","cc1 50 - 55",
              "cc1 55 - 60","cc1 60 - 65","cc1 65 - 70","cc1 70 - 75","cc1 75 - 80","cc1 80 - 85","cc1 85 - 90","cc1 90 - 95",
              "cc1 95 - 100","cc1 > 100","ccs 1 - 5","ccs 5 - 10","ccs 10 - 15","ccs 15 - 20","ccs 20 - 25","ccs 25 - 30",
              "ccs 30 - 35","ccs 35 - 40","ccs 40 - 45","ccs 45 - 50","ccs 50 - 55","ccs 55 - 60","ccs 60 - 65","ccs 65 - 70",
              "ccs 70 - 75","ccs 75 - 80","ccs 80 - 85","ccs 85 - 90","ccs 90 - 95","ccs 95 - 100","ccs > 100","Number of BUFF", "fan_in_4",
              "fan_in_5","in_flip_flop_4","out_flip_flop_3","out_flip_flop_4","in loop 4","out loop 5","in_nearest_pin",
              "out_nearest_pout","out_nearest_flipflop","out_nearest_multiplexer"]
