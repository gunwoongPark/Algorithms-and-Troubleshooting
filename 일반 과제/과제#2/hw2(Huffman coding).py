from collections import Counter
import heapq

# 허프만 트리 생성
def make_huff_tree(frequencies):
    heap = [[weight, [symbol, '']] for symbol, weight in frequencies.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

# 허프만 압축
def huff_compression(huff_tree, sentence):
    encoding_sentence = ""
    for word in sentence:
        for index in range(len(huff_tree)):
            if word == huff_tree[index][0]:
                encoding_sentence += huff_tree[index][1]

    return encoding_sentence

# 압축률 계산
def get_compression_ratio(sentence_len, frequencies, huff_tree):
    ascii_size = sentence_len * 8
    encoding_size = 0

    for word in huff_tree:
        encoding_size += frequencies[word[0]] * len(word[1])

    return (encoding_size/ascii_size) * 100

# 허프만 압축 해제
def huff_decompression(huff_tree, encoding_sentence):
    decoding_sentence = ""
    temp = ""

    for word in encoding_sentence:
        temp += word

        if len(temp) >= 2:
            for index in range(len(huff_tree)):
                if huff_tree[index][1] == temp:
                    decoding_sentence += huff_tree[index][0]
                    temp = ""
                    break

    return decoding_sentence

def main():
    sentence = "add fasd dfa aas dd fd saad fasf aas fdd dfaas df dfff sdgg fsgsas"
    print("문장 : {}\n".format(sentence))

    sentence = sentence.replace(" ", "")
    sentence_len = len(sentence)

    # 빈도수
    frequencies = dict(Counter(sentence))
    print("빈도수 : {}\n".format(frequencies))

    # 허프만 트리 구현(교재의 코드 사용)
    huff_tree = make_huff_tree(frequencies)
    print("허프만 트리 : {}\n".format(huff_tree))

    # 허프만 압축
    encoding_sentence = huff_compression(huff_tree, sentence)
    print("압축된 문장 : {}\n".format(encoding_sentence))

    # 압축률
    compression_rate = get_compression_ratio(sentence_len, frequencies, huff_tree)
    print("압축률 : {}\n".format(compression_rate))

    # 압축 풀기
    decoding_sentence = huff_decompression(huff_tree, encoding_sentence)
    print("압축 해제된 문장 : {}".format(decoding_sentence))

if __name__ == "__main__":
    main()
