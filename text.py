def revword(word):
    return word[::-1].lower()


def countword():
    cnt=1
    txt= open('text.txt','r')
    txt=txt.read()
    txt=txt.replace('\n',' ') 
    txt=(txt.lower())
    word1=txt.split()
    for i in range(1,len(word1)):
        if word1[0]==revword(word1[i]):
           cnt = cnt + 1 
    return cnt


 countword()   
