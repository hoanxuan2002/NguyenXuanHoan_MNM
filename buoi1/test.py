import tkinter as tk
from sympy import *
from tkinter import ttk

# Tạo một style mới
style = ttk.Style()
style.configure("TButton",
                foreground="midnight blue",
                background="light sky blue",
                font=("Helvetica", 16),
                padding=10)

style.configure("TLabel",
                foreground="midnight blue",
                background="light sky blue",
                font=("Helvetica", 16),
                padding=10)

style.configure("TEntry",
                foreground="midnight blue",
                background="white",
                font=("Helvetica", 16))


def open_limit_window():
    limit_window = tk.Toplevel(app)
    limit_window.title("Tính Giới Hạn")
    limit_label = tk.Label(limit_window, text="Nhập biểu thức cần tính giới hạn:")
    limit_label.pack()
    limit_entry = tk.Entry(limit_window)
    limit_entry.pack()
    limit_value_label = tk.Label(limit_window, text="Nhập giá trị tiến đến:")
    limit_value_label.pack()
    limit_value_entry = tk.Entry(limit_window)
    limit_value_entry.pack()
    calculate_limit_button = tk.Button(limit_window, text="Tính Giới Hạn",
                                       command=lambda: calculate_limit(limit_entry.get(), limit_value_entry.get()))
    calculate_limit_button.pack()
    clear_button = tk.Button(limit_window, text="Xóa", command=lambda: result_label.config(text=""))
    clear_button.pack()

    close_button = tk.Button(limit_window, text="Thoát", command=limit_window.destroy)
    close_button.pack()


def open_derivative_window():
    derivative_window = tk.Toplevel(app)
    derivative_window.title("Tính Đạo Hàm")

    derivative_label = tk.Label(derivative_window, text="Nhập biểu thức cần tính đạo hàm:")
    derivative_label.pack()

    derivative_entry = tk.Entry(derivative_window)
    derivative_entry.pack()
    calculate_derivative_button = tk.Button(derivative_window, text="Tính Đạo Hàm",
                                            command=lambda: calculate_derivative(derivative_entry.get()))
    calculate_derivative_button.pack()
    clear_button = tk.Button(derivative_window, text="Xóa", command=lambda: result_label.config(text=""))
    clear_button.pack()

    close_button = tk.Button(derivative_window, text="Thoát", command=derivative_window.destroy)
    close_button.pack()


def open_integral_window():
    integral_window = tk.Toplevel(app)
    integral_window.title("Tính nguyên hàm")
    integral_label = tk.Label(integral_window, text="Nhập biểu thức cần tính nguyên hàm:")
    integral_label.pack()
    integral_entry = tk.Entry(integral_window)
    integral_entry.pack()
    calculate_integral_button = tk.Button(integral_window, text="Tính Nguyên hàm",
                                          command=lambda: calculate_integral(integral_entry.get()))
    calculate_integral_button.pack()
    clear_button = tk.Button(integral_window, text="Xóa", command=lambda: result_label.config(text=""))
    clear_button.pack()

    close_button = tk.Button(integral_window, text="Thoát", command=integral_window.destroy)
    close_button.pack()


def open_polynomial_division_window():
    division_window = tk.Toplevel(app)
    division_window.title("Chia Đa Thức")
    dividend_label = tk.Label(division_window, text="Nhập biểu thức cho số tử của đa thức:")
    dividend_label.pack()
    dividend_entry = tk.Entry(division_window)
    dividend_entry.pack()
    divisor_label = tk.Label(division_window, text="Nhập biểu thức cho số mẫu của đa thức:")
    divisor_label.pack()
    divisor_entry = tk.Entry(division_window)
    divisor_entry.pack()
    calculate_polynomial_division_button = tk.Button(division_window, text="Chia Đa Thức",
                                                     command=lambda: calculate_polynomial_division(dividend_entry.get(),
                                                                                                   divisor_entry.get()))
    calculate_polynomial_division_button.pack()
    clear_button = tk.Button(division_window, text="Xóa", command=lambda: result_label.config(text=""))
    clear_button.pack()

    close_button = tk.Button(division_window, text="Thoát", command=division_window.destroy)
    close_button.pack()



def calculate_limit(expression, limit_value):
    if not expression or not limit_value:
        result_label.config(text="Vui lòng nhập biểu thức và giá trị tiến đến trước khi tính toán.")
        return
    x = Symbol('x')
    result = limit(sympify(expression), x, float(limit_value))
    result_label.config(text=f"Kết quả: {result}")