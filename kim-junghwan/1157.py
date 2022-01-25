##알파벳 대소문자로 된 단어가주어지면, 이 단어에서
##가장 많이 사용된 알파엣이 무엇인지 알아내는 프로그램을
#작성하시오. 대문자 소문자 구분하지 않는다.

a=input().upper() ##upper 소문자를 대문자로
list_words= list(set(a))
list=[]
for i in list_words:
    cut=a.count(i)
    list.append(cut)
    
if list.count(max(list)) > 1:
    print('?')
    
else :
    max_index=list.index(max(list))
    print(list_words[max_index])   
