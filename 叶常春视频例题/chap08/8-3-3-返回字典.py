#例8-3-3  返回字典
def build_person(first_name, last_name, age=''):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first': first_name, 'last': last_name}
    if age:  #age参数不为空
        person['age'] = age
    return person
musician = build_person('亮', '诸葛', age=27)
print(musician)