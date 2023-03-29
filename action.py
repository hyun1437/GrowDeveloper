import random
import main

# 플레이어의 행동 함수


def player_action():
    while True:  # while문을 사용해 break를 걸 때 까지 계속 실행
        try:
            print('< 공격 스킬 선택 phase >')
            print('1. 물리 공격')
            print('2. 마법 공격')
            p1_skill_input = int(input('사용할 스킬의 번호를 입력하세요. : '))
            if p1_skill_input == 0 or p1_skill_input > 2:   # 1,2 외에 다른 숫자가 들어오면 다시 입력
                print("공격 스킬을 다시 입력해주세요")
                continue     # while문을 처음부터 다시 시작함

        except ValueError:  # ValueError가 나왔을때 execpt문 실행
            print("공격방식을 숫자로 입력해주세요")
            continue
        break   # while문을 빠져나옴

    print('< 대상 선택 phase >')
    # enumerate함수를 사용해 i는 순서를 m은 m1,m2와 같은 몬스터 변수를 입력
    for i, m in enumerate(monsters_list):
        print(f"{i+1}. {m.name} (HP: {m.hp} / {m.max_hp})")

    while True:
        try:
            p1_target_input = int(input('공격할 대상의 번호를 입력하세요. : '))
            if p1_target_input <= 0 or p1_target_input > len(monsters_list):
                print("잘못된 대상을 선택하셨습니다. 다시 선택해주세요.")
                continue
        except ValueError:  # ValueError가 나왔을때 execpt문 실행
            print("대상 번호를 숫자로 입력해주세요.")
            continue

        break

    if p1_skill_input == 1:  # 공격방식의 번호 입력이 1(노말어택)이라면
        # game_class 파일 Player 클래스의 nomal_attack함수 실행
        main.Player.nomal_attack(p1, monsters_list[p1_target_input - 1])
    elif p1_skill_input == 2:  # 공격방식의 번호 입력이 2(매직어택)이라면
        main.Player.magic_attack(p1, monsters_list[p1_target_input - 1])

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


def monster_action():
    # 살아있는 몬스터들만 행동
    action_num = random.randint(1, 3)
    for monster in monsters_list:
        if action_num == 1:
            monster.main.Monster.cure()
        elif action_num == 2:
            monster.main.Monster.wait()
        elif action_num == 3:
            p1.hp = m.attack(p1)


# 몬스터 리스트 제거 함수
def monster_death():
    for monster in monsters_list:   # for문으로 몬스터리스트 monster변수에 순차적 할당
        if monster.hp <= 0:  # 만약 monster의 hp가 0보다 작거나 같다면
            monsters_list.remove(monster)   # 몬스터리스트에서 monster제거


def dungeon_01(name):
    main.Dungeon(name)
    main.Dungeon.enter(name)
    main.Dungeon.append_monsters(name, m1, m2, m3)


# 게임 실행 부분
p1 = main.Player(input("이름을 입력해주세요."), 20, 100, 100, 10, 10, 100, 30)
m1 = main.Monster('돼지1', 10, 10, 10)
m2 = main.Monster('돼지2', 20, 20, 20)
m3 = main.Monster('돼지3', 30, 30, 30)


monsters_list = [m1, m2, m3]

# 몬스터 리스트에서 뽑아오는 방식으로 가는거였나요??? 아리송

# monsters_list = [mons1, mons2, mons3, mons4, mons5, mons6, mons7, mons8, mons9, mons10]

# pliot = main.Player(input("이름을 입력해주세요."), 20, 100, 100, 10, 10, 100, 30)
# mons1 = main.Monster('초급예제', 10, 10, 10)
# mons2 = main.Monster('중급예제', 20, 20, 20)
# mons3 = main.Monster('고급예제', 30, 30, 30)
# mons4 = main.Monster('심화예제', 30, 30, 30)
# mons5 = main.Monster('백준(브론즈)', 30, 30, 30)
# mons6 = main.Monster('백준(실버)', 30, 30, 30)
# mons7 = main.Monster('백준(골드)', 30, 30, 30)
# mons8 = main.Monster('백준(플레)', 30, 30, 30)
# mons9 = main.Monster('카카오(코테)', 30, 30, 30)
# mons10 = main.Monster('삼성(코테)', 30, 30, 30)


turn = 0

while True:
    # 던전 진입 전 메시지
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

    print('===== 던전 선택 =====')

    # 턴 시작전 총 상태표시
    print('===== 턴 시작전 총 상태표시 =====')
    p1.show_status()  # 플레이어
    for m in monsters_list:  # 몬스터들
        m.status()

    # 플레이어 턴
    if turn % 2 == 0:
        print('===== 플레이어 턴 =====')

        # 플레이어 액션
        player_action()

        # 몬스터 사망 여부 체크
        monster_death()

        # 몬스터 리스트에 몬스터가 없을 경우
        if len(monsters_list) <= 0:
            print('모든 몬스터를 물리쳤습니다!')
            print('===== Win! =====')
            break

    # 몬스터 턴
    else:
        print('===== 몬스터 턴 =====')

        # 몬스터 액션
        monster_action()

        # 공격 종료 후 플레이어 상태 체크
        if p1.hp <= 0:
            print('플레이어 사망!')
            print('== Game Over ==')
            break

    turn += 1
    print('-------------------')
    print('----- 턴 종료 -----')
    print('-------------------')
