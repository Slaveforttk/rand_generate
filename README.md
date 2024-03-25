# 四则运算器实现

| 这个作业属于哪个课程 | [软件工程](https://edu.cnblogs.com/campus/gdgy/SoftwareEngineering2024) |
| -------------------- | ------------------------------------------------------------ |
| 这个作业要求在哪里   | [四则运算](https://edu.cnblogs.com/campus/gdgy/SoftwareEngineering2024/homework/13137) |
| 这个作业的目标       | 总结成败得失，分享经验，总结教训                             |

你可以在GitHub上找到本项目并下载所有的算法和查看日志

[Slave](https://github.com/Slaveforttk/rand_generate)

[使用手册](https://www.cnblogs.com/zjmforttk/p/18095748)

### *计划*

第二次使用PSP方法进行软件实现，本次编程吸取上一次的经验，在实现一个模块，立即生成测试文件对模块进行测试，可以降低后期bug修改成本

### *开发*

#### *需求分析*

功能需求：用户需要一个四则运算生成器

开发环境：Python3环境下进行开发

产品功能：可以使用-n来控制题目生成个数

​					-r可以控制数值范围

​					可以对比题目与答案对错

开发须知：生成的题目中计算过程不能产生负数

​					生成的题目中如果存在形如e1÷ e2的子表达式，那么其结果应是真分数

​					每道题目中出现的运算符个数不超过3个

​					程序一次运行生成的题目不能重复

#### *特色说明*

```
项目基本实现了所有要求
1.其中真分数和假分数的实现及其复杂，我能查到的方法也只是在每次计算把假分数转换为真分数的表示，在打印的时候又转换回去
2.实现了简单的UI界面，这部分花了不少时间学习如何使用tkinter库
3.实现了对比器和生成器的功能，只是简单调用了之前实现的逻辑
4.使用中文除号代替了英文除号，这使得每次运算都要转换回去
5.可以支持生成10000及以上的题目数量
6.还可以自定义范围（可以不指定默认为10）
7.在异常操作后都会有弹窗提醒用户
```



#### *接口设计*

考虑到需求主要有两个：生成随机四则运算和对比题目与答案

此处仅给出接口大致使用，具体代码和难点分析请查看[另一个手册](https://www.cnblogs.com/zjmforttk/p/18095748)

##### 生成器接口设计

```txt
1.用于传入范围随之生成随机数
generate_number(min_num, max_num)：
2.通过接受题目数量和范围，调用随机数生成函数来进一步生成表达式
generate_exercises(num_exercises, min_num, max_num): 
3.对传入的表达式字符串进行转换计算得到答案，从而把表达式和答案都写入文件中
write_to_files(exercises):
```

##### 对比器接口设计

```
1.将假分数的形式转换为普通分数的形式
convert_mixed_fraction(fraction):
2.将表达式中的每个操作数都转换为普通分数的形式
convert_mixed_fraction_in_expression(expression):
3.对比函数主实现，具体逻辑参考另一个手册
compare_answers(exercise_file, answer_file, output_file):
```

##### UI设计

尝试以图形化替代命令行

```txt
第一部分：生成器的设计
主体函数
open_generator():用于构建一个图形化界面，并且实现生成器的调用
	go_back():用户按下返回按钮可以实现返回主界面操作
	display_answers_and_notify():实现了将答案文件读取并打印在图形化界面的操作
	generate_and_display_exercises():实现了对表达式文件读取并打印的操作
第二部分：对比器的设计
主题函数
open_comparator():用于构建一个图形化界面，用于对比器的调用
	go_back():用户按下返回按钮可以实现返回主界面操作
	run_comparator():使得用户能通过OS的操作选择输入的文件，省去了对绝对或相对路径的转换判断
		open_file_dialog():会被run_comparator()函数调用来处理选择的文件路径，便于对比
```

#### *测试运行*

仅仅针对图形化之前进行测试，图形化测试没有意义，此处仅给出一个测试代码

其他测试可以在[手册](https://www.cnblogs.com/zjmforttk/p/18095748)中找到

这个测试是针对compare函数中用于处理真分数与假分数的两个函数，其对compare函数有很大影响

```py
import unittest
from compare import convert_mixed_fraction, convert_mixed_fraction_in_expression


class TestConversionFunctions(unittest.TestCase):
    def test_convert_mixed_fraction(self):
        self.assertEqual(convert_mixed_fraction("1’1/2"), "(1 + 1/2)")
        self.assertEqual(convert_mixed_fraction("2"), "2")

    def test_convert_mixed_fraction_in_expression(self):
        self.assertEqual(convert_mixed_fraction_in_expression("1’1/2 + 2"), "(1 + 1/2) + 2")
        self.assertEqual(convert_mixed_fraction_in_expression("2 - 1’1/2"), "2 - (1 + 1/2)")


if __name__ == '__main__':
    unittest.main()
```

结果如下：

![](https://img2024.cnblogs.com/blog/3397503/202403/3397503-20240326022704571-291424972.png)


#### *效能分析*

这个部分很难做，我一开始考虑如何将两个UI放在两个文件中，再在主文件中调用，我发现这样做使得主文件调用附文件，附文件再调用主文件，这样会产生巨大延长以及无法啊正常显示UI的bug，于是我将UI的实现都放入一个文件中

更改前

![](https://img2024.cnblogs.com/blog/3397503/202403/3397503-20240326022721165-1597296104.png)


两个文件储存两个UI，之后在一个文件中调用使得UI出现问题即无法正常返回主界面

更改后

![](https://img2024.cnblogs.com/blog/3397503/202403/3397503-20240326022734303-2095948654.png)


给出函数耗费时间

可见主函数使用时间最长

![](https://img2024.cnblogs.com/blog/3397503/202403/3397503-20240326022822411-1859998751.png)


给出函数调用图

![](https://img2024.cnblogs.com/blog/3397503/202403/3397503-20240326022842568-1237465418.png)


这次项目各处运行很快，便没有使用模块测试耗费时间和优化运行效率

### *PSP表*

| ***\*PSP2.1\****                        | ***\*Personal Software Process Stages\**** | ***\*预估耗时（分钟）\**** | ***\*实际耗时（分钟）\**** |
| --------------------------------------- | ------------------------------------------ | -------------------------- | -------------------------- |
| Planning                                | 计划                                       | 60                         | 30                         |
| · Estimate                              | · 估计这个任务需要多少时间                 | 160                        | 140                        |
| Development                             | 开发                                       | 500                        | 360                        |
| · Analysis                              | · 需求分析 (包括学习新技术)                | 200                        | 300                        |
| · Design Spec                           | · 生成设计文档                             | 60                         | 60                         |
| · Design Review                         | · 设计复审                                 | 20                         | 30                         |
| · Coding Standard                       | · 代码规范 (为目前的开发制定合适的规范)    | 5                          | 5                          |
| · Design                                | · 具体设计                                 | 60                         | 80                         |
| · Coding                                | · 具体编码                                 | 200                        | 150                        |
| · Code Review                           | · 代码复审                                 | 60                         | 30                         |
| · Test                                  | · 测试（自我测试，修改代码，提交修改）     | 120                        | 160                        |
| Reporting                               | 报告                                       | 60                         | 40                         |
| · Test Repor                            | · 测试报告                                 | 20                         | 15                         |
| · Size Measurement                      | · 计算工作量                               | 5                          | 5                          |
| · Postmortem & Process Improvement Plan | · 事后总结, 并提出过程改进计划             | 30                         | 10                         |
|                                         | · 合计                                     | 1560                       | 1415                       |

