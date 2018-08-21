#！/usr/bin/python
from py_linq import Enumerable


class jzd(object):
    id = None
    isyz = False
    isjs = False
    value = None


class ljbm(object):
    start = jzd()
    end = jzd()


ls = []

cjzd1 = jzd()
cjzd1.id = 1
cjzd1.value = 1

cjzd2 = jzd()
cjzd2.id = 2
cjzd2.value = 2

cjzd3 = jzd()
cjzd3.id = 3
cjzd3.value = 3

cjzd4 = jzd()
cjzd4.id = 4
cjzd4.value = 4

cjzd5 = jzd()
cjzd5.id = 5
cjzd5.value = 5

cjzd6 = jzd()
cjzd6.id = 6
cjzd6.value = 6

cjzd7 = jzd()
cjzd7.id = 7
cjzd7.value = 7

cjzd8 = jzd()
cjzd8.id = 8
cjzd8.value = 8

cjzd9 = jzd()
cjzd9.id = 9
cjzd9.value = 1

ljbm1 = ljbm()
ljbm1.start = cjzd1
ljbm1.end = cjzd2
ls.append(ljbm1)

ljbm2 = ljbm()
ljbm2.start = cjzd8
ljbm2.end = cjzd5
ls.append(ljbm2)

ljbm2 = ljbm()
ljbm2.start = cjzd5
ljbm2.end = cjzd2
ls.append(ljbm2)

ljbm3 = ljbm()
ljbm3.start = cjzd2
ljbm3.end = cjzd3
ls.append(ljbm3)

ljbm3 = ljbm()
ljbm3.start = cjzd3
ljbm3.end = cjzd6
ls.append(ljbm3)

ljbm4 = ljbm()
ljbm4.start = cjzd4
ljbm4.end = cjzd3
ls.append(ljbm4)

ljbm4 = ljbm()
ljbm4.start = cjzd7
ljbm4.end = cjzd4
ls.append(ljbm4)

ljbm4 = ljbm()
ljbm4.start = cjzd4
ljbm4.end = cjzd9
ls.append(ljbm4)



jd = []
for item in ls:
    jd.append(item.start)
    jd.append(item.end)
linq = Enumerable(jd)
jd = linq.distinct(lambda x: x.id).to_list()

print("邻接表start")
for k in ls:
    print(str(k.start.id)+"-->"+str(k.end.id))
print("邻接表end")

print("数据值start")
for i in jd:
    print(str(i.id)+"：" + str(i.value))
    print("=======================")
print("数据值End")

bjjd = []
startjd = None
for items in jd:
    lslinq = Enumerable(ls)
    startcount = lslinq.where(lambda x: x.start.id == items.id).count() > 0
    endcount = lslinq.where(lambda x: x.end.id == items.id).count() > 0
    if startcount and not endcount:
        startjd = items
        items.isyz = True
        bjjd.append(items)
    if not startcount and endcount:
        items.isyz = True
        bjjd.append(items)

for h in bjjd:
    print(str(h.id)+"---边界点---》" + str(h.value)+"-->状态："+str(h.isyz))


jsjg = []


def bl(startjd1):
    startjd1.isjs = True
    print("当前计算点："+str(startjd1.id))
    linqb = Enumerable(ls)
    startls = linqb.where(lambda x: x.start.id ==
                          startjd1.id and not x.end.isjs).to_list()
    endls = linqb.where(lambda x: x.end.id ==
                        startjd1.id and not x.start.isjs).to_list()
    hfji = []
    for jjkkz in endls:
        jjkkz.start.isyz = False
        hfji.append(zsbl(jjkkz.start))

    linqjd = Enumerable(jd)
    jd1 = linqjd.where(lambda x: x.id == startjd1.id).to_list()
    if jd1[0].isyz:
        return startjd1
    for jjjk in startls:
        print(jjjk.end.id)
    print("当前计算点END："+str(startjd1.id))

    for kkkkkjjj in startls:
        kkkkkjjj.end.isjs = True
        hfji.append(bl(kkkkkjjj.end))

    value = 0
    hfji.append(startjd1)
    for it in hfji:
        value += it.value
    startjd1.value = value
    newjg = jzd()
    newjg.id = startjd1.id
    newjg.value = value
    jsjg.append(newjg)
    return startjd1


def zsbl(startjd1):
    startjd1.isjs = True

    print("当前计算点正算："+str(startjd1.id))
    linqjd = Enumerable(jd)
    jd1 = linqjd.where(lambda x: x.id == startjd1.id).to_list()
    if jd1[0].isyz:
        return startjd1
    linqb = Enumerable(ls)
    endls = linqb.where(lambda x: x.end.id ==
                        startjd1.id and not x.start.isjs).to_list()
    startls = linqb.where(lambda x: x.start.id ==
                          startjd1.id and not x.end.isjs).to_list()
    hfji = []
    for kkkkkjjj in startls:
        kkkkkjjj.end.isjs = True
        startjd1.value+= bl(kkkkkjjj.end).value

    for jjjk in endls:
        print(jjjk.start.id)
    print("当前计算点正算END："+str(startjd1.id))

    for kkkkkjjj in endls:
        hfji.append(zsbl(kkkkkjjj.start))
    value = 0
    hfji.append(startjd1)
    for it in hfji:
        if value == 0:
            value = it.value
        else:
            value -= it.value
    startjd1.value = -value
    newjg = jzd()
    newjg.id = startjd1.id
    newjg.value = value
    jsjg.append(newjg)
    return startjd1


print("计算过程结果")

bjjdlinq = Enumerable(bjjd)
star2 = bjjdlinq.where(lambda x: x.id == 1).to_list()
star2[0].isyz = False
bl(star2[0])
for kkll in jsjg:
    print(str(kkll.id) + ":" + str(kkll.value))


jdjg = []
for item in ls:
    jdjg.append(item.start)
    jdjg.append(item.end)
linq = Enumerable(jdjg)
jdjg = linq.distinct(lambda x: x.id).to_list()

print("结果start")
for i in jdjg:
    print(str(i.id)+"：" + str(i.value))
    print("=======================")
print("结果End")
