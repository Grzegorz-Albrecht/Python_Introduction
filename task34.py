stih=input()   
stih=stih.split()
itog=list()

for fraz in stih:
    gls=0
    lala=list(filter(lambda x: x in 'УуЕеЫыАаОоЭэЯяИиЮюЁё',fraz))
    for i in lala:
        gls+=1
    itog.append(gls) 
if len(set(itog))==1:
    print('Парам пам-пам')
else:
    print('Пам парам')
