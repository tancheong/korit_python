import tkinter as tk

# 기본 창 구성
root = tk.Tk() # 새로운 창 생성
root.title("GUI 프로그래밍 실습") # 창 제목(타이틀)
root.geometry("800x800") # 창 크기(가로x세로) 조절(픽셀 단위)
root.resizable(False, False) # 창 크기 조절 가능/불가능

# label = tk.Label(root, text="안녕하세요", fg="red", bg="blue")
# label.pack(side="top") # top, bottom, left, right

# 라벨 각각에 이름 나이 주소 3가지를 적고 아래에서 위 방향으로 pack
# 이름:***
# 나이:**
# 주소:****
# name_label = tk.Label(root, text="이름:이정민")
# age_label = tk.Label(root, text="나이:23")
# address_label = tk.Label(root, text="부산광역시 수영구")
# address_label.pack(side="bottom")
# age_label.pack(side="bottom")
# name_label.pack(side="bottom")

def button_click():
    print("클릭 됨")
    root.quit() # 창 닫기

button = tk.Button(root, text="종료", command=button_click)
button.pack(side="bottom")

entry = tk.Entry(root)
entry.pack(side="top")

def chk_button_clik():
    print(entry.get())
    print(chk_var.get())
    print(radio_var.get())

chk_button = tk.Button(root, text="확인", command=chk_button_clik, bg="yellow", padx=5, pady=10)
chk_button.pack(side="top")

text = tk.Text(root, wrap="word")
# none: 줄 바꿈을 하지 않음
# char: 글자 단위로 줄 바꿈
# word: 단어 단위로 줄 바꿈
text.pack(side="top")

chk_var = tk.IntVar()
chk_btn = tk.Checkbutton(root, text="위 내용에 거짓이 없음을 동의합니다.", variable=chk_var)
chk_btn.pack(side="bottom")

radio_var = tk.StringVar()
r1 = tk.Radiobutton(root, text="옵션1", variable=radio_var, value="첫 번째 옵션")
r2 = tk.Radiobutton(root, text="옵션2", variable=radio_var, value="두 번째 옵션")
r3 = tk.Radiobutton(root, text="옵션3", variable=radio_var, value="세 번째 옵션")
r1.pack(side="top")
r2.pack(side="top")
r3.pack(side="top")

root.mainloop() # 창 실행