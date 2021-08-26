import subprocess, glob, json, time
import multiprocessing as mp
from multiprocessing import Pool, cpu_count

project = 'retrospective_s1_rna'
i_dir = '/data1/jaemin_1/pdiamond_raw'
o_dir = '/data2/jaemin_2/wes'
number_process = 1


start_time = time.time()
cmds = []

subprocess.run(' '.join(['sudo mkdir -p ', '/'.join([o_dir, project, 'fastqc', 'multiqc'])]), shell = True)


file_path = '/'.join(['/data1', 'jaemin_1', 'pdiamond_raw', 'retrospective_s1_rna', 'HN00137093'])
cmds.append(' '.join(['fastqc',
                      '-o', '/'.join([o_dir, project, 'fastqc', 'multiqc'])]),
                     '-t', '1',
                     '/'.join([file_path, 'RE-P002-T-3_1.fastq.gz']),
                     '/'.join([file_path, 'RE-P002-T-3_2.fastq.gz']))

subprocess.run(cmds, shell = True)

def operate(x):
    s_time = time.time()
    print(x)
    subprocess.run(x, shell = True)
    print('sample finished time :', time.time() - s_time, 'sec')

pool = mp.Pool(number_process)
pool.map(operate, cmds)
pool.close()

cmd = 'chmod -R 777 ' + '/'.join([o-dir, project, 'fastqc'])
print(cmd)
subprocess.run(cmd, shell = True)

cmd = ' '.join(['multiqc', '/'.join([o_dir, project, 'fastqc']),
                '-o', '/'.join([o_dir, project, 'fastqc/multiqc'])])

print(cmd)
subprocess.run(cmd, shell = True)

print('project finished time :', time.time() - start_time, 'sec')
