import random
from operator import itemgetter

vaccin = [["백신1",25],["백신2",50],["백신3",100]]
country = [["한국",1500,300],["중국",3000,800],["일본",2000,500],["미국",2500,750],["독일",2200,1000]]
nation = []



def name():
    print("------------------")
    print("코로나 종식 게임")
    print("------------------")
    print("1.백신 정보\n")
    print("2.감염된 국가 정보\n")
    print("3.게임 시작\n")
    print("4.게임 종료")
    print("------------------")



def vaccinInfo():
  print("백신 이름 : 백신1 \n백신 치료율 : 25%""\n")
  print("백신 이름 : 백신2 \n백신 치료율 : 50%""\n")
  print("백신 이름 : 백신3 \n백신 치료율 : 100%""\n")



def conInfo():
  for num in range(5):
    print("감염 국가:",country[num][0])
    print("인구수: %d"% (country[num][1]),"명")
    print("감염 인구수: %d"% (country[num][2]),"명","\n")





plus = 0
cure = 0

def final(plus,cure):
  print("라운드마다 추가로 감염된 감염자 수: %d명"% (plus))
  print("백신으로 치료된 감염자 수: %d명"% (cure))
  print("백신으로 완치된 국가:",nation[0],"\n")
  
  for result in range(5):
    print("%d위"% (result+1))
    print("국가 : ",country[result][0])
    print("인구수 : ",int(country[result][1]),"명")
    print("감염 인구수 : ",int(country[result][2]))

def gameStart(plus,cure):
  print("사용할 백신(1~3)과 백신을 적용할 국가(1~5)의 번호를 차례대로 입력하세요")
  vacNum, useCon = input().split()
  vacNum = int(vacNum)-1
  useCon = int(useCon)-1



  savecon = " "  
  curecon = ""
  for gameTry in range(5):
    print("★ %d"%(gameTry+1)+"번째 시도 ★")
    print("선택된 백신:", vaccin[vacNum][0], "치료율:%d"% (vaccin[vacNum][1]))
    print("선택된 나라:", country[useCon][0], "인구수: %d"% (country[useCon][1]), "감염자수: %d"% (country[useCon][2]))

    condition = True
    
    for all_cure in range(5):
        if country[all_cure][2] != 0:
           condition = False
    for number in range(5):
        if number != useCon:
           if country[number][2] == 0:
              continue
           plus += country[number][1]*15/100 
           country[number][2] += country[number][1]*15/100
        else:
           cure += country[number][2]*vaccin[vacNum][1]/100
           country[number][2] -= country[number][2]*vaccin[vacNum][1]/100
           if country[number][2] == 0:
              curecon = country[number][0]
              savecon += curecon
              savecon += " "
           else:
              curecon = "없음" 
    print("===========================================")
    print("완치된 나라:", curecon)
    print("%d차 백신 투여 후 감염된 나라에 대한 정보"% (gameTry+1))
    print("===========================================")


    conInfo()

    for check in range(5):
        if country[check][1] < country[check][2]:
            print("감염자 수가 인구 수보다 많은 국가가 발생하였습니다. 게임을 중단합니다 !")
            print("===========================================")
            print("                최종 결과                  ")
            print("===========================================")
            print("라운드마다 추가로 감염된 감염자 수: %d명"% (plus))
            print("백신으로 치료된 감염자 수: %d명"% (cure))
            print("백신으로 완치된 국가:",savecon,"\n")

            for result in range(5):
                print("%d위"% (result+1))
                print("국가 : ",country[result][0])
                print("인구수 : ",int(country[result][1]),"명")
                print("감염 인구수 : ",int(country[result][2]),"\n")
            return

        elif country[check][2] == 0:
            nation.append(country[check][0])

            
    vacNum = random.randrange(0,3)
    useCon = random.randrange(0,5)

  if condition == True:
    print("모든 국가가 완치되었습니다")  
  print("===========================================")
  print("                최종 결과                  ")
  print("===========================================")
  print("라운드마다 추가로 감염된 감염자 수: %d명"% (plus))
  print("백신으로 치료된 감염자 수: %d명"% (cure))
  print("백신으로 완치된 국가:",savecon,"\n")


  country.sort(key=itemgetter(2))
  for result in range(5):
    print("%d위"% (result+1))
    print("국가 : ",country[result][0])
    print("인구수 : ",int(country[result][1]),"명")
    print("감염 인구수 : ",int(country[result][2]),"\n")    


while True:
  name()
  menuNum = int(input())
  if menuNum == 1:
    vaccinInfo()
  if menuNum == 2:
    conInfo()
  if menuNum == 3:
    gameStart(plus,cure)
  if menuNum == 4:
    print("게임을 종료합니다")
    break

           

