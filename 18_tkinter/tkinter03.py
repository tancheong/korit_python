import tkinter as tk

root = tk.Tk()
root.title("회원가입")
root.geometry("500x200")

id_label = tk.Label(root, text="아이디:")
id_label.grid(row=0, column=0, pady=10)

id_entry = tk.Entry(root)
id_entry.grid(row=0, column=1, padx=5)

pw_label = tk.Label(root, text="비밀번호:")
pw_label.grid(row=1, column=0, pady=10)

pw_entry = tk.Entry(root)
pw_entry.grid(row=1, column=1, padx=5)

def button_click():
    user_id = id_entry.get()
    print(f"아이디: {user_id}")

button_label = tk.Button(root, text="확인", command=button_click)
button_label.grid(row=0, column=2)


# entry 옆에 버튼 하나 만들고, 해당 버튼 클릭 시
# 아이디 출력
# 아이디 밑에 비밀번호도 똑같이 만드시오.

root.mainloop()