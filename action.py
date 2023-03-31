import random, time, os, platform
import main

# 창 새로고침, 텍스트가 계속 쌓이면 가독성에 좋지 않음
def new_cmd():
    com_os = platform.system()  # 사용자 시스템의 os가 무엇인지 탐색
    input("\nENTER 키를 눌러 다음으로 진행하세요")  # 새로고침이 되기 전 나온 정보들을 사용자가 읽고 넘어갈 수 있도록 엔터 입력 후 창 새로고침 진행
    if com_os == 'windows': # 환경이 윈도우라면 cls 입력
        os.system('Cls')
    else:   # 환경이 리눅스나 맥이라면 clear 입력
        os.system('Clear')

def player_action(list):
    mon_list = list 
    while True: # while문을 사용해 break를 걸 때 까지 계속 실행
        try:
           
            print("""

            ￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣
            |　공격 개시!　　　　　　　　　　　　　　　　　　　　[－][口][×] |
            |￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣|
            |　나에게는 2가지의 공격 방법이 있다 .어떤 방법을 선택할까 ??   |
            |　　　　　　　　　　　　　　　　　　　　　　　　　           　|
            |　　　　     ＿＿＿＿＿＿　　　　    ＿＿＿＿＿＿　　　　　    |
            | 　　　     ｜1. 물리공격　　　　   ｜2. 마법공격｜ 　 　 　   |
            |　　　     　￣￣￣￣￣￣　　　　    ￣￣￣￣￣￣　　　　　　  |
            ￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣
            """)
            player_skill_input = int(input("\n공격할 방식의 번호를 입력해주세요: "))
            if player_skill_input == 0 or player_skill_input > 2:   # 1,2 외에 다른 숫자가 들어오면 다시 입력
                print("공격방식을 다시 입력해주세요")
                continue  # while문을 처음부터 다시 시작함
            
            if player_skill_input == 2:
                if p1.mp < 5:
                    print("스킬을 사용하는데 필요한 MP가 모자랍니다.")
                    continue 
        except ValueError:  # ValueError가 나왔을때 execpt문 실행
            print("공격방식을 숫자로 입력해주세요")
            continue 
            
        break  # while문을 빠져나옴

    print("\n===공격 대상 선택===")
    for i, m in enumerate(mon_list):    # enumerate함수를 사용해 i는 순서를 m은 m1,m2와 같은 몬스터 변수를 입력
        print(f"{i+1}. {m.id} (HP: {m.hp} / {m.max_hp})")

    while True: # while문을 사용해 break를 걸 때 까지 계속 실행
        try:    
            player_target_input = int(input("\n공격할 대상의 번호를 입력해주세요: ")) 
            if player_target_input <= 0 or player_target_input > len(mon_list): # 0 또는 리스트의 갯수보다 더 많은 숫자 입력 시 다시 입력
                print("잘못된 대상을 선택하셨습니다. 다시 선택해주세요.")
                continue 
        except ValueError:  # ValueError가 나왔을때 execpt문 실행
            print("대상 번호를 숫자로 입력해주세요.")
            continue
            
        break

    target = mon_list[player_target_input -1]

    if player_skill_input == 1: # 공격방식의 번호 입력이 1(노말어택)이라면
        p1.attack(target)    # main 파일 Player 클래스의 attack함수 실행
    elif player_skill_input == 2: # 공격방식의 번호 입력이 2(매직어택)이라면
        p1.magic_attack(target)


def monster_action(monsters):  
    # 살아있는 몬스터들만 행동
    action_num = random.randint(1, 3)
    for monster in monsters:
        if action_num == 1:
            monster.cure(monster.max_hp)
        elif action_num == 2:
            monster.wait()
        elif action_num == 3:
            monster.attack(p1)

# 몬스터 리스트 제거 함수(반복문으로 간략화 가능해 보임)
def monster_death(monsters_list, player):  
    for m in monsters_list:
        if m.hp <= 0:
            monsters_list.remove(m)
            player.gain_exp(m.get_exp())


def dungeon_03(dungeon, monster1, monster2, monster3):    
    dungeon.enter()

    dungeon.append_monsters(monster1, monster2, monster3)

    monsters_list = [monster1, monster2, monster3]

    turn = 1
    while True: # break가 걸릴 때 까지 반복 실행
        new_cmd()
        
        print(f"\n====={turn}번째 턴====")  # f_string을 이용
        time.sleep(0.3) # 텍스트가 한번에 입력되는 것을 방지함, 좀 더 게임처럼 즐길 수 있음
        p1.show_status() # p1 = 플레이어, 플레이어의 상태를 보여주는 status함수를 사용
        for m in monsters_list:  # 몬스터 리스트에 있는 몬스터들을 m이라는 변수에 순차 저장
            m.status()
            time.sleep(0.3)

        print("\n===플레이어 턴===")
        player_action(monsters_list)   # 플레이어 행동함수 실행
        monster_death(monsters_list, p1) # 몬스터 리스트 제거 함수 실행
        

        if monsters_list == []:  # 몬스터가 모두 죽어서 리스트가 비어버렸다면
            print("\n====clear!====\n당신이 승리했습니다.")
            # print("1. 전투를 계속 진행하기\n2. 마을로 돌아가기") 
            # if action_select not in [1, 2]:
            #     print("다시 입력해주세요")
            #     continue
            # # elif action_select == 1:
            #     #전투가 계속된다.
            # elif action_select == 2:
                
            # # 마을로 돌아간다.
            # # break 반복문 종료
            break
        
        print("\n===몬스터 턴===")
        time.sleep(0.3)
        monster_action(monsters_list)  # 몬스터 행동함수 실행

        if p1.hp <= 0:  # 플레이어의 체력이 0보다 같거나 작다면
           
            print("\n당신이 사망하였습니다.\n 마을로 돌아갑니다.")
            print("""

            ￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣ 
            |　마을 광장 　　　　　　　　　　　　　　　　　　　　[－][口][×] |
            |￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣|
            |　마을에 도착했다! 뭘 해볼까?                                  |
            |　　　　　　　　　　　　　　　　　　　　　　　　　           　 |
            |　　　　  ＿＿＿＿＿＿　　　　    ＿＿＿＿＿＿＿＿＿　　　　　  |
            | 　　　 ｜1. 던전 진입　　　　   ｜2. 마을 구경하기｜ 　 　 　  |
            |　　　  　￣￣￣￣￣￣　　　　    ￣￣￣￣￣￣￣￣￣　　　　　　|
            ￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣
            """)

            # print("1. 던전 진입\n2. 마을 구경하기")
            break   # 반복문 종료

        turn += 1   # 턴 + 1
        print("\n====턴 종료====")    # 위의 break에 걸리지 않았다면 다시 반복문으로 돌아감
        time.sleep(0.3) 

# 게임 실행 부분
# p1을 Player클래스로 생성하고 이후 직업선택에 따라 해당 직업으로 클래스를 옮기게 만들었습니다.
p1 = main.Player(input("이름을 입력해주세요."))
while True:
    choice = input("진행하려면 Y / 다시하려면 N 을 입력해주세요: ")
    if choice in ["N", "n"]:
        p1 = main.Player(input("이름을 입력해주세요: ")) # N을 입력할 경우 p1 재선언
        continue
    elif choice in ["Y", "y"]:
        break
    elif choice not in ["Y", "N", "y", "n"]:  # 입력값이 Y/N이 아니라면 continue로 다시 반복
        print("Y 또는 N을 입력해주세요")
        continue
    else:
        print()   # Y가 들어오면 함수 종료


print("====직업 선택====\n1.프론트엔드\n2.벡엔드")
if p1.html > 25 and p1.javascript > 25 and p1.python > 25:
    print("3.풀스택(히든)")
while True:
    job_select = int(input("원하시는 직업을 선택해주세요"))
    if job_select == 1:
        p1 = main.Frontend(p1.id, p1.hp, p1.mp, p1.html, p1.javascript, p1.python)
        print("(예비)프론트엔드 직업을 가지게 되었습니다.")
        break
    elif job_select == 2:
        p1 = main.Backend(p1.id, p1.hp, p1.mp, p1.html, p1.javascript, p1.python)
        print("(예비)백엔드 직업을 가지게 되었습니다.")
        break
    elif job_select == 3:
        if p1.html > 10 and p1.javascript > 10 and p1.python > 10:
            p1 = main.Fullstack(p1.id, p1.hp, p1.mp, p1.html, p1.javascript, p1.python)
            print("(히든)풀스택 직업을 가지게 되었습니다.")
            break
    else:
        print('올바른 직업번호를 입력해주세요')
        continue

# 던전 
first_dungeon = main.Dungeon("초급강의 던전")
second_dungeon = main.Dungeon("점프 투 파이썬 던전")
third_dungeon = main.Dungeon("심화강의 던전")
fourth_dungeon = main.Dungeon("정올 던전")
fifth_dungeon = main.Dungeon("백준 던전")
sixth_dungeon = main.Dungeon("프로그래머스 던전")
seventh_dungeon = main.Dungeon("쿠팡 던전")
eighth_dungeon = main.Dungeon("삼성 던전")
ninth_dungeon = main.Dungeon("카카오 던전")
tenth_dungeon = main.Dungeon("네이버 던전")

# 몬스터 - 몬스터 공격력 더 낮게 조정하기
mons1 = main.Monster('예제(초급)', 30, 10, 10)
mons2 = main.Monster('예제(중급)', 35, 15, 15)
mons3 = main.Monster('예제(고급)', 40, 20, 20)
mons4 = main.Monster('예제(심화)',45, 25, 25)
mons5 = main.Monster('백준(브론즈)', 50, 30, 30)
mons6 = main.Monster('백준(실버)', 55, 35, 35)
mons7 = main.Monster('백준(골드)', 60, 40, 40)
mons8 = main.Monster('백준(플레)', 65, 45, 45)
mons9 = main.Monster('프로그래머스(LV.0)', 70, 50, 50)
mons10 = main.Monster('프로그래머스(LV.1)', 75, 55, 55)
mons11 = main.Monster('프로그래머스(LV.2)', 80, 60, 60)
mons12 = main.Monster('코테(쿠팡)', 85, 65, 65)
mons13 = main.Monster('코테(삼성)', 90, 65, 65)
mons14 = main.Monster('코테(카카오)', 95, 65, 65)
mons15 = main.Monster('코테(네이버)', 100, 65, 65)

#포션
redportion = main.Equipment('빨간물약', 100, 0)
blueportion = main.Equipment('파란물약', 0, 100)

# 장비
hongongpa = main.Equipment('혼공파',0,0,3,3,3)
mouse = main.Equipment('마우스', 0,0,5,5,5)
keyboard = main.Equipment('키보드',0,0,5,1,10)
macbook = main.Equipment('맥북', 0,0,5,10,1)
chatgpt = main.Equipment('(전설)챗GPT',0,0,15,15,15)

# 0331 점심시간 팀장님
while True:
    if p1.level <= 5:
        print('---------------------')
        print('---- 내배캠 마을 ----')
        print('---------------------\n')
        print("1. 던전 진입\n2. 마을 구경하기")

        while True:
            action_select = int(input("행동을 선택해 주세요: "))
            if action_select not in [1, 2]:
                print("다시 입력해주세요")
                continue
            elif action_select == 1:
                print("1. 초급강의 던전\n2. 점프 투 파이썬 던전\n3. 심화강의 던전\n4. 뒤로가기")
                # 4. 뒤로가기
                dungeon_select = int(input("던전을 선택해 주세요: "))
                if dungeon_select not in [1, 2, 3, 4]:
                    print("다시 선택해주세요")
                    continue #뒤로가기가 elif로 가야된다.
                elif dungeon_select == 1:
                    dungeon_03(first_dungeon, mons1, mons2, mons3)
                elif dungeon_select == 2:
                    dungeon_03(second_dungeon, mons2, mons3, mons4)
                elif dungeon_select == 3:
                    dungeon_03(third_dungeon, mons3, mons4, mons5)
                # else:
                #     break # 마을 메뉴로 돌아감            
            elif action_select == 2:
                print("""

                                ට              ◝◜
                                    ට      ◝◜
                        🌞✧
                        ☁️        ༄          ☁️༄
                                    ☁️༄
                            ✧
                        ╱◥◣
                        │∩ │◥███◣ ╱◥███◣
                        ╱◥◣ ◥████◣▓∩▓│∩
                        │╱◥█◣║∩∩∩ ║◥█▓ ▓█

                """)
                time.sleep(3)
                print("""
                        평화로운 내배캠 마을을 
                        코딩 몬스터가 장악했다!
                        나의 갈고닦은 팀플 실력으로
                        코딩 몬스터들을 때려잡아보자!
                """)
                time.sleep(3)
            continue 
    # 던전에 몬스터의 수를 바꾸고 싶으면 dungeon_00으로 함수를 복사하여 생성한 후 만져야 한다.    
          
    elif 5 < p1.level <= 10:

        print('-----------------------')
        print('---- 알고리즘 마을 -----')
        print('---------------------\n')
        while True:
            action_select = int(input("행동을 선택해 주세요: "))
            if action_select not in [1, 2]:
                print("다시 입력해주세요")
                continue
            elif action_select == 1:
                print("1. 정올 던전\n2. 백준 던전\n3. 프로그래머스 던전\n4. 뒤로가기")
                # 4. 뒤로가기
                dungeon_select = int(input("던전을 선택해 주세요: "))
                if dungeon_select not in [1, 2, 3, 4]:
                    print("다시 선택해주세요")
                    continue #뒤로가기가 elif로 가야된다.
                elif dungeon_select == 1:
                    dungeon_03(fourth_dungeon, mons5, mons6, mons7)
                elif dungeon_select == 2:
                    dungeon_03(fifth_dungeon, mons6, mons7, mons8)
                elif dungeon_select == 3:
                    dungeon_03(sixth_dungeon, mons7, mons8, mons9)
            elif action_select == 2:
                print("""

                        성적을 확인해볼까?
                            ( ՞ਊ ՞ )　
                        ＿(_つ/￣￣/＿
                        　 ＼/＿＿/

                        하하하하하하 으하하하하
                        　　　　　 ／＼
                        　　.∵　／　／|
                        　　　ﾟ∴＼／／
                        (ﾉ ՞ਊ ՞ﾉ|／
                        /　　/

                """)
                time.sleep(3)
                print("""
                        알고리즘을 풀다 
                        
                """)
                time.sleep(3)

            continue  
    else:
        print('---------------------')
        print('----- 코테 마을 -----')
        print('---------------------\n')
        while True:
            action_select = int(input("행동을 선택해 주세요: "))
            if action_select not in [1, 2]:
                print("다시 입력해주세요")
                continue
            elif action_select == 1:
                print("1. 쿠팡 던전\n2. 삼성 던전\n3. 카카오 던전\n4. 네이버 던전")
                dungeon_select = int(input("던전을 선택해 주세요: "))
                if dungeon_select not in [1, 2, 3, 4]:
                    print("다시 선택해주세요")
                    continue #뒤로가기가 elif로 가야된다.
                elif dungeon_select == 1:
                    dungeon_03(seventh_dungeon, mons8, mons9, mons10)
                elif dungeon_select == 2:
                    dungeon_03(eighth_dungeon, mons9, mons10, mons11)
                elif dungeon_select == 3:
                    dungeon_03(ninth_dungeon, mons10, mons11, mons12)
                elif dungeon_select == 4:
                    dungeon_03(tenth_dungeon, mons13, mons14, mons15)
    
    
   # dungeon_03(first_dungeon, mons1, mons2, mons3)

