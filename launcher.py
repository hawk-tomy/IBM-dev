import subprocess,shlex

cmd1 = 'python src/bank.py'
#cmd2 = 'python src/IBM.py'

p1 = subprocess.Popen(shlex.split(cmd1),shell=True)
#p2 = subprocess.Popen(shlex.split(cmd2),shell=True)

p1.wait()
#p2.wait()
