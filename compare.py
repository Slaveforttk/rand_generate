from fractions import Fraction


def convert_mixed_fraction(fraction):
    # 将假分数的形式转换为普通分数的形式
    if "’" in fraction:
        whole, frac = fraction.split("’")
        num, denom = frac.split("/")
        return f"({whole} + {num}/{denom})"
    else:
        return fraction


def convert_mixed_fraction_in_expression(expression):
    # 将表达式中的每个操作数都转换为普通分数的形式
    parts = expression.split()
    for i, part in enumerate(parts):
        if "’" in part:
            parts[i] = convert_mixed_fraction(part)
    return " ".join(parts)


def compare_answers(exercise_file, answer_file, output_file):
    try:
        with open(exercise_file, 'r') as f_ex, open(answer_file, 'r') as f_ans:
            exercises = f_ex.readlines()
            answers = f_ans.readlines()
    except FileNotFoundError:
        return "FileNotFoundError"

    correct = []
    incorrect = []
    for i, (exercise, answer) in enumerate(zip(exercises, answers), 1):
        try:
            # 移除序号和等号，将题目转换为一个有效的表达式
            exercise = exercise.split('=')[0].split('. ')[1].strip().replace('÷', '/')
            # 将表达式中的每个操作数都转换为普通分数的形式
            exercise = convert_mixed_fraction_in_expression(exercise)
            # 计算题目的正确答案
            correct_answer = eval(exercise)
            # 如果答案是一个假分数，将其转换为假分数的格式
            if correct_answer % 1 != 0:
                correct_answer = Fraction(correct_answer).limit_denominator()
            else:
                correct_answer = str(int(correct_answer))
            if isinstance(correct_answer, Fraction) and correct_answer.numerator > correct_answer.denominator:
                whole_part = correct_answer.numerator // correct_answer.denominator
                numerator = correct_answer.numerator % correct_answer.denominator
                correct_answer = f"{whole_part}’{Fraction(numerator, correct_answer.denominator)}"
            elif isinstance(correct_answer, Fraction):
                correct_answer = f"{correct_answer}"
            # 对比答案
            if correct_answer != answer.split('. ')[1].strip():
                incorrect.append(i)
            else:
                correct.append(i)
        except Exception as e:
            return str(e)

    # 输出对比结果
    with open(output_file, 'w') as f_out:
        f_out.write(f"正确的题目有{len(correct)}道，分别是：{correct}\n")
        f_out.write(f"错误的题目有{len(incorrect)}道，分别是：{incorrect}\n")

    return "Success"
