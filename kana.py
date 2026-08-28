def get_reply(message):
    if "おはよう" in message:
        return "Kana:おはよう！"

    elif "疲れた" in message:
        return "Kana:お疲れさま。今日はゆっくりしよ？"

    else:
        return f"Kana:{message}なんだね"