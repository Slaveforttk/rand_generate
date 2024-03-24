# _*_ coding : utf-8 _*_
# @Time : 2024/3/21 18:56
# @Author : Slave
# @File : first_program
# @Project : homeworkTest.py

# 初步功能需求：项目要求完成一个简单的四则运算功能
# -- 拟使用random来进行随机数生成以及对运算方式的选择
import random


# 这是生成运算表达式的函数
def generate_exercises(num_exercises, value_range):
    exercises = []

    for _ in range(num_exercises):
        # 需求分析知道操作符可能有一个，两个，三个
        num_operators = random.choice([1, 2])

        # 随机选择操作数和操作符 -- 操作数比操作符多一个
        nums = [random.randint(1, value_range) for _ in range(num_operators + 1)]
        operators = random.choices(['+', '-', '×', '÷'], k=num_operators)

        # 构造表达式
        exercise = ''.join(f"{num} {op}" for num, op in zip(nums, operators)) + f"{nums[-1]}"
        exercises.append(exercise)

    return exercises


exercises = generate_exercises(num_exercises=10, value_range=100)
for i, exercise in enumerate(exercises, 1):
    print(f"题目{i}: {exercise}")
