def buffer(ini,out): 
   with open(ini, 'r') as f:
           lines = f.readlines()
   for i, line in enumerate(lines):
     with open(out, 'a') as f:
        f.write(line)
