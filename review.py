

def check_goal(study_minutes,daily_goal):
    if study_minutes > daily_goal:
        
        return f"今日の目標達成！目標より{study_minutes-daily_goal}分勉強しました"
    elif study_minutes == daily_goal:
        return "今日の目標達成！"
    else:
        return f"目標まであと{daily_goal - study_minutes}分！"

def input_minutes(message):
    while True:
        try:
            minutes = int(input(message))

            if minutes >= 0:
                return minutes

            print("0以上の数字を入力してください")

        except ValueError:
            print("数字で入力してください")

def calculate_achievement(study_minutes, daily_goal):
    if daily_goal == 0:
        return None

    achievement = study_minutes / daily_goal * 100
    return round(achievement)

def kana_comment(achievement):
    if achievement >= 100:
        return "おつかれさま！今日は目標達成だね！"
    elif achievement >= 50:
        return "いい調子！あと少し頑張ろう！"
    else:
        return "少しずつ進めていこうね！"

def check_goal(study_minutes, daily_goal):
    if daily_goal == 0:
        if study_minutes == 0:
            return "今日はお休みの日です！"
        else:
            return f"お休みの日だけど{study_minutes}分勉強しました！"

    if study_minutes > daily_goal:
        return f"今日の目標達成！目標より{study_minutes - daily_goal}分勉強しました"
    elif study_minutes == daily_goal:
        return "今日の目標達成！"
    else:
        return f"目標まであと{daily_goal - study_minutes}分！"

daily_goal = input_minutes("今日の目標時間を入力してください：")
study_minutes = input_minutes("今日の勉強時間を入力してください：")

message = check_goal(study_minutes, daily_goal)
achievement = calculate_achievement(study_minutes, daily_goal)

print(message)

if achievement is None:
    print("今日は目標を設定しない日です")
else:
    print(f"今日の達成率は{achievement}%です")
    comment = kana_comment(achievement)
    print(f"Kana：{comment}")

with open("study_log.txt", "a", encoding="utf-8") as file:
    file.write(f"目標：{daily_goal}分、勉強：{study_minutes}分\n")

print("今日の記録を保存しました")