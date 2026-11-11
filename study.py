from pathlib import Path

DATA_FILE = Path(__file__).parent / "study_data.json"

print("読み込み中のJSON:", DATA_FILE.resolve())
import json
from pathlib import Path
from datetime import datetime, timedelta

DATA_FILE = Path(__file__).parent / "study_data.json"

WEEKLY_GOAL_HOURS = 12

# とりあえず内定目標日
TARGET_DATE = datetime(2027, 2, 28)

def format_seconds(seconds):
    total_minutes = int(seconds // 60)

    hours = total_minutes // 60
    minutes = total_minutes % 60

    if hours > 0:
        return f"{hours}時間{minutes}分"

    return f"{minutes}分"

def load_data():
    print("load_data:", DATA_FILE.resolve())

    if DATA_FILE.exists():
        text = DATA_FILE.read_text(encoding="utf-8")
        print("JSONの中身:", text)

        data = json.loads(text)

        if "progress_logs" not in data:
            data["progress_logs"] = []

        if "english_stamps" not in data:
            data["english_stamps"] = []

        return data

    print("study_data.json が見つかりません")

    return {
        "active_session": None,
        "sessions": [],
        "progress_logs": [],
        "english_stamps": []
    }

def save_data(data):
    # 既存データがあればバックアップを作る
    if DATA_FILE.exists():
        backup_file = DATA_FILE.with_name("study_data_backup.json")

        old_text = DATA_FILE.read_text(encoding="utf-8")

        backup_file.write_text(
            old_text,
            encoding="utf-8"
        )

    # 新しいデータを保存
    text = json.dumps(
        data,
        ensure_ascii=False,
        indent=2
    )

    DATA_FILE.write_text(
        text,
        encoding="utf-8"
    )

def start_study(category):
    data = load_data()

    if data["active_session"] is not None:
        return "すでに勉強中だよ！"

    data["active_session"] = {
        "category": category,
        "start": datetime.now().isoformat()
    }

    save_data(data)

    return f"{category}の勉強開始！"


def stop_study():
    data = load_data()

    session = data["active_session"]

    if session is None:
        return "今は勉強中じゃないよ"

    start = datetime.fromisoformat(session["start"])
    end = datetime.now()

    seconds = (end - start).total_seconds()

    finished_session = {
        "category": session["category"],
        "start": session["start"],
        "end": end.isoformat(),
        "seconds": seconds
    }

    data["sessions"].append(finished_session)
    #終了したセッションを履歴に追加
    data["active_session"] = None
    #進行中のセッションを解除
    save_data(data)
    #データをセーブ
    minutes = round(seconds / 60)
    #秒を分に直す
    return f"お疲れさま！今日は{minutes}分進んだよ！"
    #お疲れ様のメッセージを返す

def get_today_seconds():
    data = load_data()
    #データを読み込む
    today = datetime.now().date()
    #今日の日付を確認する
    total = 0
    #学習時間の合計を初期化する
    for session in data["sessions"]:
        start = datetime.fromisoformat(session["start"])

        if start.date() == today:
            total += session["seconds"]

    return total


def get_week_seconds():
    
    data = load_data()
    # 保存された学習データを読み込む
    today = datetime.now().date()
    # 今日の日付を取得する
    monday = today - timedelta(days=today.weekday())
    # 今日から今週の月曜日までの日数を引く
    total = 0
    # 学習時間の合計を0で初期化する
    for session in data["sessions"]:
    # 学習履歴を1件ずつ取り出す
        start = datetime.fromisoformat(session["start"])
         # セッション開始日時を日時データに変換する
        if start.date() >= monday:
             # 開始日が今週の月曜日以降か確認する
            total += session["seconds"]
              # 条件に合う学習時間を加算する

    return total
    # 合計した学習時間を秒単位で返す

def save_progress(progress):
    data = load_data()

    today = datetime.now().date().isoformat()

    data["progress_logs"].append({
        "date": today,
        "progress": progress
    })

    save_data(data)

def add_english_stamp(category):
    data = load_data()

    today = datetime.now().date().isoformat()

    data["english_stamps"].append({
        "date": today,
        "category": category
    })

    save_data(data)

def get_recent_english_stamps(limit=30):
    data = load_data()

    stamps = list(reversed(data["english_stamps"]))

    return stamps[:limit]

def get_dashboard():
    data = load_data()

    today_seconds = get_today_seconds()
    week_seconds = get_week_seconds()

    weekly_goal_seconds = WEEKLY_GOAL_HOURS * 3600

    remaining_seconds = max(
        weekly_goal_seconds - week_seconds,
        0
    )

    achievement = min(
        round(week_seconds / weekly_goal_seconds * 100, 1),
        100
    )

    days_left = (
        TARGET_DATE.date() - datetime.now().date()
    ).days

    return {
        "today_date": datetime.now().strftime("%Y/%m/%d"),
        "today_time": format_seconds(today_seconds),
        "week_time": format_seconds(week_seconds),
        "weekly_goal": WEEKLY_GOAL_HOURS,
        "remaining_time": format_seconds(remaining_seconds),
        "achievement": achievement,
        "days_left": days_left,
        "studying": data["active_session"] is not None,
        "active_session": data["active_session"],
        "sessions": get_recent_sessions(),
        "progress_logs": get_recent_progress(),
        "week_chart": get_week_chart(),
        "english_stamps": get_recent_english_stamps(),
    }

def get_recent_sessions(limit=10):
    data = load_data()

    sessions = list(reversed(data["sessions"]))

    result = []

    for session in sessions[:limit]:
        start = datetime.fromisoformat(session["start"])

        result.append({
            "category": session["category"],
            "date": start.strftime("%m/%d"),
            "time": format_seconds(session["seconds"])
        })

    return result

def get_recent_progress(limit=7):
    data = load_data()

    logs = list(reversed(data["progress_logs"]))

    return logs[:limit]

def get_week_chart():
    data = load_data()

    today = datetime.now().date()
    monday = today - timedelta(days=today.weekday())

    chart = []
    day_names = ["月", "火", "水", "木", "金", "土", "日"]

    for i in range(7):
        date = monday + timedelta(days=i)

        programming_seconds = 0
        toeic_seconds = 0

        for session in data["sessions"]:
            start = datetime.fromisoformat(session["start"])

            if start.date() == date:

                if session["category"] == "TOEIC":
                    toeic_seconds += session["seconds"]

                else:
                    programming_seconds += session["seconds"]

        programming_minutes = int(programming_seconds // 60)
        toeic_minutes = int(toeic_seconds // 60)

        chart.append({
            "day": day_names[i],
            "programming_minutes": programming_minutes,
            "toeic_minutes": toeic_minutes
        })

    max_minutes = max(
        [
            max(
                day["programming_minutes"],
                day["toeic_minutes"]
            )
            for day in chart
        ],
        default=0
    )

    for day in chart:

        if max_minutes > 0:

            day["programming_height"] = int(
                day["programming_minutes"]
                / max_minutes
                * 100
            )

            day["toeic_height"] = int(
                day["toeic_minutes"]
                / max_minutes
                * 100
            )

        else:
            day["programming_height"] = 0
            day["toeic_height"] = 0

    return chart