import random
import time

# 플레이어, 몬스터 클래스


def ment1(a):
    time.sleep(1)
    return a


def ment2(b):
    time.sleep(2)
    return b


def ment3(c):
    time.sleep(3)
    return c


class Character:

    def __init__(self, name, hp, mp, power, magic):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.power = power
        self.magic = magic

    # 플레이어 몬스터 일반공격
    def attack(self, other):
        damage = random.randint(self.power - 2, self.power + 2)
        other.hp = max(other.hp - damage, 0)
        ment1(
            print(f"{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다."))
        if other.hp == 0:
            ment1(print(f"{other.name}이 쓰러졌습니다."))

    # 플레이어의 마법공격
    def magic_attack(self, other):
        self.mp = max(self.mp - 50, 0)
        if self.mp == 0:
            ment1(print(f"{self.name}의 MP가 부족해 마법공격을 쓸 수 없습니다."))
            return

        damage = random.randint(self.magic - 20, self.magic + 20)
        other.hp = max(other.hp - damage, 0)
        ment2(print("""
                    
            ....::::::･‘’･::::...
                ::　　　　　　　　::
                :　　원　 기　 옥　　:
                ::　　　　　　　　 ::
            　　‘’'::::::･,,･::::::‘’'
                　  　∩∧_∧∩
                　　　(　･ω･)
                　　 　/　　ﾉ
                　　　しーU     
              
              """))
        print(f"{self.name}의 원기옥!!!! {other.name}에게 {damage}의 데미지를 입혔습니다.\n")
        if other.hp == 0:
            ment1(print(f"{other.name}이 쓰러졌습니다."))

    # 플레이어와 몬스터의 상태 출력
    def show_status(self, other):
        print(
            f"{self.name}의 상태: HP {self.hp}/{self.max_hp} | MP {self.mp}/{self.max_mp}\n")
        print(f"{other.name}의 상태: HP {other.hp}/{other.max_hp}")


# 인스턴스(객체) = 클래스
P = Character(ment1(input("플레이어의 이름을 입력하세요 : ")), 100, 200, 10, 10)
M = Character("세히몬", 100, 0, 10, 0)

# 게임 스타트!

ment1(print("여기는 평화로운 스파르타 내배캠 게더타운."))
ment2(print(
    """
° :.　 . • ○ ° ★　 .　 *　.
★ ° . .　　　　.　☾ °☆　 . * ● ¸ .
    ∩ │◥███◣ ╱◥███◣
    ╱◥◣ ◥████◣▓∩▓│∩ ║
    │╱◥█◣║∩∩∩ ║◥█▓ ▓█◣
    ││∩│ ▓ ║∩田│║▓ ▓ ▓∩ ║
            """))

ment2(print(
    """
            ° :.　 . • ○ ° ★　 .　 *　.
        ★ ° . .　　　　.　☾ °☆　 . * ● ¸ .
                    오늘도 코드 헤는 밤...
            """))


ment3(print(f"앗! 플레이어 {P.name}의 앞에 야생의 세히몬이 나타났다!"))

# 게임의 턴을 위한 while문
while P.hp or M.hp > 0:
    print("""
〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓
          """)
    print("<플레이어와 몬스터 상태창>\n")
    ment1(P.show_status(M))
    print("""
〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓
          """)
    ment1(
        print(f"플레이어 {P.name}의 들레소환술!\n\n1.일반공격, 2.마법공격(mp -50)\n번호를 선택하세요.\n"))
    choice = input()
    if choice == '1':
        P.attack(M)
    elif choice == '2':
        P.magic_attack(M)
        if P.mp == 0:
            continue
    else:
        ment1(print("잘못 입력하셨습니다."))
        continue

    if P.hp == 0:
        ment1(print(f"플레이어 {P.name}의 체력이 0 이 되었다.\n 세히몬의 승리!"))
        break
    elif M.hp == 0:
        ment1(print(f"세히몬의 체력이 0 이 되었다. 플레이어 {P.name}의 승리!"))
        break

    ment1(print(f"세히몬이 떽떽거리기!! 를 시전합니다.\n"))
    M.attack(P)

    if P.hp == 0:
        ment1(print(f"플레이어 {P.name}의 체력이 0 이 되었다.\n 세히몬의 승리!"))
        break
    elif M.hp == 0:
        ment1(print(f"세히몬의 체력이 0 이 되었다. 플레이어 {P.name}의 승리!"))
        break
