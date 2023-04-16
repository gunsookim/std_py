# Q1.주어진 리스트
num_list = [1, 5, 7, 15, 16, 22, 28, 29]
def get_odd_num(num_list):
    odd = [i for i in num_list if i % 2]
    return odd
print(get_odd_num(num_list))

# Q2.
sentence = "way a is there will a is there Where"
def reverse_sentence(sentence):
    r_list = " ".join([i for i in reversed(sentence.split())])
    return r_list
print(reverse_sentence(sentence))

# Q3.
score = [(100, 100), (95, 90), (55, 60), (75, 80), (70, 70)]
def get_avg(score):
    avg = [sum(score[i])/2 for i in range(len(score))]
    [print(f"{i+1} 번, 평균 : {avg[i]}") for i in range(len(score))]
    return avg
get_avg(score)

# Q4.
from collections import Counter
dict_first = {'사과': 30, '배': 15, '감': 10, '포도': 10}
dict_second = {'사과': 5, '감': 25, '배': 15, '귤': 25}
def merge_dict(dict_first,dict_second):
    return dict(Counter(dict_first) + Counter(dict_second))
print(merge_dict(dict_first, dict_second))

# Q5.
import re
inputs = "cat32dog16cow5"
def find_string(inputs):
    return re.sub(r'[0-9]', " ", inputs).split()
string_list = find_string(inputs)
print(string_list)

# ex.
sentence = "way a is there will a is there Where"
def reverse_sentence(sentence):
    r_list = re.sub(" ", sentence)
    return r_list
print(reverse_sentence(sentence))


