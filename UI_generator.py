import tkinter as tk
from tkinter import messagebox
import rand_generate as ts


def open_generator():
    def go_back():
        root.destroy()  # 关闭当前窗口
        import UI  # 导入主界面的文件
        UI.open_main_interface()  # 打开主界面

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
