# _*_ coding : utf-8 _*_
# @Time : 2024/3/25 15:43
# @Author : Slave
# @File : UI_comparator
# @Project : homeworkTest.py

from compare import compare_answers
import tkinter as tk
from tkinter import filedialog, messagebox


def open_file_dialog():
    filename = filedialog.askopenfilename()
    return filename


def open_comparator():
    def go_back():
        root.destroy()  # 关闭当前窗口
        import UI  # 导入主界面的文件
        UI.open_main_interface()  # 打开主界面

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
            messagebox.showwarning("警告",
                                   f"处理题目时出错: {result}\n请确认第一次传入的文件为题目文件，第二次传入的是答案文件，并且两次文件内容是合法的")

    tk.Button(root, text="运行对比器", command=run_comparator).pack()
    tk.Button(root, text="返回", command=go_back).pack()

    root.mainloop()

