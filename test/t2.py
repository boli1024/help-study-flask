from datetime import datetime, timedelta, date


def future_days():  # 计算当前到未来某一天的天数
    # 构造一个将来的时间
    future = datetime.strptime('2020-6-1 0:0:0', '%Y-%m-%d %H:%M:%S')
    # 当前时间
    now = datetime.now()
    # 求时间差
    delta = future - now
    hour = delta.seconds/60/60
    minute = (delta.seconds - hour*60*60)/60
    seconds = delta.seconds - hour*60*60 - minute*60
    print(delta.days, hour, minute, seconds)


def future_time():  # 计算当前在多少天后的日期
    d1 = datetime.now()
    d = timedelta(days=100)
    print(d1 + d)


def future_after_days(year, month, day, days):
    """
    获取指定日期后多少天数的日期
    :param year: 指定年份 int
    :param month: 指定月份 int
    :param day: 指定日期 int
    :param days: 指定多少天后，间隔天数 int
    :return: 返回未来日期的一个字符串  "2010-04-11"
    """
    d1 = date(year, month, day)
    d = timedelta(days)
    return str(d1 + d)


if __name__ == '__main__':
    # future_after_days(2010, 1, 1, 100)
    print(date.today() + timedelta(-1))
