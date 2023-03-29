import random

# hi
# 방현재 - 몬스터 클래스
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

# 직업 1 : 프론트엔드


class Frontend(Player):
    # def __init__(self, frontend):
    #     super(Frontend, self).__init__()
    #     self.frontend = frontend

    def __init__(self, id, hp, max_hp, mp, max_mp, html, javascript, python, forntend):
        self.forntend = forntend
        super().__init__(id, hp, max_hp, mp, max_mp, html, javascript, python)

        print(f"{self.forntend} 직업을 가지게 되었습니다.")

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
        super(Backend, self).__init__()
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
        super(Fullstack, self).__init__()
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


# front = Frontend(Player, (input("플레이어의 이름을 입력하세요.")),
#                  100, 100, 1, 100, 10, 10, 10)

# print(front)

front = Frontend(input("이름을 입력해라"), 10, 500, 50, 50, 1, 2, 1, "frontend")
