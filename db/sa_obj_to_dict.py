#function sqlalchemy object to dictionary
def sa_obj_to_dict(obj):
    
    res = dict()

    tuple = ('id','name','system','size','version','description')
    j = 0
    for i in obj:
        dic = dict()
        dic.update({tuple[0]:i.id})
        dic.update({tuple[1]:i.name})
        dic.update({tuple[2]:i.system})
        dic.update({tuple[3]:i.size})
        dic.update({tuple[4]:i.version})
        dic.update({tuple[5]:i.description}) 
        res.update({j:dic})
        j+=1

    return res