import statistics
from scipy.stats.mstats import gmean

def FeatureExtractor(final_primary_inputs_list, final_primary_outputs_list, final_gates_list, gate_list_input,
                     gate_list_output, gate_list_name, time_elapsed, name_of_file, CC0_list, CC1_list, CO_list, P0_list, P1_list):


    '''Number of primary input gates'''
    feature_1_npi = len(final_primary_inputs_list)

    '''Number of primary output gates'''
    feature_2_npo = len(final_primary_outputs_list)

    '''Number of wires'''
    wires_list_final = []
    for ga in final_gates_list:
        if ga in final_primary_inputs_list or ga in final_primary_outputs_list:
            pass
        else:
            wires_list_final.append(ga)

    feature_3_nw = len(wires_list_final)

    '''Number of non primary input gates'''
    # gate_list_input
    temp_list = []
    for ga in gate_list_input:
        for g in ga:
            temp_list.append(g)
    feature_4_nnpi = len(temp_list)

    '''Number of non-primary output gates'''
    feature_5_nnpo = len(gate_list_output)

    '''Number of 1 input gattes'''
    count_1 = 0
    count_2 = 0
    count_3ormore = 0
    for ga in gate_list_input:
        l = len(ga)
        if l == 1:
            count_1 += 1
        elif l == 2:
            count_2 += 1
        else:
            count_3ormore += 1

    feature_6_1i = count_1

    '''Number of 2 input gates'''

    feature_7_2i = count_2

    '''Number of 3 or more input gates'''

    feature_8_3omi = count_3ormore

    '''Sum CC0'''

    sum_cc0 = sum(CC0_list)
    sum_cc1 = sum(CC1_list)
    sum_co = sum(CO_list)

    feature_9_sum_cc0 = sum_cc0

    '''Sum CC1'''

    feature_10_sum_cc1 = sum_cc1

    '''Sum CO'''

    feature_11_sum_co = sum_co

    '''Number of AND'''

    # ['NOT', 'NOT', 'OR', 'NAND', 'NOT', 'NOT', 'OR', 'NAND', 'NAND', 'NAND']
    count_and = 0
    count_or = 0
    count_not = 0
    count_nand = 0
    count_nor = 0
    count_dff = 0
    count_xor = 0
    count_xnor = 0
    count_buff = 0

    for name in gate_list_name:
        if name == "AND":
            count_and += 1
        elif name == "OR":
            count_or += 1
        elif name == "NOT":
            count_not += 1
        elif name == "NAND":
            count_nand += 1
        elif name == "NOR":
            count_nor += 1
        elif name == "DFF":
            count_dff += 1
        elif name == "XOR":
            count_xor += 1
        elif name == "XNOR":
            count_xnor += 1
        elif name == "BUFF":
            count_buff += 1

    feature_12_cand = count_and

    '''Count OR'''

    feature_13_cor = count_or

    '''Count NOT'''

    feature_14_cnot = count_not

    '''Count NAND'''

    feature_15_cnand = count_nand

    '''Count NOR'''

    feature_16_cnor = count_nor

    '''Count DFF'''

    feature_17_cdff = count_dff

    '''Count XOR'''

    feature_18_cxor = count_xor

    '''Count XNOR'''

    feature_19_cxnor = count_xnor

    '''Geometric Mean P0'''
    P0_list = [i for i in P0_list if i != 0]
    feature_98_gm_p0 = gmean(P0_list)

    '''Geometric Mean P1'''
    P1_list = [i for i in P1_list if i != 0]
    feature_99_gm_p1 = gmean(P1_list)

    '''Geometric Mean CC0'''
    CC0_list = [i for i in CC0_list if i != 0]
    feature_100_gm_cc0 = gmean(CC0_list)

    '''Geometric Mean CC1'''
    CC1_list = [i for i in CC1_list if i != 0]
    feature_101_gm_cc1 = gmean(CC1_list)

    '''RATIO SUM(P0/P1)'''
    feature_96_rsp0p1 = 0
    for p0, p1 in zip(P0_list, P1_list):
        feature_96_rsp0p1 += (p0 / p1)

    '''RATIO SUM(CC0/CC1)'''
    feature_97_rscc0cc1 = 0
    for c0, c1 in zip(CC0_list, CC1_list):
        feature_97_rscc0cc1 += (c0 / c1)

    '''ratio SUM(P0)/SUM(P1)'''
    summp0 = sum(P0_list)
    summp1 = sum(P1_list)

    feature_102_rsp0rsp1 = summp0 / summp1

    '''ratio SUM(CC0)/SUM(CC1)'''
    summcc0 = sum_cc0
    summcc1 = sum_cc1

    feature_103_rscc0rscc1 = summcc0 / summcc1

    '''Population variance p0'''
    feature_92_pvp0 = statistics.pvariance(P0_list)
    '''Population variance p1'''
    feature_93_pvp1 = statistics.pvariance(P1_list)
    '''Population variance cc0'''
    feature_94_pvcc0 = statistics.pvariance(CC0_list)
    '''Population variance cc1'''
    feature_95_pvcc1 = statistics.pvariance(CC1_list)

    '''Population standard deviation p0'''
    feature_88_psdp0 = statistics.pstdev(P0_list)
    '''Population standard deviation p1'''
    feature_89_psdp1 = statistics.pstdev(P1_list)
    '''Population standard deviation cc0'''
    feature_90_psdcc0 = statistics.pstdev(CC0_list)
    '''Population standard deviation cc1'''
    feature_91_psdcc1 = statistics.pstdev(CC1_list)

    '''Harmonic Mean p0'''
    feature_84_hmp0 = statistics.harmonic_mean(P0_list)
    '''Harmonic Mean p1'''
    feature_85_hmp1 = statistics.harmonic_mean(P1_list)
    '''Harmonic Mean cc0'''
    feature_86_hmcc0 = statistics.harmonic_mean(CC0_list)
    '''Harmonic Mean cc1'''
    feature_87_hmcc1 = statistics.harmonic_mean(CC1_list)

    '''Standard Deviation p0'''
    feature_80_sdp0 = statistics.stdev(P0_list)
    '''Standard Deviation p1'''
    feature_81_sdp1 = statistics.stdev(P1_list)
    '''Standard Deviation cc0'''
    feature_82_sdcc0 = statistics.stdev(CC0_list)
    '''Standard Deviation cc1'''
    feature_83_sdcc1 = statistics.stdev(CC1_list)

    '''Median High p0'''
    feature_68_mhp0 = statistics.median_high(P0_list)
    '''Median High p1'''
    feature_69_mhp1 = statistics.median_high(P1_list)
    '''Median High cc0'''
    feature_70_mhcc0 = statistics.median_high(CC0_list)
    '''Median High cc1'''
    feature_71_mhcc1 = statistics.median_high(CC1_list)

    '''Median Low p0'''
    feature_72_mlp0 = statistics.median_low(P0_list)
    '''Median Low p1'''
    feature_73_mlp1 = statistics.median_low(P1_list)
    '''Median Low cc0'''
    feature_74_mlcc0 = statistics.median_low(CC0_list)
    '''Median Low cc1'''
    feature_75_mlcc1 = statistics.median_low(CC1_list)

    '''Features 22 - 30'''

    feature_22_gt9p0 = 0
    feature_23_gt8p0 = 0
    feature_24_gt7p0 = 0
    feature_25_gt6p0 = 0
    feature_26_gt5p0 = 0
    feature_27_gt4p0 = 0
    feature_28_gt3p0 = 0
    feature_29_gt2p0 = 0
    feature_30_gt1p0 = 0
    feature_31_gt9p1 = 0
    feature_32_gt8p1 = 0
    feature_33_gt7p1 = 0
    feature_34_gt6p1 = 0
    feature_35_gt5p1 = 0
    feature_36_gt4p1 = 0
    feature_37_gt3p1 = 0
    feature_38_gt2p1 = 0
    feature_39_gt1p1 = 0

    for i in P0_list:

        if i >= 0.9:
            feature_22_gt9p0 += 1
        if i >= 0.8:
            feature_23_gt8p0 += 1
        if i >= 0.7:
            feature_24_gt7p0 += 1
        if i >= 0.6:
            feature_25_gt6p0 += 1
        if i >= 0.5:
            feature_26_gt5p0 += 1
        if i >= 0.4:
            feature_27_gt4p0 += 1
        if i >= 0.3:
            feature_28_gt3p0 += 1
        if i >= 0.2:
            feature_29_gt2p0 += 1
        if i >= 0.1:
            feature_30_gt1p0 += 1

    '''Feature 31 - 39'''

    for i in P1_list:

        if i >= 0.9:
            feature_31_gt9p1 += 1
        if i >= 0.8:
            feature_32_gt8p1 += 1
        if i >= 0.7:
            feature_33_gt7p1 += 1
        if i >= 0.6:
            feature_34_gt6p1 += 1
        if i >= 0.5:
            feature_35_gt5p1 += 1
        if i >= 0.4:
            feature_36_gt4p1 += 1
        if i >= 0.3:
            feature_37_gt3p1 += 1
        if i >= 0.2:
            feature_38_gt2p1 += 1
        if i >= 0.1:
            feature_39_gt1p1 += 1

    '''Feature 40 - 50'''

    feature_40_lt10cc0 = 0
    feature_41_lt9cc0 = 0
    feature_42_lt8cc0 = 0
    feature_43_lt7cc0 = 0
    feature_44_lt6cc0 = 0
    feature_45_lt5cc0 = 0
    feature_46_lt4cc0 = 0
    feature_47_lt3cc0 = 0
    feature_48_lt2cc0 = 0
    feature_49_lt1cc0 = 0
    feature_50_gt10cc0 = 0

    for i in CC0_list:

        if i <= 10:
            feature_40_lt10cc0 += 1
        if i <= 9:
            feature_41_lt9cc0 += 1
        if i <= 8:
            feature_42_lt8cc0 += 1
        if i <= 7:
            feature_43_lt7cc0 += 1
        if i <= 6:
            feature_44_lt6cc0 += 1
        if i <= 5:
            feature_45_lt5cc0 += 1
        if i <= 4:
            feature_46_lt4cc0 += 1
        if i <= 3:
            feature_47_lt3cc0 += 1
        if i <= 2:
            feature_48_lt2cc0 += 1
        if i <= 1:
            feature_49_lt1cc0 += 1
        if i > 10:
            feature_50_gt10cc0 += 1

    '''51 - 61'''

    feature_51_lt10cc1 = 0
    feature_52_lt9cc1 = 0
    feature_53_lt8cc1 = 0
    feature_54_lt7cc1 = 0
    feature_55_lt6cc1 = 0
    feature_56_lt5cc1 = 0
    feature_57_lt4cc1 = 0
    feature_58_lt3cc1 = 0
    feature_59_lt2cc1 = 0
    feature_60_lt1cc1 = 0
    feature_61_gt10cc1 = 0

    for i in CC1_list:

        if i <= 10:
            feature_51_lt10cc1 += 1
        if i <= 9:
            feature_52_lt9cc1 += 1
        if i <= 8:
            feature_53_lt8cc1 += 1
        if i <= 7:
            feature_54_lt7cc1 += 1
        if i <= 6:
            feature_55_lt6cc1 += 1
        if i <= 5:
            feature_56_lt5cc1 += 1
        if i <= 4:
            feature_57_lt4cc1 += 1
        if i <= 3:
            feature_58_lt3cc1 += 1
        if i <= 2:
            feature_59_lt2cc1 += 1
        if i <= 1:
            feature_60_lt1cc1 += 1
        if i > 10:
            feature_61_gt10cc1 += 1

    '''76 - 79'''
    #######################Normalize-P0############################

    norm = [float(i) / summp0 for i in P0_list]
    feature_76_np0 = statistics.mean(norm)
    ##########################Normalize-P1#####################################

    norm = [float(i) / summp1 for i in P1_list]
    feature_77_np1 = statistics.mean(norm)
    #########################Normalize-CC0#####################################

    norm = [float(i) / summcc0 for i in CC0_list]
    feature_78_ncc0 = statistics.mean(norm)
    #########################Normalize-CC1#####################################

    norm = [float(i) / summcc1 for i in CC1_list]
    feature_79_ncc1 = statistics.mean(norm)

    feature_9_sum_CC0 = summcc0
    feature_10_sum_CC1 = summcc1
    feature_11_sum_CO = sum_co
    feature_20_sum_P0 = summp0
    feature_21_sum_P1 = summp1

    # for i in CC0_list:
    #     feature_9_sum_CC0 = feature_9_sum_CC0 + i
    # for i1 in CC1_list:
    #     feature_10_sum_CC1 = feature_10_sum_CC1 + i1
    # for i2 in CO_list:
    #     feature_11_sum_CO = feature_11_sum_CO + i2
    # for i3 in P0_list:
    #     feature_20_sum_P0 = feature_20_sum_P0 + i3
    # for i4 in P1_list:
    #     feature_21_sum_P1 = feature_21_sum_P1 + i4

    ###########################MIN-MAX -- P0###################################

    feature_118_maxP0 = max(P0_list)
    feature_119_minP0 = min(P0_list)
    ###################################MIN- MAX CO######################################
    feature_121_minP1 = min(P1_list)
    feature_120_maxP1 = max(P1_list)
    ###################################MIN- MAX CC0######################################
    feature_123_minCC0 = min(CC0_list)
    feature_122_maxCC0 = max(CC0_list)
    ###################################MIN- MAX CC1######################################
    feature_125_minCC1 = min(CC1_list)
    feature_124_maxCC1 = max(CC1_list)

    feature_127_minCO = min(CO_list)
    feature_126_maxCO = max(CO_list)

    feature_104_multiply_CC1CC0 = feature_10_sum_CC1 * feature_9_sum_CC0
    feature_105_multiply_CC1CO = feature_10_sum_CC1 * feature_11_sum_CO
    feature_106_multiply_CC1P0 = feature_10_sum_CC1 * feature_20_sum_P0
    feature_107_multiply_CC0CO = feature_9_sum_CC0 * feature_11_sum_CO
    feature_108_multiply_CC0P1 = feature_9_sum_CC0 * feature_21_sum_P1
    feature_109_multiply_COP0 = feature_11_sum_CO * feature_20_sum_P0
    feature_110_multiply_COP1 = feature_11_sum_CO * feature_21_sum_P1
    feature_111_multiply_P0P1 = feature_20_sum_P0 * feature_21_sum_P1
    feature_112_multiply_CC0CC1P0P1CO = feature_9_sum_CC0 * feature_10_sum_CC1 * feature_21_sum_P1 * feature_20_sum_P0 * feature_11_sum_CO

    feature_62_Multiplysum_P0C0 = feature_20_sum_P0 * feature_9_sum_CC0
    feature_63_Multiplysum_P1C1 = feature_21_sum_P1 * feature_10_sum_CC1
    feature_64_avg_P0 = feature_20_sum_P0 / len(P0_list)
    feature_65_avg_P1 = feature_21_sum_P1 / len(P1_list)
    feature_66_avg_CC0 = feature_9_sum_CC0 / len(CC0_list)
    feature_67_avg_CC1 = feature_10_sum_CC1 / len(CC1_list)

    # print(feature_62_Multiplysum_P0C0)
    # print(feature_63_Multiplysum_P1C1)
    # print(feature_9_sum_CC0)
    # print(feature_10_sum_CC1)
    # print(feature_11_sum_CO)
    # print(feature_20_sum_P0)
    # print(feature_21_sum_P1)
    # print(feature_64_avg_P0)
    # print(feature_65_avg_P1)
    # print(feature_66_avg_CC0)
    # print(feature_67_avg_CC1)
    # print(feature_104_multiply_CC1CC0)
    # print(feature_105_multiply_CC1CO)
    # print(feature_106_multiply_CC1P0)
    # print(feature_107_multiply_CC0CO)
    # print(feature_108_multiply_CC0P1)
    # print(feature_109_multiply_COP0)
    # print(feature_110_multiply_COP1)
    # print(feature_111_multiply_P0P1)
    # print(feature_112_multiply_CC0CC1P0P1CO)

    feature_113_multiply_CC0CC1P0P1 = feature_9_sum_CC0 * feature_10_sum_CC1 * feature_21_sum_P1 * feature_20_sum_P0
    feature_114_multiply_CC0CC1P0CO = feature_9_sum_CC0 * feature_10_sum_CC1 * feature_21_sum_P1 * feature_11_sum_CO
    feature_115_multiply_CC0CC1P1CO = feature_9_sum_CC0 * feature_10_sum_CC1 * feature_20_sum_P0 * feature_11_sum_CO
    feature_116_multiply_CC0P0P1CO = feature_9_sum_CC0 * feature_21_sum_P1 * feature_20_sum_P0 * feature_11_sum_CO
    feature_117_multiply_CC1P0P1CO = feature_10_sum_CC1 * feature_21_sum_P1 * feature_20_sum_P0 * feature_11_sum_CO

    # print(feature_113_multiply_CC0CC1P0P1)
    # print(feature_114_multiply_CC0CC1P0CO)
    # print(feature_115_multiply_CC0CC1P1CO)
    # print(feature_116_multiply_CC0P0P1CO)
    # print(feature_117_multiply_CC1P0P1CO)

    feature_128_multiply_P0P1CO = feature_21_sum_P1 * feature_20_sum_P0 * feature_11_sum_CO
    feature_129_multiply_CC0P0P1 = feature_9_sum_CC0 * feature_21_sum_P1 * feature_20_sum_P0
    feature_130_multiply_CC0P1CO = feature_9_sum_CC0 * feature_21_sum_P1 * feature_11_sum_CO
    feature_131_multiply_CC0P0CO = feature_9_sum_CC0 * feature_20_sum_P0 * feature_11_sum_CO
    feature_132_multiply_CC1P0P1 = feature_10_sum_CC1 * feature_21_sum_P1 * feature_20_sum_P0
    feature_133_multiply_CC1P0CO = feature_10_sum_CC1 * feature_20_sum_P0 * feature_11_sum_CO
    feature_134_multiply_CC1P1CO = feature_10_sum_CC1 * feature_21_sum_P1 * feature_11_sum_CO
    feature_135_multiply_CC0CC1P1 = feature_9_sum_CC0 * feature_10_sum_CC1 * feature_21_sum_P1
    feature_136_multiply_CC0CC1P0 = feature_9_sum_CC0 * feature_10_sum_CC1 * feature_20_sum_P0
    feature_137_multiply_CC0CC1CO = feature_9_sum_CC0 * feature_10_sum_CC1 * feature_11_sum_CO

    # print(feature_128_multiply_P0P1CO)
    # print(feature_129_multiply_CC0P0P1)
    # print(feature_130_multiply_CC0P1CO)
    # print(feature_131_multiply_CC0P0CO)
    # print(feature_132_multiply_CC1P0P1)
    # print(feature_133_multiply_CC1P0CO)
    # print(feature_134_multiply_CC1P1CO)
    # print(feature_135_multiply_CC0CC1P1)
    # print(feature_136_multiply_CC0CC1P0)
    # print(feature_137_multiply_CC0CC1CO)
    # print(feature_138_power_CC1CC0)
    # print(feature_139_power_CC1CO)
    # print(feature_140_power_CC1P0)
    # print(feature_141_power_CC0CO)
    # print(feature_142_power_CC0P1)
    # print(feature_143_power_COP0)
    # print(feature_144_power_COP1)
    # print(feature_145_power_P0P1)
    # print(feature_146_multiply_P0P1_power_CO)
    # print(feature_147_multiply_CC0P0_power_P1)
    # print(feature_148_multiply_CC0P1_power_CO)
    # print(feature_149_multiply_CC0P0_power_CO)
    # print(feature_150_multiply_CC1P0_power_P1)
    # print(feature_151_multiply_CC1P0_power_CO)
    # print(feature_152_multiply_CC1P1_power_CO)
    # print(feature_153_multiply_CC0CC1_power_P1)
    # print(feature_154_multiply_CC0CC1_power_P0)
    # print(feature_155_multiply_CC0CC1_power_CO)

    # print(feature_1_npi)
    # print(feature_2_npo)
    # print(feature_3_nw)
    # print(feature_4_nnpi)
    # print(feature_5_nnpo)
    # print(feature_6_1i)
    # print(feature_7_2i)
    # print(feature_8_3omi)
    # print(feature_9_sum_cc0)
    # print(feature_10_sum_cc1)
    # print(feature_11_sum_co)
    # print(feature_12_cand)
    # print(feature_13_cor)
    # print(feature_14_cnot)
    # print(feature_15_cnand)
    # print(feature_16_cnor)
    # print(feature_17_cdff)
    # print(feature_18_cxor)
    # print(feature_19_cxnor)

    # print(feature_20_sum_P0)
    # print(feature_21_sum_P1)
    # print(feature_22_gt9p0)

    # Extracting CCS Values

    ccs_list = []

    for cc0, cc1 in zip(CC0_list, CC1_list):
        ccs = ((cc0 ** 2) * (cc1 ** 2)) ** 0.5
        ccs_list.append(ccs)

    feature_139_CO_1and5 = 0
    feature_140_CO_5and10 = 0
    feature_141_CO_10and15 = 0
    feature_142_CO_15and20 = 0
    feature_143_CO_20and25 = 0
    feature_144_CO_25and30 = 0
    feature_145_CO_30and35 = 0
    feature_146_CO_35and40 = 0
    feature_147_CO_40and45 = 0
    feature_148_CO_45and50 = 0
    feature_149_CO_50and55 = 0
    feature_150_CO_55and60 = 0
    feature_151_CO_60and65 = 0
    feature_152_CO_65and70 = 0
    feature_153_CO_70and75 = 0
    feature_154_CO_75and80 = 0
    feature_155_CO_80and85 = 0
    feature_156_CO_85and90 = 0
    feature_157_CO_90and95 = 0
    feature_158_CO_95and100 = 0
    feature_159_CO_100 = 0
    feature_160_CO_01and02 = 0
    feature_161_CO_02and03 = 0
    feature_162_CO_03and04 = 0
    feature_163_CO_04and05 = 0
    feature_164_CO_05and06 = 0
    feature_165_CO_06and07 = 0
    feature_166_CO_07and08 = 0
    feature_167_CO_08and09 = 0
    feature_168_CO_09and10 = 0

    for i2 in CO_list:
        if 1 <= i2 < 5:
            feature_139_CO_1and5 += 1
        elif 5 <= i2 < 10:
            feature_140_CO_5and10 += 1
        elif 10 <= i2 < 15:
            feature_141_CO_10and15 += 1
        elif 15 <= i2 < 20:
            feature_142_CO_15and20 += 1
        elif 20 <= i2 < 25:
            feature_143_CO_20and25 += 1
        elif 25 <= i2 < 30:
            feature_144_CO_25and30 += 1
        elif 30 <= i2 < 35:
            feature_145_CO_30and35 += 1
        elif 35 <= i2 < 40:
            feature_146_CO_35and40 += 1
        elif 40 <= i2 < 45:
            feature_147_CO_40and45 += 1
        elif 45 <= i2 < 50:
            feature_148_CO_45and50 += 1
        elif 50 <= i2 < 55:
            feature_149_CO_50and55 += 1
        elif 55 <= i2 < 60:
            feature_150_CO_55and60 += 1
        elif 60 <= i2 < 65:
            feature_151_CO_60and65 += 1
        elif 65 <= i2 < 70:
            feature_152_CO_65and70 += 1
        elif 70 <= i2 < 75:
            feature_153_CO_70and75 += 1
        elif 75 <= i2 < 80:
            feature_154_CO_75and80 += 1
        elif 80 <= i2 < 85:
            feature_155_CO_80and85 += 1
        elif 85 <= i2 < 90:
            feature_156_CO_85and90 += 1
        elif 90 <= i2 < 95:
            feature_157_CO_90and95 += 1
        elif 95 <= i2 < 100:
            feature_158_CO_95and100 += 1
        elif i2 >= 100:
            feature_159_CO_100 += 1
        elif 0.1 <= i2 < 0.2:
            feature_160_CO_01and02 += 1
        elif 0.2 <= i2 < 0.3:
            feature_161_CO_02and03 += 1
        elif 0.3 <= i2 < 0.4:
            feature_162_CO_03and04 += 1
        elif 0.4 <= i2 < 0.5:
            feature_163_CO_04and05 += 1
        elif 0.5 <= i2 < 0.6:
            feature_164_CO_05and06 += 1
        elif 0.6 <= i2 < 0.7:
            feature_165_CO_06and07 += 1
        elif 0.7 <= i2 < 0.8:
            feature_166_CO_07and08 += 1
        elif 0.8 <= i2 < 0.9:
            feature_167_CO_08and09 += 1
        elif 0.9 <= i2 < 1.0:
            feature_168_CO_09and10 += 1

    feature_182_CC0_1and5 = 0
    feature_183_CC0_5and10 = 0
    feature_184_CC0_10and15 = 0
    feature_185_CC0_15and20 = 0
    feature_186_CC0_20and25 = 0
    feature_187_CC0_25and30 = 0
    feature_188_CC0_30and35 = 0
    feature_189_CC0_35and40 = 0
    feature_190_CC0_40and45 = 0
    feature_191_CC0_45and50 = 0
    feature_192_CC0_50and55 = 0
    feature_193_CC0_55and60 = 0
    feature_194_CC0_60and65 = 0
    feature_195_CC0_65and70 = 0
    feature_196_CC0_70and75 = 0
    feature_197_CC0_75and80 = 0
    feature_198_CC0_80and85 = 0
    feature_199_CC0_85and90 = 0
    feature_200_CC0_90and95 = 0
    feature_201_CC0_95and100 = 0
    feature_202_CC0_100 = 0

    for i2 in CC0_list:
        if 1 <= i2 < 5:
            feature_182_CC0_1and5 += 1
        elif 5 <= i2 < 10:
            feature_183_CC0_5and10 += 1
        elif 10 <= i2 < 15:
            feature_184_CC0_10and15 += 1
        elif 15 <= i2 < 20:
            feature_185_CC0_15and20 += 1
        elif 20 <= i2 < 25:
            feature_186_CC0_20and25 += 1
        elif 25 <= i2 < 30:
            feature_187_CC0_25and30 += 1
        elif 30 <= i2 < 35:
            feature_188_CC0_30and35 += 1
        elif 35 <= i2 < 40:
            feature_189_CC0_35and40 += 1
        elif 40 <= i2 < 45:
            feature_190_CC0_40and45 += 1
        elif 45 <= i2 < 50:
            feature_191_CC0_45and50 += 1
        elif 50 <= i2 < 55:
            feature_192_CC0_50and55 += 1
        elif 55 <= i2 < 60:
            feature_193_CC0_55and60 += 1
        elif 60 <= i2 < 65:
            feature_194_CC0_60and65 += 1
        elif 65 <= i2 < 70:
            feature_195_CC0_65and70 += 1
        elif 70 <= i2 < 75:
            feature_196_CC0_70and75 += 1
        elif 75 <= i2 < 80:
            feature_197_CC0_75and80 += 1
        elif 80 <= i2 < 85:
            feature_198_CC0_80and85 += 1
        elif 85 <= i2 < 90:
            feature_199_CC0_85and90 += 1
        elif 90 <= i2 < 95:
            feature_200_CC0_90and95 += 1
        elif 95 <= i2 < 100:
            feature_201_CC0_95and100 += 1
        elif i2 >= 100:
            feature_202_CC0_100 += 1

    feature_203_CC1_1and5 = 0
    feature_204_CC1_5and10 = 0
    feature_205_CC1_10and15 = 0
    feature_206_CC1_15and20 = 0
    feature_207_CC1_20and25 = 0
    feature_208_CC1_25and30 = 0
    feature_209_CC1_30and35 = 0
    feature_210_CC1_35and40 = 0
    feature_211_CC1_40and45 = 0
    feature_212_CC1_45and50 = 0
    feature_213_CC1_50and55 = 0
    feature_214_CC1_55and60 = 0
    feature_215_CC1_60and65 = 0
    feature_216_CC1_65and70 = 0
    feature_217_CC1_70and75 = 0
    feature_218_CC1_75and80 = 0
    feature_219_CC1_80and85 = 0
    feature_220_CC1_85and90 = 0
    feature_221_CC1_90and95 = 0
    feature_222_CC1_95and100 = 0
    feature_223_CC1_100 = 0

    for i2 in CC1_list:
        if 1 <= i2 < 5:
            feature_203_CC1_1and5 += 1
        elif 5 <= i2 < 10:
            feature_204_CC1_5and10 += 1
        elif 10 <= i2 < 15:
            feature_205_CC1_10and15 += 1
        elif 15 <= i2 < 20:
            feature_206_CC1_15and20 += 1
        elif 20 <= i2 < 25:
            feature_207_CC1_20and25 += 1
        elif 25 <= i2 < 30:
            feature_208_CC1_25and30 += 1
        elif 30 <= i2 < 35:
            feature_209_CC1_30and35 += 1
        elif 35 <= i2 < 40:
            feature_210_CC1_35and40 += 1
        elif 40 <= i2 < 45:
            feature_211_CC1_40and45 += 1
        elif 45 <= i2 < 50:
            feature_212_CC1_45and50 += 1
        elif 50 <= i2 < 55:
            feature_213_CC1_50and55 += 1
        elif 55 <= i2 < 60:
            feature_214_CC1_55and60 += 1
        elif 60 <= i2 < 65:
            feature_215_CC1_60and65 += 1
        elif 65 <= i2 < 70:
            feature_216_CC1_65and70 += 1
        elif 70 <= i2 < 75:
            feature_217_CC1_70and75 += 1
        elif 75 <= i2 < 80:
            feature_218_CC1_75and80 += 1
        elif 80 <= i2 < 85:
            feature_219_CC1_80and85 += 1
        elif 85 <= i2 < 90:
            feature_220_CC1_85and90 += 1
        elif 90 <= i2 < 95:
            feature_221_CC1_90and95 += 1
        elif 95 <= i2 < 100:
            feature_222_CC1_95and100 += 1
        elif i2 >= 100:
            feature_223_CC1_100 += 1

    feature_224_CCS_1and5 = 0
    feature_225_CCS_5and10 = 0
    feature_226_CCS_10and15 = 0
    feature_227_CCS_15and20 = 0
    feature_228_CCS_20and25 = 0
    feature_229_CCS_25and30 = 0
    feature_230_CCS_30and35 = 0
    feature_231_CCS_35and40 = 0
    feature_232_CCS_40and45 = 0
    feature_233_CCS_45and50 = 0
    feature_234_CCS_50and55 = 0
    feature_235_CCS_55and60 = 0
    feature_236_CCS_60and65 = 0
    feature_237_CCS_65and700 = 0
    feature_238_CCS_70and75 = 0
    feature_239_CCS_75and80 = 0
    feature_240_CCS_80and85 = 0
    feature_241_CCS_85and90 = 0
    feature_242_CCS_90and95 = 0
    feature_243_CCS_95and100 = 0
    feature_244_CCS_100 = 0

    for i2 in ccs_list:
        if 1 <= i2 < 5:
            feature_224_CCS_1and5 += 1
        elif 5 <= i2 < 10:
            feature_225_CCS_5and10 += 1
        elif 10 <= i2 < 15:
            feature_226_CCS_10and15 += 1
        elif 15 <= i2 < 20:
            feature_227_CCS_15and20 += 1
        elif 20 <= i2 < 25:
            feature_228_CCS_20and25 += 1
        elif 25 <= i2 < 30:
            feature_229_CCS_25and30 += 1
        elif 30 <= i2 < 35:
            feature_230_CCS_30and35 += 1
        elif 35 <= i2 < 40:
            feature_231_CCS_35and40 += 1
        elif 40 <= i2 < 45:
            feature_232_CCS_40and45 += 1
        elif 45 <= i2 < 50:
            feature_233_CCS_45and50 += 1
        elif 50 <= i2 < 55:
            feature_234_CCS_50and55 += 1
        elif 55 <= i2 < 60:
            feature_235_CCS_55and60 += 1
        elif 60 <= i2 < 65:
            feature_236_CCS_60and65 += 1
        elif 65 <= i2 < 70:
            feature_237_CCS_65and700 += 1
        elif 70 <= i2 < 75:
            feature_238_CCS_70and75 += 1
        elif 75 <= i2 < 80:
            feature_239_CCS_75and80 += 1
        elif 80 <= i2 < 85:
            feature_240_CCS_80and85 += 1
        elif 85 <= i2 < 90:
            feature_241_CCS_85and90 += 1
        elif 90 <= i2 < 95:
            feature_242_CCS_90and95 += 1
        elif 95 <= i2 < 100:
            feature_243_CCS_95and100 += 1
        elif i2 >= 100:
            feature_244_CCS_100 += 1

    feature_169_sum_ccs = sum(ccs_list)
    feature_170_max_ccs = max(ccs_list)
    feature_171_min_ccs = min(ccs_list)
    feature_172_avg_ccs = statistics.mean(ccs_list)
    feature_173_med_high_ccs = statistics.median_high(ccs_list)
    feature_174_med_low_ccs = statistics.median_low(ccs_list)
    # norm_ccs = sum(ccs_list)/len(ccs_list)
    feature_175_normal_ccs = statistics.mean(ccs_list)
    feature_176_standard_deviation_ccs = statistics.stdev(ccs_list)
    featur_177_harmonic_mean_ccs = statistics.harmonic_mean(ccs_list)
    feature_178_population_stdev_ccs = statistics.pstdev(ccs_list)
    feature_179_pop_variance_ccs = statistics.pvariance(ccs_list)
    feature_180_variance_ccs = statistics.variance(ccs_list)
    feature_181_geometric_mean_ccs = gmean(ccs_list)

    list_features_final = [name_of_file, feature_1_npi, feature_2_npo, feature_3_nw, feature_4_nnpi, feature_5_nnpo,
                           feature_6_1i,
                           feature_7_2i, feature_8_3omi,

                           feature_9_sum_cc0, feature_10_sum_cc1, feature_11_sum_co, feature_12_cand, feature_13_cor,
                           feature_14_cnot, feature_15_cnand,

                           feature_16_cnor, feature_17_cdff, feature_18_cxor, feature_19_cxnor, feature_20_sum_P0,
                           feature_21_sum_P1, feature_22_gt9p0,

                           feature_23_gt8p0, feature_24_gt7p0, feature_25_gt6p0, feature_26_gt5p0, feature_27_gt4p0,
                           feature_28_gt3p0, feature_29_gt2p0,

                           feature_30_gt1p0, feature_31_gt9p1, feature_32_gt8p1, feature_33_gt7p1, feature_34_gt6p1,

                           feature_35_gt5p1, feature_36_gt4p1, feature_37_gt3p1, feature_38_gt2p1, feature_39_gt1p1,
                           feature_40_lt10cc0,

                           feature_41_lt9cc0, feature_42_lt8cc0, feature_43_lt7cc0, feature_44_lt6cc0,
                           feature_45_lt5cc0, feature_46_lt4cc0,

                           feature_47_lt3cc0, feature_48_lt2cc0, feature_49_lt1cc0, feature_50_gt10cc0,
                           feature_51_lt10cc1, feature_52_lt9cc1, feature_53_lt8cc1,

                           feature_54_lt7cc1, feature_55_lt6cc1, feature_56_lt5cc1, feature_57_lt4cc1,
                           feature_58_lt3cc1, feature_59_lt2cc1, feature_60_lt1cc1,

                           feature_61_gt10cc1, feature_62_Multiplysum_P0C0, feature_63_Multiplysum_P1C1,
                           feature_64_avg_P0, feature_65_avg_P1, feature_66_avg_CC0,

                           feature_67_avg_CC1, feature_68_mhp0, feature_69_mhp1, feature_70_mhcc0, feature_71_mhcc1,
                           feature_72_mlp0, feature_73_mlp1, feature_74_mlcc0

        , feature_75_mlcc1, feature_76_np0, feature_77_np1, feature_78_ncc0, feature_79_ncc1, feature_80_sdp0,
                           feature_81_sdp1, feature_82_sdcc0,

                           feature_83_sdcc1, feature_84_hmp0, feature_85_hmp1, feature_86_hmcc0, feature_87_hmcc1,
                           feature_88_psdp0, feature_89_psdp1, feature_90_psdcc0,

                           feature_91_psdcc1, feature_92_pvp0, feature_93_pvp1, feature_94_pvcc0, feature_95_pvcc1,
                           feature_96_rsp0p1, feature_97_rscc0cc1, feature_98_gm_p0,

                           feature_99_gm_p1, feature_100_gm_cc0, feature_101_gm_cc1, feature_102_rsp0rsp1,
                           feature_103_rscc0rscc1, feature_104_multiply_CC1CC0, feature_105_multiply_CC1CO,

                           feature_106_multiply_CC1P0, feature_107_multiply_CC0CO, feature_108_multiply_CC0P1,
                           feature_109_multiply_COP0, feature_110_multiply_COP1, feature_111_multiply_P0P1,

                           feature_112_multiply_CC0CC1P0P1CO, feature_113_multiply_CC0CC1P0P1,
                           feature_114_multiply_CC0CC1P0CO, feature_115_multiply_CC0CC1P1CO,

                           feature_116_multiply_CC0P0P1CO, feature_117_multiply_CC1P0P1CO, feature_118_maxP0,
                           feature_119_minP0, feature_120_maxP1, feature_121_minP1, feature_122_maxCC0,

                           feature_123_minCC0, feature_124_maxCC1, feature_125_minCC1, feature_126_maxCO,
                           feature_127_minCO, feature_128_multiply_P0P1CO,
                           feature_129_multiply_CC0P0P1, feature_130_multiply_CC0P1CO, feature_131_multiply_CC0P0CO,
                           feature_132_multiply_CC1P0P1,
                           feature_133_multiply_CC1P0CO,
                           feature_134_multiply_CC1P1CO, feature_135_multiply_CC0CC1P1, feature_136_multiply_CC0CC1P0,
                           feature_137_multiply_CC0CC1CO,
                           feature_139_CO_1and5, feature_140_CO_5and10, feature_141_CO_10and15, feature_142_CO_15and20,
                           feature_143_CO_20and25, feature_144_CO_25and30, feature_145_CO_30and35,
                           feature_146_CO_35and40, feature_147_CO_40and45,
                           feature_148_CO_45and50, feature_149_CO_50and55, feature_150_CO_55and60,
                           feature_151_CO_60and65,
                           feature_152_CO_65and70, feature_153_CO_70and75, feature_154_CO_75and80,
                           feature_155_CO_80and85,
                           feature_156_CO_85and90, feature_157_CO_90and95, feature_158_CO_95and100, feature_159_CO_100,
                           feature_160_CO_01and02, feature_161_CO_02and03, feature_162_CO_03and04,
                           feature_163_CO_04and05,
                           feature_164_CO_05and06, feature_165_CO_06and07, feature_166_CO_07and08,
                           feature_167_CO_08and09, feature_168_CO_09and10,
                           time_elapsed,
                           feature_169_sum_ccs, feature_170_max_ccs, feature_171_min_ccs, feature_172_avg_ccs,
                           feature_173_med_high_ccs,
                           feature_174_med_low_ccs, feature_175_normal_ccs, feature_176_standard_deviation_ccs,
                           featur_177_harmonic_mean_ccs,
                           feature_178_population_stdev_ccs, feature_179_pop_variance_ccs, feature_180_variance_ccs,
                           feature_181_geometric_mean_ccs,
                           feature_182_CC0_1and5, feature_183_CC0_5and10, feature_184_CC0_10and15,
                           feature_185_CC0_15and20,
                           feature_186_CC0_20and25, feature_187_CC0_25and30, feature_188_CC0_30and35,
                           feature_189_CC0_35and40,
                           feature_190_CC0_40and45, feature_191_CC0_45and50, feature_192_CC0_50and55,
                           feature_193_CC0_55and60,
                           feature_194_CC0_60and65, feature_195_CC0_65and70, feature_196_CC0_70and75,
                           feature_197_CC0_75and80,
                           feature_198_CC0_80and85, feature_199_CC0_85and90, feature_200_CC0_90and95,
                           feature_201_CC0_95and100,
                           feature_202_CC0_100, feature_203_CC1_1and5, feature_204_CC1_5and10, feature_205_CC1_10and15,
                           feature_206_CC1_15and20,
                           feature_207_CC1_20and25, feature_208_CC1_25and30, feature_209_CC1_30and35,
                           feature_210_CC1_35and40,
                           feature_211_CC1_40and45, feature_212_CC1_45and50, feature_213_CC1_50and55,
                           feature_214_CC1_55and60,
                           feature_215_CC1_60and65, feature_216_CC1_65and70, feature_217_CC1_70and75,
                           feature_218_CC1_75and80,
                           feature_219_CC1_80and85, feature_220_CC1_85and90, feature_221_CC1_90and95,
                           feature_222_CC1_95and100,
                           feature_223_CC1_100, feature_224_CCS_1and5, feature_225_CCS_5and10, feature_226_CCS_10and15,
                           feature_227_CCS_15and20, feature_228_CCS_20and25, feature_229_CCS_25and30,
                           feature_230_CCS_30and35,
                           feature_231_CCS_35and40, feature_232_CCS_40and45, feature_233_CCS_45and50,
                           feature_234_CCS_50and55,
                           feature_235_CCS_55and60, feature_236_CCS_60and65, feature_237_CCS_65and700,
                           feature_238_CCS_70and75,
                           feature_239_CCS_75and80, feature_240_CCS_80and85, feature_241_CCS_85and90,
                           feature_242_CCS_90and95,
                           feature_243_CCS_95and100, feature_244_CCS_100, count_buff]

    return list_features_final
