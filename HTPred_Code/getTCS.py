

def getTCS(rtrl):
    Total_TCs = 0
    for i in range(len(rtrl)):
        if i == 0:
            Total_TCs = Total_TCs + (pow(2, len(rtrl[i])) - 1)
        else:
            MTest_Rares = [None for x in range(i)]
            for j in range(i):
                MTest_Rares[j] = []
            for j in range(len(rtrl[i])):
                for k in range(i):
                    if (rtrl[i][j] in rtrl[k]):
                        if rtrl[i][j] not in MTest_Rares[k]:
                            MTest_Rares[k].append(rtrl[i][j])
            empty_ind = []
            for k in range(len(MTest_Rares)):
                if len(MTest_Rares[k]) == 0:
                    if k not in empty_ind:
                        empty_ind.append(k);

            new_MTest_Rares_list = [];
            status = True
            for k in range(len(MTest_Rares)):
                status = True;
                for l in range(len(MTest_Rares)):
                    if k == l:
                        continue
                    if (all(elem in MTest_Rares[l] for elem in MTest_Rares[k]) and len(MTest_Rares[k]) < len(
                            MTest_Rares[l])):
                        status = False
                        break
                    elif (all(elem in MTest_Rares[l] for elem in MTest_Rares[k]) and len(MTest_Rares[k]) == len(
                            MTest_Rares[l]) and k > l):
                        status = False
                        break

                if status == True and (k not in empty_ind):
                    if MTest_Rares[k] not in new_MTest_Rares_list:
                        new_MTest_Rares_list.append(MTest_Rares[k])

            new_MTest_Rares = [None for x in range(len(new_MTest_Rares_list))]
            for j in range(len(new_MTest_Rares)):
                new_MTest_Rares[j] = [None for x in range(len(new_MTest_Rares_list[j]))]

            Total_TCs = Total_TCs + (pow(2, len(rtrl[i])) - 1) - getTCS(new_MTest_Rares)

    return Total_TCs

# l=[['693', '620'], ['721', '655'], ['720', '655'], ['692', '620'], ['630', '703'], ['635', '707'], ['650', '719'], ['714', '645'], ['625', '697']]
# print(getTCS(l))
# getTCS(rltl)