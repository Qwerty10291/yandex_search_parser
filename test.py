import re

file = open('out1.csv', 'r', encoding='utf-8').readlines()
filtered = filter(lambda x: re.match(r'.+;\d+;.+;.+', x), file)
out = sorted(filtered, key=lambda x: int(x.split(';')[1]), reverse=True)
open('deploy.txt', 'w').write(''.join(out))