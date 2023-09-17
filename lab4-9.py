sentence=input('enter any sentence')
c_count=0
s_count=0
d_count=0
sp_count=0
index=0
while index<=len(sentence):
 char=sentence(index)
 if 'A'<=char<='Z':
  c_count+=1
 elif 'a'<=char<='z':
  s_count+=1
 elif 0<=char<=9:
  d_count+=1
 else:
  sp_count+=1
index+=1
print(c_count)
print(s_count)
print(d_count)
print(sp_count)