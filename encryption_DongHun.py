# 암호문.txt 생성 코드
print("-"*10,"2019E7178 최동훈","-"*10,"\n")
print("-"*13,"키값.txt","-"*15)

#텍스트 파일 읽기
f1 = open("C:\텍스트파일\키값.txt","r")
key = f1.read()
print(key)
f1.close()

f2 = open("C:\텍스트파일\평문.txt","r")
plainText = f2.read().lower()
print("-"*37)
f2.close()

arr = key.split()

#알파벳 갯수별로 딕셔너리 저장
dic = {}
for a in range(0,26):
        dic[arr[a][0]]=arr[a][2]

#키 기준으로 오름차순 정렬
key_Dic = sorted(dic.items(),key=lambda x : x[0])   #x[0]은 키 , x[1]은 값을 의미함
print(key_Dic)

#값 기준으로 오름차순 정렬
value_Dic = sorted(dic.items(),key=lambda x : x[1])   #x[0]은 키 , x[1]은 값을 의미함
print(value_Dic)

list_text = list(plainText) #plainText를 리스트형태로 저장

copy = [""]*len(list_text)  #copy라는 임의의 문자열 리스트 생성
print(list_text)


for ch in range(0, len(list_text)):
   for i in range(0,len(key_Dic)):
        if list_text[ch]==key_Dic[i][0]:
            copy[ch] = value_Dic[i][0]
        elif list_text[ch]==" ":     #띄어쓰기인 경우
            copy[ch]= " "
        elif list_text[ch]=="\n":    #줄바꿈인 경우
            copy[ch]="\n"

        #특수 문자인 경우
        elif list_text[ch] == "[":
            copy[ch] = "["
        elif list_text[ch] == "]":
            copy[ch] = "]"
        elif list_text[ch] == ":":
            copy[ch] = ":"
        elif list_text[ch] == ";":
            copy[ch] = ";"
        elif list_text[ch] == "'":
            copy[ch] = "'"
        elif list_text[ch] == '"':
            copy[ch] = '"'

        #숫자인 경우
        elif list_text[ch].isdigit():
            copy[ch]=list_text[ch]
        else:
            continue

new_file = open("C:\텍스트파일\암호문.txt","w")
print("\n")
print("-"*11,"암호화한 문장","-"*13)
print(copy)

#암호문.txt 파일 쓰기
for i in copy:
    print(i,end=" ")
    new_file.write(i)

print("\n")
print("-"*37)

new_file.close()
