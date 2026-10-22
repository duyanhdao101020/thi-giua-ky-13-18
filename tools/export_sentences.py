# Doc js/data.js -> data/sentences.txt va tao lai tao_mp3.py (tu chua san cac cau, chi ASCII).
import re, json, pathlib
r = pathlib.Path(__file__).resolve().parent.parent
raw = re.search(r'const RAW=`(.*?)`;', (r / 'js/data.js').read_text('utf8'), re.S).group(1).strip().split('\n')
S = []
for n, l in enumerate(raw, 1):
    a, w, v, s = l.split('|')
    assert w in s, f'Tu "{w}" khong co trong cau: {s}'
    S.append([f's{n:02d}', s])
(r / 'data/sentences.txt').write_text(''.join(f'{i}|{s}\n' for i, s in S), 'utf8')
tpl = (r / 'tools/tao_mp3_template.py').read_text('utf8')
(r / 'tao_mp3.py').write_text(tpl.replace('__SENTENCES__', json.dumps(S, ensure_ascii=True)), 'utf8')
print(len(S), 'cau -> data/sentences.txt va tao_mp3.py')
