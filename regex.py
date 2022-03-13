import re
print("Vvedite nomer zadaniya: ")
a = int(input())
print("Vvedite stroku: ")
line = input()
if a == 1:
    x = re.search(r'ab*', line)
    if x: print("Yes")
    else: print("No")
if a == 2:
    x = re.search(r'ab{2,3}$', line)
    if x: print("Yes")
    else: print("No")  
if a == 3:
    x = re.search(r'^[a-z]+_[a-z]+$', line)
    if x: print("Yes")
    else: print("No") 
if a == 4:
    x = re.search(r'[A-Z]{1}+_[a-z]+$', line)
    if x: print("Yes")
    else: print("No") 
if a == 5:
    x = re.search(r'a.*b$', line)
    if x: print("Yes")
    else: print("No") 
if a == 6:
    x = re.sub('[\s.,]','{}', line)
    print(x)
if a == 7:
    line = line.title()
    for i in range(len(line)):
      if line[i]!='_':
          print(line[i], end='')
if a == 8:
    x = re.findall(r'[A-Z]{1}[a-z]*', line)
    for i in x:
        print(i,end=' ')
if a == 9:
    x = re.findall(r'[A-Z]{1}[a-z]*', line)
    for i in x:
        print(i,end=' ')
if a == 10: 
    x = re.findall(r'[A-Z]+[a-z]*', line)
    x = [l.lower() for l in x]
    line = '_'.join(x)
    print(line)