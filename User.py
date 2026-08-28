from pathlib import Path
from schedule import schedule_menu
from calendar_gui import open_calendar

USER_FILE = Path("user.txt")


# 終了時のあいさつ
def goodbye():
    print("Kana:行ってらっしゃい！また来てね！！ばいばーい")

# ユーザー名を読み込む・初回なら保存する
def load_user():
    if USER_FILE.exists():
        name = USER_FILE.read_text(encoding="utf-8").strip()
        print(f"Kana:おかえり、{name}！")
    else:
        print("Kana:おかえりなさい！")
        print("Kana:名前を教えてね。")

        name = input()

        USER_FILE.write_text(name, encoding="utf-8")

        print(f"Kana:{name}、よろしくね！")

    return name


# 指定した数字だけ受け付ける
def get_choice(valid_choices):
    while True:
        try:
            choice = int(input())

            if choice in valid_choices:
                return choice

        except ValueError:
            pass

        print("Kana:ごめん、よく分からなかった")
        print("Kana:もう一度選んでね！")


# 気分を聞く
def ask_mood():
    print("Kana:今日の気分はどう？")
    print("Kana:1. 元気！")
    print("Kana:2. まあまあかな")
    print("Kana:3. 疲れた")

    mood = get_choice([1, 2, 3])

    if mood == 1:
        print("Kana:元気そうでよかった！")

    elif mood == 2:
        print("Kana:まあ、そういう日もあるよ")

    elif mood == 3:
        print("Kana:お疲れ様")


# 簡単な会話
def talk():
    ask_mood()

    print("Kana:まだ話す？")
    print("Kana:1.もう少し話をする")
    print("Kana:2.今日はもう帰る")

    talk_choice = get_choice([1, 2])

    # 一度だけ引き留める
    if talk_choice == 2:
        print("Kana:もうかえっちゃうの!?")
        print("Kana:1.やっぱりもう少し話す")
        print("Kana:2.うん、今日は帰る")

        talk_choice = get_choice([1, 2])

    if talk_choice == 2:
        goodbye()
        return

    print("Kana:たくさん話そう")

    while True:
        print("Kana:何を話す？")

        message = input()

        if "疲れた" in message:
            print("Kana:お疲れさま。今日はゆっくりしよ？")

        elif "勉強" in message:
            print("Kana:勉強したんだ！何を勉強したの？")

            subject = input()

            print(f"Kana:{subject}を勉強したんだね！")

        else:
            print(f"Kana:{message}なんだね")

        print("Kana:もっと話そう！")
        print("Kana:1.もう少し話す")
        print("Kana:2.今日は帰る")

        talk_choice = get_choice([1, 2])

        if talk_choice == 2:
            goodbye()
            break


# 予定機能
def open_calendar():
    print("Kana:予定機能はあとでここにつなげるよ")


# メイン処理
def main():
    name = load_user()

    print("Kana:何する？")
    print("Kana:1.Kanaと話す")
    print("Kana:2.予定を見る")
    print("Kana:3.終わる")

    choice = get_choice([1, 2, 3])

    if choice == 1:
        talk()

    elif choice == 2:
        schedule_menu()
        
    elif choice == 3:
        goodbye()


main()