from base import *


def io_heavy(text, base):
    start = time.time() - base
    f = open('output.txt', 'wt', encoding='utf-8')
    f.write(text)
    f.close()
    stop = time.time() - base
    return start, stop


f = open('input.txt', 'rt', encoding='utf-8')
text = f.read()
f.close()
texts = [text + text] * 8

run_test(io_heavy, texts)
