# -*- coding: utf-8 -*-
# @Time     : 2020/10/23 17:28
# @Author   : chw
# @File     : game_fun.py

# 定义fight函数实现游戏逻辑
import random


def fight(enemy_hp, enemy_power):
    # 定义四个变量来存放数据
    my_hp = 1000
    my_power = 200
    # 打印敌人的血量和攻击力
    print(f"敌人的血量为{enemy_hp},攻击力为{enemy_power}")

    # 加入循环，让游戏可以进行多轮
    while True:
        my_hp = my_hp - enemy_power
        enemy_hp = enemy_hp - my_power

        #判断谁的血量小于等于0
        if my_hp <= 0:
            # 打印我和敌人的剩余血量
            print(f"我的剩余血量为{my_hp}")
            print(f"敌人的剩余血量为{enemy_hp}")
            print("我输了")
            #满足条件跳出循环
            break
        if enemy_hp <=0:
            print(f"我的剩余血量为{my_hp}")
            print(f"敌人的剩余血量为{enemy_hp}")
            print("我赢了")
            # 满足条件跳出循环
            break

if __name__ == "__main__":
    # 利用列表推导式生成hp
    hp = [x for x in range(990,1010)]
    # 让敌人的hp从hp列表中随机挑选一个值
    enemy_hp = random.choice(hp)
    # enemy_hp = random.randint(990,1010)
    print(enemy_hp)
    # 敌人的攻击力用randint方法生成随机的整数
    enemy_power = random.randint(190,210)
    # enemy_hp与enemy_power的两种生成方式其实是一样的结果
    print(enemy_power)

    # 调用函数，传入敌人的hp和power
    fight(enemy_hp,enemy_power)
