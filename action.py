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


# 플레이어의 행동 함수


# def player_action():
#     while True:  # while문을 사용해 break를 걸 때 까지 계속 실행
#         try:
#             print('< 공격 스킬 선택 phase >')
#             print('1. 물리 공격')
#             print('2. 마법 공격')
#             p1_skill_input = int(input('사용할 스킬의 번호를 입력하세요. : '))
#             if p1_skill_input == 0 or p1_skill_input > 2:   # 1,2 외에 다른 숫자가 들어오면 다시 입력
#                 print("공격 스킬을 다시 입력해주세요")
#                 continue     # while문을 처음부터 다시 시작함

#         except ValueError:  # ValueError가 나왔을때 execpt문 실행
#             print("공격방식을 숫자로 입력해주세요")
#             continue
#         break   # while문을 빠져나옴

#     print('< 대상 선택 phase >')
#     # enumerate함수를 사용해 i는 순서를 m은 m1,m2와 같은 몬스터 변수를 입력
#     for i, m in enumerate(monsters_list):
#         print(f"{i+1}. {m.id} (HP: {m.hp} / {m.max_hp})")

#     while True:
#         try:
#             p1_target_input = int(input('공격할 대상의 번호를 입력하세요. : '))
#             if p1_target_input <= 0 or p1_target_input > len(monsters_list):
#                 print("잘못된 대상을 선택하셨습니다. 다시 선택해주세요.")
#                 continue
#         except ValueError:  # ValueError가 나왔을때 execpt문 실행
#             print("대상 번호를 숫자로 입력해주세요.")
#             continue

#         break

#     if p1_skill_input == 1:  # 공격방식의 번호 입력이 1(노말어택)이라면
#         # game_class 파일 Player 클래스의 nomal_attack함수 실행
#         p1.attack(monsters_list[p1_target_input - 1])
#     elif p1_skill_input == 2:  # 공격방식의 번호 입력이 2(매직어택)이라면
#         p1.magic_attack(monsters_list[p1_target_input - 1])

########## 던전 클래스 이용시 사용할 함수들
###### 기본 틀을 거의 같고 dungeon_03이라는 함수가 추가되었습니다.
###### 본래는 *monster를 파라미터로 받아 몇개가 들어오든 상관없게 짜서 하나의 던전 함수로 다 해결하려 했는데
###### *args스타일로 인자를 받으면 튜플로 변경 되는 것 같습니다.
###### dungeon뒤에 오는 숫자는 몬스터의 수를 의미합니다. 1마리, 2마리는 함수를 복사해 만들면 될 것으로 보입니다.
###### 전역변수로 미리 몬스터들 m1, m2, m3 같은거 만들어 놓고 사용하면 좋아 보입니다.
def player_action(list):
    mon_list = list 
    while True: # while문을 사용해 break를 걸 때 까지 계속 실행
        try:    
            print("\n===공격 방식 선택===\n1. 물리 공격\n2. 마법 공격")
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

# # 몬스터의 행동함수
# def monster_turn(monsters):
#     for monster in monsters:
#         monster.attack(p1)    # 반복문을 돌면서 한마리씩 플레이어 어택

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
def monster_death(monsters_list):  
    for m in monsters_list:
        if m.hp <= 0:
            monsters_list.remove(m)



def dungeon_03(dungeon, monster1, monster2, monster3):    
    dungeon.enter()

    dungeon.append_monsters(monster1, monster2, monster3)

    monsters_list = [monster1, monster2, monster3]

    turn = 1
    while True: # break가 걸릴 때 까지 반복 실행
        new_cmd()
        if p1.level <= 5:
            print('---------------------')
            print('---- 어쩌구 마을 ----')
            print('---------------------')
        elif 5 < p1.level <= 10:
            print('---------------------')
            print('---- 저쩌구 마을 ----')
            print('---------------------')
        else:
            print('---------------------')
            print('---- 엄청쎈 마을 ----')
            print('---------------------')
    
        print(f"\n====={turn}번째 턴====")  # f_string을 이용
        time.sleep(0.3) # 텍스트가 한번에 입력되는 것을 방지함, 좀 더 게임처럼 즐길 수 있음
        p1.show_status() # p1 = 플레이어, 플레이어의 상태를 보여주는 status함수를 사용
        for m in monsters_list:  # 몬스터 리스트에 있는 몬스터들을 m이라는 변수에 순차 저장
            m.status()
            time.sleep(0.3)

        print("\n===플레이어 턴===")
        player_action(monsters_list)   # 플레이어 행동함수 실행
        monster_death(monsters_list) # 몬스터 리스트 제거 함수 실행

        if monsters_list == []:  # 몬스터가 모두 죽어서 리스트가 비어버렸다면
            print("\n====clear!====\n당신이 승리했습니다.")
            break   # 반복문 종료
        
        print("\n===몬스터 턴===")
        time.sleep(0.3)
        monster_action(monsters_list)  # 몬스터 행동함수 실행

        if p1.hp <= 0:  # 플레이어의 체력이 0보다 같거나 작다면
            print("\n당신이 사망하였습니다.\n ====게임 오버====")
            break   # 반복문 종료

        turn += 1   # 턴 + 1
        print("\n====턴 종료====")    # 위의 break에 걸리지 않았다면 다시 반복문으로 돌아감
        time.sleep(0.3) 

# p1 = main.Player(input("당신의 이름은 무엇입니까?: "))    # Player 클래스 __init__에서 많은 숫자가 랜덤으로 부여시켜서 id만 받음
# m1 = main.Monster("주황버섯", 15, 4, 10)  # Monster 클래스 __init__에서 요구하는 (id, hp, power)
# m2 = main.Monster("초록버섯", 25, 5, 10)
# m3 = main.Monster("파랑버섯", 35, 6, 10)
# m4 = main.Monster("뿔버섯", 35, 6, 10)


#######


    # # 물리 공격시
    # if p1_skill_input == 1:
    #     # 공격 대상 돼지1
    #     if p1_target_input == 1:
    #         m1.hp = p1.attack(m1)
    #     # 공격 대상 돼지2
    #     elif p1_target_input == 2:
    #         m2.hp = p1.attack(m2)
    #     # 공격 대상 돼지3
    #     elif p1_target_input == 3:
    #         m3.hp = p1.attack(m3)
    # # 마법 공격시
    # elif p1_skill_input == 2:
    #     # 공격 대상 돼지1
    #     if p1_target_input == 1:
    #         m1.hp = p1.magic_attack(m1)
    #     # 공격 대상 돼지2

    #     elif p1_target_input == 2:
    #         m2.hp = p1.magic_attack(m2)
    #     # 공격 대상 돼지3
    #     elif p1_target_input == 3:
    #         m3.hp = p1.magic_attack(m3)


# def monster_action():
#     # 살아있는 몬스터들만 행동
#     action_num = random.randint(1, 3)
#     for monster in monsters_list:
#         if action_num == 1:
#             monster.main.Monster.cure()
#         elif action_num == 2:
#             monster.main.Monster.wait()
#         elif action_num == 3:
#             p1.hp = m.attack(p1)


# # 몬스터 리스트 제거 함수
# def monster_death():
#     for monster in monsters_list:   # for문으로 몬스터리스트 monster변수에 순차적 할당
#         if monster.hp <= 0:  # 만약 monster의 hp가 0보다 작거나 같다면
#             monsters_list.remove(monster)   # 몬스터리스트에서 monster제거


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
if p1.html > 10 and p1.javascript > 10 and p1.python > 10:
    print("3.풀스택(히든)")
while True:
    job_select = int(input("원하시는 직업을 선택해주세요"))
    if job_select == 1:
        p1 = main.Frontend(p1.id, p1.hp, p1.mp, p1.html, p1.javascript, p1.python)
        print("Frontend 직업을 가지게 되었습니다.")
        break
    elif job_select == 2:
        p1 = main.Backend(p1.id, p1.hp, p1.mp, p1.html, p1.javascript, p1.python)
        print("Backend 직업을 가지게 되었습니다.")
        break
    elif job_select == 3:
        if p1.html > 10 and p1.javascript > 10 and p1.python > 10:
            p1 = main.Fullstack(p1.id, p1.hp, p1.mp, p1.html, p1.javascript, p1.python)
            break
    else:
        print('올바른 직업번호를 입력해주세요')
        continue

first_dungeon = main.Dungeon("초보자 던전")


mons1 = main.Monster('초급예제', 10, 10, 10)
mons2 = main.Monster('중급예제', 20, 20, 20)
mons3 = main.Monster('고급예제', 30, 30, 30)
mons4 = main.Monster('심화예제', 30, 30, 30)
mons5 = main.Monster('백준(브론즈)', 30, 30, 30)
mons6 = main.Monster('백준(실버)', 30, 30, 30)
mons7 = main.Monster('백준(골드)', 30, 30, 30)
mons8 = main.Monster('백준(플레)', 30, 30, 30)
mons9 = main.Monster('카카오(코테)', 30, 30, 30)
mons10 = main.Monster('삼성(코테)', 30, 30, 30)


dungeon_03(first_dungeon, mons1, mons2, mons3)

