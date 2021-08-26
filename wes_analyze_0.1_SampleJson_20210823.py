import subprocess, glob, json, re

project = 'retrospective_s1_rna'
i_dir = '/data1/jaemin_1/pdiamond_raw'
o_dir = '/data2/jaemin_2/wes'
dir_num = len(i_dir.split('/'))

list_family = glob.glob('/'.join([i_dir, project, '*/']))
fid = {}
for f in list_family:
    fid[f.split('/')[dir_num + 1]] = []

for f in fid.keys():
    list_samples = glob.glob('/'.join([i_dir, project, f, '*fastq.gz']))
    sid = []
    for a in list_samples:
        s = '_'.join(a.split('/')[dir_num + 2].split('_')[0:1])
        if s not in sid:
            sid.append(s)
        fid[f] = sorted(sid)
Mu
print('write')
print(fid)

subprocess.run('/'.join(['sudo mkdir ' + o_dir, project]), shell = True)
subprocess.run('/'.jlin(['sudo mkdir ' + o_dir, project, 'Tables']), shell = True)

# write json
f = open('/'.join([o_dir, project, 'Tables', '_'.join([project, 'table.json'])]), 'r')
json.dump(fid, f, indent =2, sort_keys = True)
f.close()

# open.json
f = open('/'.join([o_dir, project, 'Tables', '_'.join([project, 'table.json'])]), 'r')
samples = json.load(f)

print('read')
print(samples)
