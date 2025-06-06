from datetime import datetime, timedelta

def generate_dates_with_weekdays(date_count=30):
    """
    生成从2000年1月1日开始的30天日期和对应的星期几。
    
    返回一个包含日期和星期几的字典列表。
    """
    # 设置起始日期
    start_date = datetime(2000, 1, 1)
    dates_list = []

    # 生成30天的日期和星期
    for i in range(date_count):
        current_date = start_date + timedelta(days=i)
        # 获取星期几的中文名称
        weekday_cn = {
            0: 'monday',
            1: 'tuesday',
            2: 'wednesday',
            3: 'thursday',
            4: 'friday',
            5: 'saturday',
            6: 'sunday'
        }[current_date.weekday()]
        
        # 格式化日期并添加星期
        date_str = {
            'date': current_date.strftime('%Y-%m-%d'),
            'weekday': weekday_cn
        }
        dates_list.append(date_str)

    return dates_list

if __name__ == "__main__":
    # 生成日期列表
    dates = generate_dates_with_weekdays(30)
    
    # 打印结果
    for date in dates:
        print(f"日期: {date['date']}, 星期: {date['weekday']}")