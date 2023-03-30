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

# init함수에 yes or no 기능을 만들어서 마음에 드는 스탯이 나올때까지 스탯을 굴리게 만들었습니다.
class Player:   # init함수가 받는 인자를 이름만 받도록 변경, 스텟은 전부 랜덤에, 경험치와 레벨은 고정이라 저렇게 했습니다.
    def __init__(self, id):
        self.id = id
        self.hp = random.randint(50, 150)
        self.max_hp = self.hp
        self.mp = random.randint(50, 150)
        self.max_mp = self.mp
        self.level = 1
        self.exp = 0 
        self.html = random.randint(5, 15)  # 스탯 1. 기본공격
        self.javascript = random.randint(5, 15)  # 스탯 2.마법공격 - front
        self.python = random.randint(5, 15)  # 스탯 3. 마법공격 - back
        print(f"\n{self.id}이(가) 생성 되었습니다.")
        print(f"""
            LV : {self.level}
            HP: {self.hp} | {self.max_hp}
            MP: {self.mp} | {self.max_mp}
            EXP : {self.exp}
            Html:{self.html} | Javascript:{self.javascript} | Python:{self.python}
            """)
        

    def show_status(self):
        print(f"""
            <<{self.id}의 상태>>
            HP {self.hp}/{self.max_hp}
            MP{self.mp}/{self.max_mp}
            """)
        # 이걸 여기 놓고 같이 쓰면 어떨까요??? 위에 프린트는 지우구요요 흠!
        # 같이 쓰는 거 굉장히 좋다고 생각합니다. 만약 스탯 다시 굴리는 기능이 없다면 지워도 괜찮을것 같습니다.
        # 스탯 다시 굴리는 기능을 쓴다면 양쪽에 다 있어야 할 것 같습니다.
        # 아니면 여기서 말고 레벨업 할때만 레벨 경험치 능력치를 보여주는건 어떨까요?
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
    def __init__(self, id, hp, mp, html, javascript, python):
        # super(Frontend, self).__init__()
        self.id = id
        self.hp = hp
        self.max_hp = self.hp
        self.mp = mp
        self.max_mp = self.mp
        self.level = 1
        self.exp = 0 
        self.html = html
        self.javascript = javascript 
        self.python = python

     # 프론트엔드 일반 공격

    def attack(self, target):
        damage = random.randint(int(self.html * 0.8), int(self.html * 1.3))
        target.hp = max(target.hp - damage, 0)
        print(f"{self.id}의 웹표준 공격! {target.id}에게 {damage}의 데미지를 입혔습니다.")
        if target.hp == 0:
            print(f"{target.id}이(가) 쓰러졌습니다.")
            self.drop_item()  # 몬스터가 죽으면  드랍
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
            self.drop_item()  # 몬스터가 죽으면  드랍

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
            self.drop_item()  # 몬스터가 죽으면  드랍
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
            self.drop_item()  # 몬스터가 죽으면  드랍
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
            self.drop_item()  # 몬스터가 죽으면  드랍
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
            self.drop_item()  # 몬스터가 죽으면  드랍

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
    def __init__(self, id, hp, power, exp):
        self.id = id
        self.hp = hp
        self.max_hp = self.hp
        self.power = power
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

    def drop_item(self):  # 몬스터가 죽으면 드랍 아이템 , 확률
        items = ['RedPortion', 'BluePortion', 'MacBook',
                 'Keyboard', 'Mouse', 'ChatGpt']  # 드랍 아이템 종류
        probabilities = [0.2, 0.2, 0.15, 0.15, 0.15, 0.15]  # 드랍 확률

        for i in range(len(items)):
            if random.random() < probabilities[i]:
                print(f"{self.id}이(가) {items[i]}을(를) 떨어뜨렸습니다.")
                return items[i]
        return None

    # 몬스터를 죽이면 랜덤으로 무기 나오게 하기 (확률)

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

### 던전 클래스 만들어놨는데 불완전합니다~~
class Dungeon():
    def __init__(self, name):
        self.name = name
        self.monsters = []

    def enter(self):
        print(f"{self.name}에 입장하셨습니다.")

    def append_monsters(self, *monster):
        mon_list = [monster]
        for m in mon_list:
            self.monsters.append(m)

    def get_monsters(self):
        return self.monsters
    
    def remove_monster(self, monster):
        self.monsters.remove(monster)
#####

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

class Equipment():  # 장비 부모 객체
    def __init__(self, name, hp, mp, html, javascript, python):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.html = html
        self.javascript = javascript
        self.python = python


class RedPortion(Equipment):  # 체력 포션
    def __init__(self, name, hp):
        super().__init__(name, hp)

    def use_portion(self):
        self.hp += 100  # 체력 100만큼 증가
        print(f"{self.name}을(를) 사용하여 체력이 100씩 회복되었습니다.")


class BluePortion(Equipment):  # 마나 포션
    def __init__(self, name, mp):
        super().__init__(name, mp)

    def use_portion(self):
        self.mp += 100
        print(f"{self.name}을(를) 사용하여 마나가 100씩 회복되었습니다.")

# portion1 = Portion("체력 포션", 0, 0)   # 체력 포션 객체 생성
# portion1.use_potion()                # 포션 사용하여 체력과 마나 회복


class MacBook(Equipment):  # 맥북 무기
    def __init__(self, name, html, javascript, python):
        super().__init__(name, html, javascript, python)
        self.html += 15
        self.javascript += 5  # 무기 스탯
        self.python += 5


class Keyboard(Equipment):  # 키보드 무기
    def __init__(self, name, html, javascript, python):
        super().__init__(name, html, javascript, python)
        self.html += 5
        self.javascript += 15
        self.python += 5


class Mouse(Equipment):  # 마우스 무기
    def __init__(self, name, html, javascript, python):
        super().__init__(name, html, javascript, python)
        self.html += 5
        self.javascript += 5
        self.python += 15


class ChatGpt(Equipment):  # 쥐피티 무기
    def __init__(self, name, html, javascript, python):
        super().__init__(name, html, javascript, python)
        self.html += 20
        self.javascript += 20
        self.python += 20


# 인벤토리를 클래스로 만들어서 아이템을 추가하고 

# 무기 드랍 확률 만들어보기
# red_portion = RedPortion() 30%
# blue_portion = BluePortion() 25%
# mac_book = MacBook() 10%
# keyboard = Keyboard() 10%
# mouse = Mouse() 10% 
# chat_gpt = ChatGpt() 5%




# 서경이의 인벤토리

# class Inventory:
#     def __init__(self):
#         self.items = []

#     def add_item(self, item):
#         if item in self.items:
#             self.items[item] += 1
#         else:
#             self.items[item] = 1

#         # 만약 아이템이 없다면 아이템을
#         # 만약 아이템의 갯수가 하나 증가하면 value 의 숫자를 +1씩 증가시킨다.
#         # 아이템값이 key 이름 :value 갯수 로 들어가야 할 듯

#     def remove_item(self, item):
#         if self.items[item] > 1:
#             self.items[item] -= 1
#         else:
#             self.items.remove(item)
#         # 아이템을 사용한다면 value의 숫자를 -1씩 감소시킨다
#         # 아이템의 벨류 == 0 아이템을 지운다.

#     def view_items(self):
#         for item in self.items:
#             print(f'{item.name}: {item.quantity}')


# inventory = Inventory()

# redportion = RedPortion("레드포션", 50)
# blueportion = BluePortion("블루포션", 50)
# macbook = MacBook()
# mouse = Mouse()
# keyboard = Keyboard()
# chatgpt = ChatGpt()


# # print(f"{}의 인벤토리를 확인합니다.")
# inventory.view_items()


# inventory.add_item(redportion)
# inventory.view_items()
