import os,time,shutil

def R_name():
    import re
    from datetime import datetime
    pattern = 'YX_backup_(?P<year>\d+)_(?P<mon>[0-1]?[0-9]?)_(?P<day>[0-3]?[0-9]?)_(?P<n1>\d+)_(?P<n2>\d+).bak'
    path=os.getcwd()
    names = os.listdir(path)
    p = re.compile(pattern)
    curtime = datetime.now()
    year = int(curtime.strftime('%Y'))
    month = int(curtime.strftime('%m'))
    day = int(curtime.strftime('%d'))
    for n in names:
        match = p.match(n)
        if match:
            y = int(match.group(1))
            m = int(match.group(2))
            d = int(match.group(3))
            if y == year and m == month and d == day:
                b_p=os.path.join(path,n)
                b_p1=b_p.replace('\\','/')
                print(b_p1)
                shutil.copyfile(b_p1,"//192.168.0.111/u9备份/YX/{}".format(n))

def del_file():
    bf_path="//192.168.0.111/u9备份/YX/"
    names=os.listdir(bf_path)
    while(len(names)>3):
        names.sort()
        del_path=os.path.join(bf_path,names[0])
        os.remove(del_path)
        names.pop(0)

def DeltaSeconds():
    SECONDS_PER_DAY = 24 * 60 * 60
    from datetime import datetime, timedelta
    curTime = datetime.now()
    desTime = curTime.replace(hour=5, minute=0, second=0, microsecond=0)  #这里添加时间
    delta = desTime - curTime
    skipSeconds = delta.total_seconds() % SECONDS_PER_DAY
    print("Must sleep %d seconds" % skipSeconds)
    return skipSeconds


while True:
    s = DeltaSeconds()
    time.sleep(s)
    # print ("work it!" ) #这里可以替换成作业
    print("开始备份：")
    R_name()
    del_file()
    print("备份成功！")

