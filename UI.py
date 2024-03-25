import tkinter as tk
import rand_generate as ts
from compare import compare_answers
from tkinter import filedialog, messagebox


def open_file_dialog():
    filename = filedialog.askopenfilename()
    return filename


def open_comparator():
    def go_back():
        root.destroy()  # 关闭当前窗口
        # import UI  # 导入主界面的文件
        open_main_interface()  # 打开主界面

    root = tk.Tk()
    root.title("四则运算题目对比器")

    result_text = tk.Text(root)
    result_text.pack()

    # 在文本框中插入提示信息
    result_text.insert(tk.END, "请点击开始运行对比器，之后请依次选择题目文件，答案文件，输出结果文件\n")

    def run_comparator():
        # 跳转到输入路径的界面
        exercise_file = open_file_dialog()
        answer_file = open_file_dialog()
        output_file = open_file_dialog()
        result = compare_answers(exercise_file, answer_file, output_file)

        if result == "Success":
            with open(output_file, 'r') as f_out:
                output = f_out.read()
            result_text.delete('1.0', tk.END)
            result_text.insert(tk.END, output)
            messagebox.showinfo("提示", "文件对比成功，结果已保存到output.txt中")
        elif result == "FileNotFoundError":
            messagebox.showerror("错误", "未找到题目或答案文件")
        else:
            messagebox.showwarning("警告", f"处理题目时出错: {result}\n请确认第一次传入的文件为题目文件，第二次传入的是答案文件，并且两次文件内容是合法的")

    tk.Button(root, text="运行对比器", command=run_comparator).pack()
    tk.Button(root, text="返回", command=go_back).pack()

    root.mainloop()


def open_generator():
    def go_back():
        root.destroy()  # 关闭当前窗口
        # import UI  # 导入主界面的文件
        open_main_interface()  # 打开主界面

    def display_answers_and_notify():
        try:
            with open('exercise.txt', 'r') as f_ex, open('answer.txt', 'r') as f_ans:
                exercises = f_ex.readlines()
                answers = f_ans.readlines()
        except FileNotFoundError:
            messagebox.showerror("错误", "未找到题目或答案文件")
            return

        exercises_text.delete('1.0', tk.END)
        for exercise, answer in zip(exercises, answers):
            exercises_text.insert(tk.END, f"{exercise.strip()} {answer.split('. ')[1]}\n")

        messagebox.showinfo("提示", "答案已生成到answer文件")

    def generate_and_display_exercises():
        try:
            num_exercises = int(num_exercises_entry.get())
            if num_exercises <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("错误", "题目数量必须是一个正整数")
            return

        try:
            num_range = range_entry.get()
            if num_range:
                min_num, max_num = map(int, num_range.split('-'))
                if min_num >= max_num or min_num <= 0:
                    raise ValueError
            else:
                min_num, max_num = 1, 10
        except ValueError:
            messagebox.showerror("错误", "随机数范围必须是两个正整数，用'-'分隔，且第一个数小于第二个数")
            return

        exercises = ts.generate_exercises(num_exercises, min_num, max_num)
        ts.write_to_files(exercises)
        messagebox.showinfo("提示", "题目已经生成到exercise.txt文件")
        # 将假分数的形式转换回 a'b/c
        exercises = [ts.format_exercise(ex) for ex in exercises]
        exercises_text.delete('1.0', tk.END)
        for i, ex in enumerate(exercises, 1):
            exercises_text.insert(tk.END, f"{i}.  {ex} =\n")

    root = tk.Tk()
    root.title("四则运算题目生成器")

    tk.Label(root, text="题目数量：").grid(row=0, column=0)
    num_exercises_entry = tk.Entry(root)
    num_exercises_entry.grid(row=0, column=1)

    tk.Label(root, text="随机数范围（可选）：").grid(row=1, column=0)
    range_entry = tk.Entry(root)
    range_entry.grid(row=1, column=1)

    tk.Button(root, text="生成题目", command=generate_and_display_exercises).grid(row=2, column=0, columnspan=2)
    tk.Button(root, text="显示答案", command=display_answers_and_notify).grid(row=4, column=0, columnspan=2)
    exercises_text = tk.Text(root)
    exercises_text.grid(row=3, column=0, columnspan=2)

    tk.Button(root, text="返回", command=go_back).grid(row=5, column=0, columnspan=2)

    root.mainloop()


def open_main_interface():
    root = tk.Tk()
    root.title("四则运算题目生成器和对比器")

    def open_generator_ui():
        root.destroy()  # 关闭主界面
        open_generator()  # 打开生成器

    def open_comparator_ui():
        root.destroy()  # 关闭主界面
        open_comparator()  # 打开对比器

    tk.Label(root, text="请选择一个操作：", font=("Arial", 14)).pack(pady=10)

    tk.Button(root, text="打开生成器", command=open_generator_ui, font=("Arial", 12), width=30, height=2).pack(
        pady=10)
    tk.Button(root, text="打开对比器", command=open_comparator_ui, font=("Arial", 12), width=30, height=2).pack(
        pady=10)

    root.mainloop()


# 使用UI
open_main_interface()
