from app.model import Position,Skill
from pandas import DataFrame
import datetime
import matplotlib.pyplot as plt
import seaborn
def getPosintionNum_by_time():
    columns = Skill.query.all()
    rower = Position.query.all();

    datelist = get_last_month()
    print(datelist)
    info = {}
    for month in datelist:
        print(month)
        list = []
        for column in columns:
            # 查询 每个月 每个技能 的岗位数
            count = Position.query.filter(Position.skillName == column.skillName,Position.createTime.like(month+'%')).count()
            list.append(count)
        info[month] = list
    df = DataFrame(info)
    df.to_csv(
        ".\\info.csv"
    )
    seaborn.distplot(df['2018-04'])
    plt.show()
    print(info)


def get_last_month():
    #获取过去的12个月
    now = datetime.datetime.now()
    today_year = now.year
    last_year =  int(now.year) -1
    today_year_months = range(1,now.month+1)
    last_year_months = range(now.month+1, 13)
    data_list_lasts = []
    for last_year_month in last_year_months:
        if last_year_month < 10:
            data_list = '%s-0%s' % (last_year, last_year_month)
            data_list_lasts.append(data_list)
        else:
            date_list = '%s-%s' % (last_year, last_year_month)
            data_list_lasts.append(date_list)

    data_list_todays = []
    for today_year_month in today_year_months:
        if today_year_month < 10:
            data_list = '%s-0%s' % (today_year, today_year_month)
            data_list_todays.append(data_list)
        else:
            data_list = '%s-%s' % (today_year, today_year_month)
            data_list_todays.append(data_list)
    data_year_month = data_list_lasts + data_list_todays
    data_year_month.reverse()
    return data_year_month