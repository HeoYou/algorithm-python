from collections import deque

def check_word(word1, word2):
    count = 0
    for i in range(len(word1)):
        if word1[i] == word2[i]:
            count += 1
    return 1 if count == len(word1) - 1 else 0


def solution(begin, target, words):
    answer = 100000
    stack = deque([[begin, 0]])
    visit = []

    while stack:

        node = stack.popleft()
        if node[0] == target:
            return node[1]
        
        for word in words:
            if word in visit:
                continue
            if check_word(node[0], word):
                visit.append(word)
                stack.append([word, node[1] + 1])

    return 0


if __name__=='__main__':
    begin = 'hit'
    target = 'cog'
    # words = ["hot", "dot", "dog", "lot", "log", "cog"]
    words = ["hot", "dot", "dog", "lot", "log"]
    print(solution(begin, target, words))