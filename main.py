import random


### 플레이어 클래스

# init함수에 yes or no 기능을 만들어서 마음에 드는 스탯이 나올때까지 스탯을 굴리게 만들었습니다.
class Player():   # init함수가 받는 인자를 이름만 받도록 변경, 스텟은 전부 랜덤에, 경험치와 레벨은 고정이라 저렇게 했습니다.
    def __init__(self, id):
        self.id = id
        self.hp = random.randint(100, 200)
        self.max_hp = self.hp
        self.mp = random.randint(100, 150)
        self.max_mp = self.mp
        self.level = 1
        self.exp = 0
        self.max_exp = 50
        self.html = random.randint(20, 30)  # 스탯 1. 기본공격
        self.javascript = random.randint(20, 30)  # 스탯 2.마법공격 - front
        self.python = random.randint(20, 30)  # 스탯 3. 마법공격 - back
        print(f"\n{self.id}이(가) 생성 되었습니다.")
        print(f"""
            LV: {self.level}
            HP: {self.hp}/{self.max_hp}
            MP: {self.mp}/{self.max_mp}
            EXP: {self.exp}/{self.max_exp}
            Html: {self.html}/Javascript: {self.javascript}/Python: {self.python}
            """)
        
    def show_status(self):
        print(f"""
            <<{self.id}의 상태>>
            LV: {self.level}
            HP: {self.hp}/{self.max_hp}
            MP: {self.mp}/{self.max_mp}
            EXP: {self.exp}/{self.max_exp}
            Html: {self.html}/Javascript: {self.javascript}/Python: {self.python}
            """)

    # 레벨업 함수
    def gain_exp(self, mon_exp):
        self.exp += mon_exp
        if self.exp >= self.max_exp:  # 10레벨까지.
            while self.exp >= self.max_exp:
                next_exp =  self.exp - self.max_exp
                self.level_up(next_exp)


    def level_up(self, current_exp):
        self.level += 1
        self.max_hp += 10
        self.max_mp += 5
        self.html += 5
        self.javascript += 5
        self.python += 5
        self.hp = self.max_hp
        self.mp = self.max_mp
        self.exp = current_exp
        self.max_exp += 20
        print(f"{self.id}이(가) 레벨업 했습니다. LV : {self.level}")
 
    def use_item(self, item_name):
        self.hp += item_name.hp
        self.mp += item_name.mp
        self.html += item_name.html
        self.javascript += item_name.javascript
        self.python += item_name.python

### 여기까지 플레이어 클래스

### 직업 1 : 프론트엔드

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
        self.max_exp = 50
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
            target.drop_item(self)  # 몬스터가 죽으면 드랍


     # 프론트엔드 마법 공격

    def magic_attack(self, target):
        self.mp = max(self.mp - 50, 0)
        if self.mp == 0:
            print("마나가 부족합니다.")
            return

        damage = random.randint(int(self.javascript * 0.8), int(self.javascript * 1.2))
        target.hp = max(target.hp - damage, 0)
        print(f"{self.id}의 리액트 공격! {target.id}에게 {damage}의 마법데미지를 입혔습니다.")
        if target.hp == 0:
            print(f"{target.id}이(가) 쓰러졌습니다.")
            target.drop_item(self)  # 몬스터가 죽으면 드랍


### 직업 2 : 백엔드

class Backend(Player):
    def __init__(self, id, hp, mp, html, javascript, python):
        # super(Backend, self).__init__()
        self.id = id
        self.hp = hp
        self.max_hp = self.hp
        self.mp = mp
        self.max_mp = self.mp
        self.level = 1
        self.exp = 0 
        self.max_exp = 50
        self.html = html
        self.javascript = javascript 
        self.python = python


    # 백엔드 일반 공격

    def attack(self, target):
        damage = random.randint(int(self.html * 0.8), int(self.html * 1.3))
        target.hp = max(target.hp - damage, 0)
        print(f"{self.id}의 공격! {target.id}에게 {damage}의 데미지를 입혔습니다.")
        if target.hp == 0:
            print(f"{target.id}이(가) 쓰러졌습니다.")
            target.drop_item(self)  # 몬스터가 죽으면 드랍
    
    
    # 백엔드 마법 공격

    def magic_attack(self, target):
        self.mp = max(self.mp - 50, 0)
        if self.mp == 0:
            print("마나가 부족합니다.")
            return

        damage = random.randint(int(self.javascript * 0.8), int(self.javascript * 1.2))
        target.hp = max(target.hp - damage, 0)
        print(f"{self.id}의 장고 공격! {target.id}에게 {damage}의 마법데미지를 입혔습니다.")
        if target.hp == 0:
            print(f"{target.id}이(가) 쓰러졌습니다.")
            target.drop_item(self)  # 몬스터가 죽으면  드랍


### 직업 3 : 풀스택 (히든)

class Fullstack(Player):
    def __init__(self, id, hp, mp, html, javascript, python):
        # super(Fullstack, self).__init__()
        self.id = id
        self.hp = hp
        self.max_hp = self.hp
        self.mp = mp
        self.max_mp = self.mp
        self.level = 1
        self.exp = 0 
        self.max_exp = 50
        self.html = html
        self.javascript = javascript 
        self.python = python


    # 풀스택 일반 공격

    def attack(self, target):
        damage = random.randint(int(self.html * 1.5), int(self.html * 2))
        target.hp = max(target.hp - damage, 0)
        print(f"{self.id}의 공격! {target.id}에게 {damage}의 데미지를 입혔습니다.")
        if target.hp == 0:
            print(f"{target.id}이(가) 쓰러졌습니다.")
            target.drop_item(self)  # 몬스터가 죽으면  드랍
    

    # 풀스택 마법 공격

    def magic_attack(self, target):
        self.mp = max(self.mp - 50, 0)
        if self.mp == 0:
            print("마나가 부족합니다.")
            return
        # self.javascript + self.python * 0.75, self.javascript + self.python)
        damage = random.randint(int(self.javascript + self.python * 0.75), int(self.javascript + self.python))
        target.hp = max(target.hp - damage, 0)
        print(f"{self.id}의 장고 공격! {target.id}에게 {damage}의 마법데미지를 입혔습니다.")
        if target.hp == 0:
            print(f"{target.id}이(가) 쓰러졌습니다.")
            target.drop_item(self)  # 몬스터가 죽으면  드랍


### 몬스터 클래스

class Monster():
    def __init__(self, id, hp, power, exp):
        self.id = id
        self.hp = hp
        self.max_hp = self.hp
        self.power = power
        self.exp = exp

    def attack(self, target):  # 몬스터 데미지 80%~ 120% 변경
        damage = random.randint(int(self.power * 0.8), int(self.power * 1.2))
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

    def get_exp(self):   # 몬스터를 잡으면 경험치를 반환.
        exp_gain = self.exp
        return exp_gain

    def drop_item(self, player):  # 몬스터가 죽으면 드랍 아이템 , 확률
        items = [redportion, blueportion, hongongpa, mouse, keyboard, macbook, chatgpt]  # 드랍 아이템 종류
        probabilities = [0.3, 0.3, 0.2, 0.09, 0.05, 0.05, 0.01] # 드랍 확률
                           
        # 확인 부탁드립니다.
        for i in range(len(items)):
            if random.random() < probabilities[i]:
                item = items[i]
                if item in [redportion, blueportion]:
                    print(f"{player.id}이(가) {item.name}을(를) 획득하였습니다.")
                    player.use_item(item)
                    print(f"{player.id}이(가) HP를 {item.hp}만큼 / MP를 {item.mp}만큼 회복시켰습니다.")
                else:
                    print(f"{player.id}이(가) {item.name}을(를) 획득하여. 장착했습니다")
                    player.use_item(item)
                    print(f"html: {item.html} / javascript: {item.javascript} / python: {item.python} 만큼 증가했습니다.")
 

### 여기까지 몬스터 클래스
    


### 던전 클래스 
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

class Equipment(): # 장비 부모 객체
    def __init__(self, name, hp, mp, html = 0, javascript = 0, python = 0):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.html = html
        self.javascript = javascript
        self.python = python


#포션
redportion = Equipment('빨간물약', 100, 0)
blueportion = Equipment('파란물약', 0, 100)

# 장비
hongongpa = Equipment('혼공파',0,0,3,3,3)
mouse = Equipment('마우스', 0,0,5,5,5)
keyboard = Equipment('키보드',0,0,5,1,10)
macbook = Equipment('맥북', 0,0,5,10,1)
chatgpt = Equipment('(전설)챗GPT',0,0,15,15,15)