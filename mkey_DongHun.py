# 키값.txt 생성 코드
print("-"*10,"2019E7178 최동훈","-"*10,"\n")
print("-"*15,"평문","-"*17)

#텍스트 파일 읽기
f = open("C:\텍스트파일\평문.txt","r")
text = f.read().lower()             #평문을 읽고 소문자로 변환
print(text)                         #평문 출력

#공백과 줄바꿈 제거
new_text = text.replace(" ","").replace("\n","")

#알파벳 개수를 세기 위한 리스트
cnt = [0]*26

#알파벳 종류를 문자열로 선언
alphabet = "abcdefghijklmnopqrstuvwxyz"

print("-"*37)


#알파벳 개수 세기
for i in text:
    if i in alphabet:
        idx = alphabet.find(i)   #alphabet 문자열에서 같은 문자를 찾아 인덱스 위치를 알려줌
        cnt[idx] += 1


key = open("C:\텍스트파일\키값.txt","w")

#알파벳 개수 출력
print("\n")
print("-"*12,"알파벳 개수","-"*14)

for i in range(0,26):
    print(alphabet[i]+"의 개수 : ",cnt[i])
    arr = alphabet[i]+"="+str(cnt[i])+"\n"
    key.write(arr)

print("-"*37)
