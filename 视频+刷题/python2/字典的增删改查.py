infor = {"name":"李健"}

#添加
infor["age"] = 39
infor["qq"] = "79889899"
infor["addr"] = "哈尔滨"
print(infor)

#删除
del infor["age"]
print(infor)

#查询
#一般不用infor[age]查询，因为要是字典中不存在该元素，那么程序会崩溃
#一般情况下用get[name],无论如何程序都不会崩溃，不存在就返回空值
print(infor.get("name"))
print(infor.get("age"))

#修改：一般值作已存在的修改
infor["addr"] = "黑龙江"
print(infor)



