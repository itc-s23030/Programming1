from datetime import datetime, timedelta


def classify_date(days_after=0):
    today = datetime.today().date()

    target_date = today + timedelta(days=days_after)

    date_difference = (target_date - today).days

    if date_difference == -1:
        return "昨日"
    elif date_difference == 0:
        return "今日"
    elif date_difference == 1:
        return "明日"
    else:
        return "今日より一日を超えて離れた日"


# テスト
print(classify_date(-1))
print(classify_date(0))
print(classify_date(1))
print(classify_date(2))  # 出力: "今日より一日を超えて離れた日"
