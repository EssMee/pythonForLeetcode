def special(year,month,day):
    """注: 还需要额外处理3->4, 5->6, 8->9, 10->11这四个时间点的31号的订单，定义函数special()
    """
    if (month == 3 and day == 31) or (month ==5 and day ==31) or (month == 8 and day == 31) or (month == 10 and day == 31):
        return True

def isLeapYear(year):
    """
    rtype = bool
    """
    if year % 4 == 0 and year % 100 !=0:
        return True
    else:
        return False
def getExpirationDate(year, month, day):
    """方便计算闰平年，限定year从2000到2050.
    世纪年能被400整除为闰年
    输入格式请遵守：数字年份+字母月份+数字日期

    """
    # dateDict_LearYear = {"Jan":31,"Feb_LearYear":29,"March":31,
    # "Apr":30, "May":31, "Jun":30, "Jul":31, "Aug":31, "Sep":30, "Oct":31,
    # "Nov":30, "Dec":31}
    # dateDict_NotLearYear = {"Jan":31, "Feb":28, "March":31,
    # "Apr":30, "May":31, "Jun":30, "Jul":31, "Aug":31, "Sep":30, "Oct":31,
    # "Nov":30, "Dec":31}
    output = []
    # month = ["Jan","Feb","March","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    # month = [1,2,3,4,5,6,7,8,9,10,11,12]
    # year_carry = 0
    if isLeapYear(year):
        """ 闰年的时候，二月有29天，可以接受1月29之前的订单；
        订单时间在1月30，31时要特殊处理
        """
        if month == 1:
            if day == 31:
                year = year
                month = 3
                day = 2
            elif day == 30:
                year = year
                month = 3
                day = 1
            else:
                year = year
                month += 1
                day = day
            # output.append(year)
            # output.append(month)
            # output.append(day)
    
        elif month == 12:
            year += 1
            month = 1
            day = day
        elif special(year,month,day):
            year = year
            month += 2
            day = 1
        else:
            year = year
            month += 1
            day = day
        output.append(year)
        output.append(month)
        output.append(day)
    else:
        # 平年时，二月有28天，只能处理1月28号及之前的订单
        if month == 1:
            if day == 29:
                year = year
                month = 3
                day = 1
            elif day ==30:
                year = year
                month = 3
                day = 2
            elif day == 31:
                year = year
                month = 3
                day = 3
        elif month == 12:
            year += 1
            month = 1
            day = day
        elif special(year,month,day):
            year = year
            month += 2
            day = 1
        else:
            year = year
            month += 1
            day = day
        output.append(year)
        output.append(month)
        output.append(day)
    return output
res1 = getExpirationDate(2003,3,31)
for i in res1:
    print(i)

res2 = getExpirationDate(2004,12,31)
for i in res2:
    print(i)

res3 = getExpirationDate(2004,1,30)
for i in res3:
    print(i)

