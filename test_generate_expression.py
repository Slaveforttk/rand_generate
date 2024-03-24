import unittest
from first_program import generate_exercises

class TestGenerateExercises(unittest.TestCase):
    def test_generate_exercises(self):
        # 测试生成10道题目，数值范围在1到100之间
        exercises = generate_exercises(num_exercises=10, value_range=100)
        self.assertEqual(len(exercises), 10)  # 确保生成了10道题目

        # 检查题目是否符合要求
        for exercise in exercises:
            self.assertTrue(isinstance(exercise, str))  # 题目应该是字符串类型
            self.assertTrue(exercise.count('+') <= 3)  # 运算符个数不超过3个
            self.assertTrue(exercise.count('-') <= 3)
            self.assertTrue(exercise.count('×') <= 3)
            self.assertTrue(exercise.count('÷') <= 3)

if __name__ == '__main__':
    unittest.main()
