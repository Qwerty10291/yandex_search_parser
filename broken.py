from os import error


file1 = open('подсказки.txt', 'r', encoding='utf-8')
file2 = open('out1.csv', 'r', encoding='utf-8')
file_out = open('errors.txt', 'w')
l2 = list(map(lambda x: x.split(';'), file2.readlines()))
l1 = list(map(lambda x: x.split(';'), file1.readlines()))
errors = set(map(lambda x: x[0], l1)) - set(map(lambda x: x[0], l2))
print(len(list((errors))))
errors1 = filter(lambda x: x[0] in errors, map(lambda x: [x[0], x[1][:-1]], l1))
file_out.write('\n'.join(map(lambda x: ';'.join(x), errors1)))