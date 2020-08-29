def solution(dataSource, tags):
    answer = []
    doc_dic = { data[0] : 0 for data in dataSource }


    for tag in tags:
        for i in range(len(dataSource)):
            for j in range(1, len(dataSource[i])):
                if tag == dataSource[i][j]:
                    doc_dic[dataSource[i][0]] += 1

    # answer = sorted(doc_dic.items(), key=lambda item: (item[1], item[0]), reverse = True)
    answer = sorted(sorted(doc_dic.items(), key = lambda item : item[0]), key = lambda item : item[1], reverse = True)  

    answer_lst = []
    if len(answer) > 10: 
        for i in range(10):
            if answer[i][1] != 0:
                answer_lst.append(answer[i][0])
    else:
        for i in range(len(answer)):
            if answer[i][1] != 0:
                answer_lst.append(answer[i][0])


    return answer_lst







dataSource = [
    ["doc1", "t1", "t2", "t3"],
    ["doc2", "t0", "t2", "t3"],
    ["doc3", "t1", "t6", "t7"],
    ["doc4", "t1", "t2", "t4"],
    ["doc5", "t6", "t100", "t8"]
]

dataSource1 = [
    ["doc1", "t1", "t5", "t3"],
    ["dac2", "t0", "t6", "t3"],
    ["doc3", "t1", "t5", "t3"],
    ["dac4", "t0", "t6", "t3"],
    ["doc5", "t1", "t5", "t3"],
    ["dac6", "t0", "t6", "t3"],
    ["dzc7", "t1", "t5", "t3"],
    ["dac8", "t0", "t6", "t3"],
    ["doc9", "t1", "t5", "t3"],
    ["dac10", "t0", "t6", "t3"],
    ["dac11", "t1", "t5", "t3"],
    ["doc21", "t0", "t6", "t3"],

    ["doc11", "t1", "t5", "t3"],
    ["dac221", "t0", "t6", "t3"],
    ["dac31", "t1", "t6", "t7"],
    ["doc41", "t6", "t2", "t4"],
    ["doc51", "t6", "t1", "t2"]
]

