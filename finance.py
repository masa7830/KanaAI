from datetime import date
import json
import os

FILE_NAME = "finance_data.json"


def input_money(message):
    while True:
        try:
            money = int(input(message))

            if money >= 0:
                return money

            print("0以上の数字を入力してください")

        except ValueError:
            print("数字で入力してください")

def save_data(data):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def show_reward(gohoubi):
    if gohoubi >= 1000:
        print("Kana：母港拡張できるよ！")

    elif gohoubi >= 700:
        print("Kana：ネジ10本に届いたよ！")

    elif gohoubi >= 500:
        print("Kana：補強増設に届いたよ！")

    else:
        remaining = 500 - gohoubi
        print(f"Kana：補強増設まであと{remaining}円！")



if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r", encoding="utf-8") as file:
        data = json.load(file)

else:
    print("初回設定を始めます。")

    home_budget = input_money("在宅日の予算を入力してください：")
    outing_budget = input_money("外出日の予算を入力してください：")

    data = {
    "home_budget": home_budget,
    "outing_budget": outing_budget,
    "gohoubi": 0,
    "records": {}
}
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    print("予算を保存しました。")


home_budget = data["home_budget"]
outing_budget = data["outing_budget"]
gohoubi = data["gohoubi"]

print(f"現在のごほうび残高：{gohoubi}円")

today = date.today().isoformat()
print(f"今日の日付：{today}")
records = data.setdefault("records", {})

if today in records:
    previous_spending = records[today]["spending"]    
    print(f"今日の登録済み支出：{previous_spending}円")
else:
    print("今日の記録はまだありません。")

def select_today_budget(home_budget, outing_budget):
    while True:
        day_type = input("今日の過ごし方を選んでください（1：在宅、2：外出）：")

        if day_type == "1":
            return home_budget

        elif day_type == "2":
            return outing_budget

        else:
            print("1か2を入力してください")

today_budget = select_today_budget(home_budget, outing_budget)
print(f"今日の予算は{today_budget}円です。")

spending = input_money("今日使った合計金額を入力してください：")

change = today_budget - spending

print(f"今日の予算：{today_budget}円")
print(f"今日の支出：{spending}円")
print(f"今日の増減：{change:+}円")
if today in records:
    previous_change = records[today]["change"]
    gohoubi -= previous_change
    print("今日の記録を更新しました。")

gohoubi += change

records[today] = {
    "budget": today_budget,
    "spending": spending,
    "change": change
}

data["gohoubi"] = gohoubi
data["records"] = records


print(f"ごほうび残高：{gohoubi}円")

show_reward(gohoubi)



save_data(data)


