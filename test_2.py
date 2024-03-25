import unittest
import rand_generate


class TestFunctions(unittest.TestCase):
    def test_generate_number(self):
        for _ in range(100):
            num = rand_generate.generate_number(1, 10)
            # 检查生成的数字是否在指定范围内
            self.assertTrue(0 <= eval(num) <= 10)
            # 检查生成的数字是否为整数或分数
            if '.' not in num:
                self.assertTrue(num.isdigit() or '/' in num)

    def test_write_to_files(self):
        exercises = rand_generate.generate_exercises(10, 1, 10)
        rand_generate.write_to_files(exercises)
        # 检查文件是否存在并且内容正确
        with open('exercise.txt', 'r') as exer_file, open('answer.txt', 'r') as ans_file:
            exer_lines = exer_file.readlines()
            ans_lines = ans_file.readlines()
            self.assertEqual(len(exer_lines), len(ans_lines))
            for i, line in enumerate(exer_lines, 1):
                self.assertTrue(line.startswith(f"{i}. "))
                self.assertTrue(" = \n" in line)
            for i, line in enumerate(ans_lines, 1):
                self.assertTrue(line.startswith(f"{i}. "))


if __name__ == '__main__':
    unittest.main()
