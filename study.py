import json
from pathlib import Path
from datetime import datetime, timedelta

DATA_FILE = Path("study_data.json")

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
    if DATA_FILE.exists():
        text = DATA_FILE.read_text(encoding="utf-8")
        data = json.loads(text)

        if "progress_logs" not in data:
            data["progress_logs"] = []

        return data

    return {
        "active_session": None,
        "sessions": [],
        "progress_logs": []
    }

def save_data(data):
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
    data["active_session"] = None

    save_data(data)

    minutes = round(seconds / 60)

    return f"お疲れさま！今日は{minutes}分進んだよ！"


def get_today_seconds():
    data = load_data()

    today = datetime.now().date()

    total = 0

    for session in data["sessions"]:
        start = datetime.fromisoformat(session["start"])

        if start.date() == today:
            total += session["seconds"]

    return total


def get_week_seconds():
    data = load_data()

    today = datetime.now().date()

    monday = today - timedelta(days=today.weekday())

    total = 0

    for session in data["sessions"]:
        start = datetime.fromisoformat(session["start"])

        if start.date() >= monday:
            total += session["seconds"]

    return total


def save_progress(progress):
    data = load_data()

    today = datetime.now().date().isoformat()

    data["progress_logs"].append({
        "date": today,
        "progress": progress
    })

    save_data(data)


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
        "week_chart": get_week_chart()
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
        total_seconds = 0

        for session in data["sessions"]:
            start = datetime.fromisoformat(session["start"])

            if start.date() == date:
                total_seconds += session["seconds"]

        chart.append({
            "day": day_names[i],
            "minutes": int(total_seconds // 60)
        })

    max_minutes = max(
        [day["minutes"] for day in chart],
        default=0
    )

    for day in chart:
        if max_minutes > 0:
         day["height"] = int(
    day["minutes"] / max_minutes * 100
)
            
        else:
            day["height"] = 0

    return chart