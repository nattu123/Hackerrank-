dic = {}
for  i in input() : 
  
    
    if i not in dic:
        dic[i]=0 
    dic[i]+=1

dic=dict(sorted(dic.items())   )
print(dic) 
v= list(dic.values())
k= list(dic.keys())

for i in range(3):
     print(k[v.index(max(v))],v[v.index(max(v))])
     
     del_=v.index(max(v))
    
     v.pop(del_)
     k.pop(del_)