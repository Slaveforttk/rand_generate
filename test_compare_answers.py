import unittest
from compare import compare_answers


class TestCompareAnswers(unittest.TestCase):
    def test_compare_answers(self):
        # 创建题目文件和答案文件
        with open('exercise_test.txt', 'w') as f_ex, open('answer_test.txt', 'w') as f_ans:
            f_ex.write('1.  1 + 1 =\n2.  2 * 2 =\n')
            f_ans.write('1.  2\n2.  4\n')

        # 调用 compare_answers 函数
        compare_answers('exercise_test.txt', 'answer_test.txt', 'output_test.txt')

        # 验证输出文件的内容
        with open('output_test.txt', 'r') as f_out:
            output = f_out.read()
        self.assertEqual(output, '正确的题目有2道，分别是：[1, 2]\n错误的题目有0道，分别是：[]\n')


if __name__ == '__main__':
    unittest.main()
