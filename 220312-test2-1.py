import pprint

def solution(products, purchased):
    pref = {}
    products = [p.split() for p in products]
    products_dic = {p[0]: p[1:] for p in products}
    # pprint.pprint(products_dic)
    # print()
    
    for i in products:
        if i[0] in purchased:
            for p in i[1:]:
                if pref.get(p):
                    pref[p] += 1
                else:
                    pref[p] = 1
                
    pref = sorted(sorted([[i, pref[i]] for i in pref]), key = lambda x: x[1], reverse = True)
    
    # print(pref)
    rec_lst = sorted(list(set([i[0] for i in products]) - set(purchased)))

    # print(rec_lst)
    rec_lst_tmp = rec_lst[:]
    
    
    for i in pref: # 선호
        for j in rec_lst_tmp:  # 구매하지 않은 리스트
            if i[0] not in products_dic[j]:
                rec_lst_tmp.remove(j)
                print(rec_lst_tmp, rec_lst)
        if len(rec_lst_tmp) == 0:
            rec_lst_tmp = rec_lst
        elif len(rec_lst_tmp) == 1:
            return rec_lst_tmp[0]
            



print(solution(["sofa red long", "blanket blue long", "towel red", "mattress long", "curtain blue long cheap"],["towel", "mattress", "curtain"] ))
print(solution(["towel red long thin", "blanket red thick short", "curtain red long wide", "mattress thick", "hat red thin", "pillow red long", "muffler blue thick long"],["blanket", "curtain", "hat", "muffler"]))

