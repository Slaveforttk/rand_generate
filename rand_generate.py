import random
import re
from fractions import Fraction


def format_exercise(exercise):
    # 使用正则表达式替换只作为运算符的除号
    exercise = re.sub(r'(?<= )/(?= )', '÷', exercise)
    # 将假分数的形式转换回 a'b/c
    exercise = re.sub(r"\((\d+) \+ (\d+/\d+)\)", r"\1’\2", exercise)
    return exercise


# 生成随机数（整数或真分数）的函数
def generate_number(min_num, max_num):
    rand_num = random.random()
    if rand_num < 0.5:  # 生成整数的概率为50%
        return str(random.randint(min_num, max_num))
    else:  # 生成分数的概率为50%
        numerator = random.randint(min_num, max_num)
        denominator = random.randint(min_num, max_num)
        fraction = Fraction(numerator, denominator)
        # 如果是假分数，转换为 (a + b/c) 的形式
        if numerator > denominator:
            whole_part = numerator // denominator
            numerator = numerator % denominator
            if numerator == 0:  # 如果分子为0，只返回整数部分
                return str(whole_part)
            else:
                return f"({whole_part} + {Fraction(numerator, denominator)})"
        else:
            return str(fraction)


# 生成四则运算表达式的函数
def generate_exercises(num_exercises, min_num, max_num):
    exercises = []
    ops = ['+', '-', '*', '/']

    for _ in range(num_exercises):
        num1 = generate_number(min_num, max_num)
        num2 = generate_number(min_num, max_num)
        op = random.choice(ops)
        # 对于减法和除法，确保结果是非负数
        if op == '-' and eval(num1) < eval(num2):
            num1, num2 = num2, num1
        elif op == '/' and eval(num1) < eval(num2):
            num1, num2 = num2, num1
        # 对除法运算的右操作数添加括号
        exercise = f"{num1} {op} {num2}" if op != '/' or "/" not in num2 else f"{num1} {op} ({num2})"
        exercises.append(exercise)

    return exercises


# 将题目和答案写入文件的函数
def write_to_files(exercises):
    with open('exercise.txt', 'w') as exer_file, open('answer.txt', 'w') as ans_file:
        for i, exercise in enumerate(exercises, 1):
            answer = eval(exercise.replace('÷', '/'))  # 在计算之前，将÷替换回/
            # 如果答案是一个假分数，将其转换为假分数的格式
            if answer % 1 != 0:
                answer = Fraction(answer).limit_denominator()
            else:
                answer = int(answer)
            if isinstance(answer, Fraction) and answer.numerator > answer.denominator:
                whole_part = answer.numerator // answer.denominator
                numerator = answer.numerator % answer.denominator
                answer = f"{whole_part}’{Fraction(numerator, answer.denominator)}"
            # 使用正则表达式替换只作为运算符的除号
            exercise = re.sub(r'(?<= )/(?= )', '÷', exercise)
            # 将假分数的形式转换回 a'b/c
            exercise = re.sub(r"\((\d+) \+ (\d+/\d+)\)", r"\1’\2", exercise)
            exer_file.write(f"{i}. {exercise} = \n")
            ans_file.write(f"{i}. {answer}\n")
