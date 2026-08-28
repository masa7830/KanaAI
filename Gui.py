import tkinter as tk
from tkinter import simpledialog
from pathlib import Path

SCHEDULE_FILE = Path("schedule.txt")


def add_schedule():
    date = simpledialog.askstring(
        "Kana",
        "日付を入力してください\n例：2026-08-12"
    )

    if not date:
        return

    schedule = simpledialog.askstring(
        "Kana",
        "予定を入力してください"
    )

    if not schedule:
        return

    with SCHEDULE_FILE.open("a", encoding="utf-8") as file:
        file.write(f"{date},{schedule}\n")

    message_label.config(
        text=f"Kana:{date}の予定は「{schedule}」だね！"
    )


def check_schedule():
    check_date = simpledialog.askstring(
        "Kana",
        "何日の予定を確認しますか？\n例：2026-08-12"
    )

    if not check_date:
        return

    if not SCHEDULE_FILE.exists():
        message_label.config(
            text="Kana:まだ予定は登録されてないよ！"
        )
        return

    results = []

    with SCHEDULE_FILE.open("r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            date, schedule = line.split(",", 1)

            if date == check_date:
                results.append(schedule)

    if results:
        result_text = "\n".join(
            f"・{schedule}" for schedule in results
        )

        message_label.config(
            text=f"Kana:{check_date}の予定だよ！\n{result_text}"
        )

    else:
        message_label.config(
            text=f"Kana:{check_date}は予定がないよ！"
        )


def end_app():
    print("Kana:行ってらっしゃい！また来てね！")
    root.destroy()


# ウィンドウを作る
root = tk.Tk()

root.title("Kana")
root.geometry("500x400")


# Kanaのセリフ
message_label = tk.Label(
    root,
    text="Kana:おかえりなさい！"
)

message_label.pack(pady=20)


# 予定登録ボタン
add_button = tk.Button(
    root,
    text="予定を登録する",
    command=add_schedule
)

add_button.pack(pady=10)


# 予定確認ボタン
check_button = tk.Button(
    root,
    text="予定を確認する",
    command=check_schedule
)

check_button.pack(pady=10)


# 終了ボタン
end_button = tk.Button(
    root,
    text="終了する",
    command=end_app
)

end_button.pack(pady=10)


# ウィンドウを表示し続ける
root.mainloop()