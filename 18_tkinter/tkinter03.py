import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("회원가입")
root.geometry("500x200")

id_label = tk.Label(root, text="아이디")
id_label.grid(row=0, column=0, pady=10)

id_entry = tk.Entry(root)
id_entry.grid(row=0, column=1, padx=5)

def dupl_click():
    # 실제 서버와 데이터 베이스에 정보를 요청 해서
    # 비교 하는 중복 확인 절차
    if id_entry.get() == "":
        messagebox.showwarning("경고", "아이디를 입력해주세요.")
    else:
        messagebox.showinfo("중복확인", "중복확인이 되었습니다.")

dupl_btn = tk.Button(root, text="중복확인", command=dupl_click)
dupl_btn.grid(row=0, column=2)

password_label1 = tk.Label(root, text="비밀번호")
password_label1.grid(row=1, column=0)

password_entry1 = tk.Entry(root, show="*")
password_entry1.grid(row=1, column=1)

password_label2 = tk.Label(root, text="비밀번호 확인")
password_label2.grid(row=2, column=0)

password_entry2 = tk.Entry(root, show="*")
password_entry2.grid(row=2, column=1)

chk_var = tk.IntVar()
chk_box = tk.Checkbutton(root, text="약관 내용에 동의합니다.", variable=chk_var)
chk_box.grid(row=3, column=1)

def signup_click():
    if password_entry1.get() != password_entry2.get():
        messagebox.showerror("경고", "비밀번호가 일치하지 않습니다.")
    elif chk_var.get() != 1:
        messagebox.showerror("경고", "약관 내용에 동의 해주세요.")
    else:
        messagebox.showinfo("회원가입", "성공적으로 회원가입이 되었습니다.")

signup_btn = tk.Button(root, text="회원가입", command=signup_click)
signup_btn.grid(row=4, column=2)

root.mainloop()