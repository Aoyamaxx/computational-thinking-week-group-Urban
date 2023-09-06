
def solution_station_2(date):
    from datetime import datetime

    date_object = datetime.strptime(date, '%Y-%m-%d')

    day = date_object.isoweekday()

    weekdays_num = {1: '月曜日', 2: '火曜日', 3: '水曜日', 4: '木曜日', 5: '金曜日', 6: '土曜日', 7:'日曜日'}

    japanese_day = weekdays_num[day]

    return japanese_day

