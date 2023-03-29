import random


# 클래스 명은 무조건 앞글자 대문자, 띄어쓰기 할때도 대문자로 구분 (카멜케이스)
# 함수 및 변수의 경우 소문자로 구성 띄어쓰기 는 언더바(_)를 이용(snake표기법)


# 슈퍼클래스

# Id
# 직업 : 프론트, 백 + 풀스택
# Hp
# Mp
# Max hp
# Max mp
# 스탯 1 html
# 스탯 2 Javascript
# 스탯 3 Python


class Player:
    def __init__(self, id, hp, mp, level, exp, html, javascript, python):
        self.id = id
        self.hp = hp
        self.max_hp = hp
        self.mp = mp
        self.max_mp = mp
        self.level = level
        self.exp = exp
        self.html = html  # 스탯 1. 기본공격
        self.javascript = javascript  # 스탯 2.마법공격 - front
        self.python = python  # 스탯 3. 마법공격 - back
        print(f"\n{self.id}이(가) 생성 되었습니다.")
        print(f"""
            LV : {self.level}
            HP: {self.hp}|{self.max_hp}
            MP: {self.mp}|{self.max_mp}
            EXP : {self.exp}
            Html: {self.html}|Javascript: {self.javascript}|Python:{self.python}
            """)

    def show_status(self):
        print(f"""
            <<{self.id}의 상태>>
            HP {self.hp}/{self.max_hp}
            MP{self.mp}/{self.max_mp}
            """)
        # 이걸 여기 놓고 같이 쓰면 어떨까요??? 위에 프린트는 지우구요요 흠!
        # print(f"""
        #     LV : {self.level}
        #     HP: {self.hp}|{self.max_hp}
        #     MP: {self.mp}|{self.max_mp}
        #     EXP : {self.exp}
        #     Html: {self.html}|Javascript: {self.javascript}|Python:{self.python}
        #     """)

    # 레벨업 함수
    def gain_exp(self, amount):
        self.exp += amount
        if self.exp >= self.level * 10:  # 10레벨까지.
            self.level_up()

    def level_up(self):
        self.level += 1
        self.max_hp += 10
        self.max_mp += 5
        self.html += 5
        self.javascript += 5
        self.python += 5
        self.hp = self.max_hp
        self.mp = self.max_mp
        print(f"{self.id}이(가) 레벨업 했습니다. LV : {self.level}")


# 직업 1 : 프론트엔드


class Frontend(Player):
    def __init__(self, frontend):
        # super(Frontend, self).__init__()
        self.frontend = frontend

     # 프론트엔드 일반 공격

    def attack(self, target):
        damage = random.randint(self.html * 0.9, self.html * 1.3)
        target.hp = max(target.hp - damage, 0)
        print(f"{self.id}의 웹표준 공격! {target.id}에게 {damage}의 데미지를 입혔습니다.")
        if target.hp == 0:
            print(f"{target.id}이(가) 쓰러졌습니다.")

     # 프론트엔드 마법 공격

    def magic_attack(self, target):
        self.mp = max(self.mp - 50, 0)
        if self.mp == 0:
            print("마나가 부족합니다.")
            return

        damage = random.randint(self.javascript * 0.8, self.javascript * 1.2)
        target.hp = max(target.hp - damage, 0)
        print(f"{self.id}의 리액트 공격! {target.id}에게 {damage}의 마법데미지를 입혔습니다.")
        if target.hp == 0:
            print(f"{target.id}이(가) 쓰러졌습니다.")


# 직업 2 : 백엔드


class Backend(Player):
    def __init__(self, backend):
        # super(Backend, self).__init__()
        self.backend = backend

    # 백엔드 일반 공격

    def attack(self, target):
        damage = random.randint(self.html * 0.7, self.html * 1.2)
        target.hp = max(target.hp - damage, 0)
        print(f"{self.id}의 공격! {target.id}에게 {damage}의 데미지를 입혔습니다.")
        if target.hp == 0:
            print(f"{target.id}이(가) 쓰러졌습니다.")

    # 백엔드 마법 공격

    def magic_attack(self, target):
        self.mp = max(self.mp - 50, 0)
        if self.mp == 0:
            print("마나가 부족합니다.")
            return

        damage = random.randint(self.javascript * 1.1, self.javascript * 1.3)
        target.hp = max(target.hp - damage, 0)
        print(f"{self.id}의 장고 공격! {target.id}에게 {damage}의 마법데미지를 입혔습니다.")
        if target.hp == 0:
            print(f"{target.id}이(가) 쓰러졌습니다.")

# 직업 3 : 풀스택 (히든)


class Fullstack(Player):
    def __init__(self, fullstack):
        # super(Fullstack, self).__init__()
        self.fullstack = fullstack

    # 풀스택 일반 공격

    def attack(self, target):
        damage = random.randint(self.html * 0.5, self.html * 1.5)
        target.hp = max(target.hp - damage, 0)
        print(f"{self.id}의 공격! {target.id}에게 {damage}의 데미지를 입혔습니다.")
        if target.hp == 0:
            print(f"{target.id}이(가) 쓰러졌습니다.")

    # 풀스택 마법 공격

    def magic_attack(self, target):
        self.mp = max(self.mp - 50, 0)
        if self.mp == 0:
            print("마나가 부족합니다.")
            return

        damage = random.randint(
            self.javascript + self.python * 0.75, self.javascript + self.python)
        target.hp = max(target.hp - damage, 0)
        print(f"{self.id}의 장고 공격! {target.id}에게 {damage}의 마법데미지를 입혔습니다.")
        if target.hp == 0:
            print(f"{target.id}이(가) 쓰러졌습니다.")


# front = Frontend(Player)()

# # 둔기 객체


# class Dungi(Player):
#     def __init__(self, id, power, hp, mp, cute, magic_power,):
#         super().__init__(id, power, hp, mp, cute, magic_power, weapon)
#         self.weapon = weapon

#     def get_weapon(self):
#     print("===== 둔기를 선택했습니다. =====")
#     return "{}로 선택했습니다.".format(self.weapon)

# # 칼 객체


# class Knife(Player):
#     def __init__(self, id, power, hp, mp, cute, magic_power):
#         super().__init__(id, power, hp, mp, cute, magic_power, weapon)
#         self.weapon = weapon

#     def get_weapon(self):
#         print("===== 칼을 선택했습니다. =====")
#         return "{}로 선택했습니다.".format(self.weapon)

# # 마법봉 객체


# class Magicbong(Player):
#     def __init__(self, id, power, hp, mp, cute, magic_power,):
#         super().__init__(id, power, hp, mp, cute, magic_power, weapon)
#         self.weapon = weapon

#     def get_weapon(self):
#         print("===== 마법봉을 선택했습니다. =====")
#         return "{}로 선택했습니다.".format(self.weapon)

class Monster():
    def __init__(self, id, power, hp, max_hp, exp):
        self.id = id
        self.power = power
        self.hp = hp
        self.max_hp = max_hp
        self.exp = exp

    def attack(self, target):  # 몬스터 데미지 80%~ 120% 변경
        damage = random.randint(self.power * 0.8, self.power * 1.2)
        target.hp = max(target.hp - damage, 0)
        print(f"{self.id}의 공격! {target.id}에게 {damage}의 데미지를 입혔습니다.")
        if target.hp == 0:
            print(f"{target.id}이(가) 쓰러졌습니다.")
            return 0
        return target.hp

    def cure(self, max_hp):  # 체력 리밋 설정함 (버그 생길수도..)
        self.hp += 10
        print(f'{self.id}가 자신의 체력을 10만큼 회복했습니다. 현재 체력 : {self.hp}')
        if self.hp > max_hp:
            self.hp = max_hp
        return self.hp

    def wait(self):
        print(f'{self.id}가 대기했습니다.')

    def status(self):
        print(f"\n{self.id} HP: {self.hp} / {self.max_hp}")

    def get_exp(monster):   # 몬스터를 잡으면 경험치를 반환.
        exp_gain = monster.exp
        return exp_gain

    def get_equipment():
        equipment_names = ["Red_portion", "Blue_portion",
                           "Mac_book", "Keyboard", "Mouse"]
        equipment_name = random.choice(equipment_names)


# 마을이 3개 마을마다 던전이 3개
# 마을 클래스 하나 던전 클래스 하나 를 나눠쓰면 되지 않을까?
# 타운과 던전이 몬스터 플레이어 상속받아야할 듯

class Town(Player, Monster):
    def __init__(self, town_name, dungeon_name):
        self.town_name = town_name
        self.dungeon_name = dungeon_name

    def show_status(self):

        print(f"""
            <<{self.id}의 상태>>
            HP {self.hp}/{self.max_hp}
            MP{self.mp}/{self.max_mp}
            """)

        # print(f"""
        #     LV : {self.level}
        #     HP: {self.hp}|{self.max_hp}
        #     MP: {self.mp}|{self.max_mp}
        #     EXP : {self.exp}
        #     Html: {self.html}|Javascript: {self.javascript}|Python:{self.python}
        #     """)


# 마을이 하는 역할
# 다른 마을로 가게 해준다. (레벨업 하면?)
# 다른 던전으로 가게 해준다. (던전과 플레이어를 이어준다.)
# 캐릭터가 죽으면 마을에서 살아난다.
# 마을 설명??? 마을 스토리???

# 던전이 하는 역할
# 던전과 마을은 이어저있다.
# 몬스터가 살고 있다.
# 캐릭터가 전투를 하는 곳이다.

# 순서
# 1. 플레이어 마을로 들어온다.
# 2. 00님 00마을에 입장하셨습니다.
# 3. 캐릭터 상태 출력
# -- 중간에 캐릭터 정비 할 수 있는 시간 만들지 ?
# 4. 어떤 던전으로 들어가시겠습니까? 1 2 3 고르기
# 5. 00님 00던전에 입장하셨습니다.
# 6. 앗! 거대한 몬스터가가 등장했따!
# 7. 선택지를 골라주세요 1.일반공격 2.마법공격 3.런 4.물약먹기
# 8. 일반공격 시전!/ 마법공격 시전 / 도망치셨습니다. / hp, mp가 -만큼 회복하였습니다.
# 9. 3번은 6번으로 돌아가고 나머지는 7-8번의 반복
# 10. 플레이어 또는 몬스터가 승리했다! 출력
# 11. 플레이어가 죽었다면 마을로 돌아간다.

# 밤8시 서경 : 플레이어 > 타운 > 던전 순으로 상속받게 작업할것임
class Dungeon():
    def __init__(self, name):
        self.name = name
        self.monsters = []

    def enter(self):
        print(f"{self.name}에 입장하셨습니다.")

    def append_monsters(self, *monsters):
        for monster in monsters:
            self.monsters.append(monster)


# # # 아이디 입력
# print("===== 이름을 입력해주세요. =====")
# ID = str(input("       "))


# # 무기 고르기
# print("===== 선택 할 무기를 골라주세요. ======")
# print("***** 1. 둔기  2. 칼  3. 마법봉 *****")
# number = int(input("→   "))
# if (number == 1):
#     weapon = "둔기"
#     dungi = Dungi(ID, sto, hp1, mp2, cut, str(weapon))
#     dungi.get_weapon()

# elif (number == 2):
#     weapon = '칼'
#     knife = Knife(ID, sto, hp1, mp2, cut, weapon)
#     knife.get_weapon()
# elif (number == 3):
#     weapon = '마법봉'
#     magicbong = Magicbong(ID, sto, hp1, mp2, cut, weapon)
#     magicbong.get_weapon()
# else:
#     print("===== 번호를 다시 선택해주세요. =====")

class Equipment():
    def __init__(self, name, hp, mp, html, javascript, python):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.html = html
        self.javascript = javascript
        self.python = python

#  포션은 혹시몰라서 두개 만들었습니다.


class Red_portion(Equipment):
    def __init__(self, name, hp):
        super().__init__(name, hp)

    def use_portion(self):
        self.hp += 100
        print(f"{self.name}을(를) 사용하여 체력이 100씩 회복되었습니다.")


class Blue_portion(Equipment):
    def __init__(self, name, mp):
        super().__init__(name, mp)

    def use_portion(self):
        self.mp += 100
        print(f"{self.name}을(를) 사용하여 마나가 100씩 회복되었습니다.")

# portion1 = Portion("체력 포션", 0, 0)   # 체력 포션 객체 생성
# portion1.use_potion()                # 포션 사용하여 체력과 마나 회복


class Mac_book(Equipment):
    def __init__(self, name, html, javascript, python):
        super().__init__(name, html, javascript, python)
        self.html += 15
        self.javascript += 5
        self.python += 5


class Keyboard(Equipment):
    def __init__(self, name, html, javascript, python):
        super().__init__(name, html, javascript, python)
        self.html += 5
        self.javascript += 15
        self.python += 5


class Mouse(Equipment):
    def __init__(self, name, html, javascript, python):
        super().__init__(name, html, javascript, python)
        self.html += 5
        self.javascript += 5
        self.python += 15
