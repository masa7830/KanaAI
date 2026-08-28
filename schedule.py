from pathlib import Path

SCHEDULE_FILE = Path("schedule.txt")


def add_schedule():
    print("Kana:日付を入力してください")
    print("Kana:例：2026-08-12")

    date = input()

    print("Kana:予定を入力してください")
    schedule = input()

    with SCHEDULE_FILE.open("a", encoding="utf-8") as file:
        file.write(f"{date},{schedule}\n")

    print(f"Kana:{date}の予定として{schedule}を登録したよ！")


def check_schedule():
    print("Kana:何日の予定を確認しますか？")
    check_date = input()

    if not SCHEDULE_FILE.exists():
        print("Kana:まだ予定は登録されてないよ")
        return

    found = False

    with SCHEDULE_FILE.open("r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            date, schedule = line.split(",", 1)

            if date == check_date:
                print(f"Kana:{date}の予定は{schedule}です。")
                found = True

    if not found:
        print(f"Kana:{check_date}の予定は登録されてないよ")


def schedule_menu():
    while True:
        print("Kana:何をしますか？")
        print("Kana:1.予定を登録する")
        print("Kana:2.予定を確認する")
        print("Kana:3.戻る")

        choice = input()

        if choice == "1":
            add_schedule()

        elif choice == "2":
            check_schedule()

        elif choice == "3":
            break

        else:
            print("Kana:ごめん、よく分からなかった")
            print("Kana:もう一度選んでね！")