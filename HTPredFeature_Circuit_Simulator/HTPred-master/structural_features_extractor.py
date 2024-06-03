# subjects=["Maths","Science","Arts","Commerce"]
# subjects_2=["Artificial intelligence","Statistics"]
# subjects.extend(subjects_2)
# print(subjects)
import statistics

sample_dict = {'fan_in_x': {'10': [2, 0, 0, 0, 0], '11': [2, 0, 0, 0, 0], '16': [2, 2, 0, 0, 0], '19': [2, 2, 0, 0, 0]},
               'loop_in_x': {'10': [0, 0, 0, 0, 0], '11': [0, 0, 0, 0, 0], '16': [0, 0, 0, 0, 0], '19': [0, 0, 0, 0, 0]},
               'loop_out_x': {'10': [0, 0, 0, 0, 0], '11': [0, 0, 0, 0, 0], '16': [0, 0, 0, 0, 0], '19': [0, 0, 0, 0, 0]},
               'in_nearest_pin': {'10': [1], '11': [1], '16': [1], '19': [1]},
               'out_nearest_pout': {'10': [1], '11': [2], '16': [1], '19': [1]},
               'in_ff_x': {'10': [0, 0, 0, 0, 0], '11': [0, 0, 0, 0, 0], '16': [0, 0, 0, 0, 0], '19': [0, 0, 0, 0, 0]},
               'out_ff_x': {'10': [0, 0, 0, 0, 0], '11': [0, 0, 0, 0, 0], '16': [0, 0, 0, 0, 0], '19': [0, 0, 0, 0, 0]},
               'in_nearest_ff': {'10': [None], '11': [None], '16': [None], '19': [None]},
               'out_nearest_ff': {'10': [None], '11': [None], '16': [None], '19': [None]},
               'in_const_x': {'10': [0, 0, 0, 0, 0], '11': [0, 0, 0, 0, 0], '16': [0, 0, 0, 0, 0], '19': [0, 0, 0, 0, 0]},
               'out_const_x': {'10': [0, 0, 0, 0, 0], '11': [0, 0, 0, 0, 0], '16': [0, 0, 0, 0, 0], '19': [0, 0, 0, 0, 0]}}

def extract_sf(sample_dict):
    final_list = []
    for x in sample_dict:
        a = sample_dict[x]
        i = -1
        for _ in a.values():
            d = len(_)
            break
        for b in range(d):
            i += 1
            listx = []
            for b in a.values():
                if (b[i] == None):
                    b[i] = 1000
                listx.append(b[i])
            temp_list = get_features(listx)
            final_list.extend(temp_list)


    print(len(final_list) ,"structural features extracted ")
    print(final_list)
    return final_list


def get_features(listA):
    f1 = sum(listA)
    f2 = max(listA)
    f3 = min(listA)
    f4 = statistics.mean(listA)
    f5 = statistics.median_high(listA)
    f6 = statistics.median_low(listA)
    f7 = statistics.mean(listA)
    f8 = statistics.stdev(listA)
    f9 = statistics.harmonic_mean(listA)
    f10 = statistics.pstdev(listA)
    f11 = statistics.pvariance(listA)
    f12 = statistics.variance(listA)
    listA = [i for i in listA if i != 0]
    if len(listA)== 0:
        f13 = 0
    else:
        f13 = statistics.geometric_mean(listA)

    f14 = 0
    f15 = 0
    f16 = 0
    f17 = 0
    f18 = 0
    f19 = 0
    f20 = 0
    f21 = 0
    f22 = 0
    f23 = 0
    f24 = 0
    f25 = 0
    f26 = 0
    f27 = 0
    f28 = 0
    f29 = 0
    f30 = 0
    f31 = 0
    f32 = 0
    f33 = 0
    f34 = 0

    for i2 in listA:
        if 1 <= i2 < 5:
            f14 += 1
        elif 5 <= i2 < 10:
            f15 += 1
        elif 10 <= i2 < 15:
            f16 += 1
        elif 15 <= i2 < 20:
            f17 += 1
        elif 20 <= i2 < 25:
            f18 += 1
        elif 25 <= i2 < 30:
            f19 += 1
        elif 30 <= i2 < 35:
            f20 += 1
        elif 35 <= i2 < 40:
            f21 += 1
        elif 40 <= i2 < 45:
            f22 += 1
        elif 45 <= i2 < 50:
            f23 += 1
        elif 50 <= i2 < 55:
            f24 += 1
        elif 55 <= i2 < 60:
            f25 += 1
        elif 60 <= i2 < 65:
            f26 += 1
        elif 65 <= i2 < 70:
            f27 += 1
        elif 70 <= i2 < 75:
            f28 += 1
        elif 75 <= i2 < 80:
            f29 += 1
        elif 80 <= i2 < 85:
            f30 += 1
        elif 85 <= i2 < 90:
            f31 += 1
        elif 90 <= i2 < 95:
            f32 += 1
        elif 95 <= i2 < 100:
            f33 += 1
        elif i2 >= 100:
            f34 += 1

    # if x == "out_nearest_ff":
    #     list_of_features = [f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14, f15, f16, f17, f18, f19, f20, f21, f34]
    # elif x == "in_nearest_ff":
    #     list_of_features = [f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14, f15, f16, f17, f18, f19, f34]
    # elif x == "fan_in_x" and countfix == 1:
    #     countfix += 1
    #     list_of_features = [f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14, f15, f16, f17]
    # elif x == "fan_in_x" and countfix == 2:
    #     countfix += 1
    #     list_of_features = [f1, f2, f4, f5, f6, f7, f8, f10, f11, f12, f13, f14, f15, f16, f17, f18, f19, f20]
    # elif x == "fan_in_x" and countfix == 3:
    #     countfix += 1
    #     list_of_features = [f1, f2, f4, f5, f6, f7, f8, f10, f11, f12, f13, f14, f15, f16, f17, f18, f19, f20, f21, f22, f23]
    # elif x == "fan_in_x" and countfix == 4:
    #     countfix += 1
    #     list_of_features = [f1, f2, f4, f5, f6, f7, f8, f10, f11, f12, f13, f14, f15, f16, f17, f18, f19, f20, f21, f22, f23, f24, f25, f26, f27, f28]
    # elif x == "fan_in_x" and countfix == 5:
    #     countfix += 1
    #     list_of_features = [f1, f2, f4, f5, f6, f7, f8, f10, f11, f12, f13, f14, f15, f16, f17, f18, f19, f20, f21, f22, f23, f24, f25, f26, f27, f28, f29, f30, f31, f32, f33, f34]
    #
    #
    #
    #
    # elif x == "loop_in_x" and countlix == 1:
    #     countlix += 1
    #     list_of_features = []
    # elif x == "loop_in_x" and countlix > 1:
    #     countlix += 1
    #     list_of_features = [f1, f2, f4, f7, f8, f10, f11, f12, f13, f14]
    #
    #
    # elif x == "loop_in_x" and countlix == 1:
    #     countlix += 1
    #     list_of_features = []
    # elif x == "loop_in_x" and countlix > 1:
    #     countlix += 1
    #     list_of_features = [f1, f2, f4, f7, f8, f10, f11, f12, f13, f14]
    #
    #
    #
    #
    # else:
    list_of_features = [f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14, f15, f16, f17, f18, f19, f20, f21, f22, f23, f24, f25, f26, f27, f28, f29, f30, f31, f32, f33, f34]
    return list_of_features


extract_sf(sample_dict)