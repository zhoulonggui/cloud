from sqlalchemy import func, or_, not_,and_
import dbConn
import sa_obj_to_dict

class db:

    #function delete one image according to id
    #The meaning of 2 delete 
    def deleteOneImage(self,id):
        query = dbConn.session.query(dbConn.Image)
        query.filter(dbConn.Image.id==id).update({dbConn.Image.status:'2'})

    #show all image    
    def listAllImage(self):
        query = dbConn.session.query(dbConn.Image)
        qry = query.filter(dbConn.Image.status==1)
        res = sa_obj_to_dict.sa_obj_to_dict(qry)
        return res

    #show have delete image
    def listOtherImage(self):
        query = dbConn.session.query(dbConn.Image)
        qry = query.filter(dbConn.Image.status==2)
        res = sa_obj_to_dict.sa_obj_to_dict(qry)
        return res

    
    #dic is a dictionary
    def addNewImage(self,dic):
        i = dbConn.img_table.insert()
        i.execute(name = dic['name'],system = dic['system'],size = dic['size'],version = dic['version'],description = dic['description'])
    

    #update an image according to some choice    
    def updateByXXX(self,choice,id,value):
        if choice=="name":
            query = dbConn.session.query(dbConn.Image)
            query.filter(dbConn.Image.id==id).update({dbConn.Image.name:value})
        elif choice =="system":
            query = dbConn.session.query(dbConn.Image)
            query.filter(dbConn.Image.id==id).update({dbConn.Image.system:value})
        elif choice =="size":
            query = dbConn.session.query(dbConn.Image)
            query.filter(dbConn.Image.id==id).update({dbConn.Image.size:value})
        elif choice =="version":
            query = dbConn.session.query(dbConn.Image)
            query.filter(dbConn.Image.id==id).update({dbConn.Image.version:value})  
        elif choice =="description":
            query = dbConn.session.query(dbConn.Image)
            query.filter(dbConn.Image.id==id).update({dbConn.Image.description:value})   
        else:
            print "Do nothing!"
        
    #find some image according to some choice        
    def selectByXXX(self,choice,value):
        if choice=="name":
            query = dbConn.session.query(dbConn.Image)
            qry = query.filter(and_(dbConn.Image.name==value,dbConn.Image.status ==1)).all()
            res = sa_obj_to_dict.sa_obj_to_dict(qry)
        elif choice =="system":
            query = dbConn.session.query(dbConn.Image)
            qry = query.filter(and_(dbConn.Image.system==value,dbConn.Image.status ==1)).all()  
            res = sa_obj_to_dict.sa_obj_to_dict(qry)
        elif choice =="size":
            query = dbConn.session.query(dbConn.Image)
            qry = query.filter(and_(dbConn.Image.size==value,dbConn.Image.status ==1)).all() 
            res = sa_obj_to_dict.sa_obj_to_dict(qry)
        elif choice =="version":
            query = dbConn.session.query(dbConn.Image)
            qry = query.filter(and_(dbConn.Image.version==value,dbConn.Image.status ==1)).all()
            res = sa_obj_to_dict.sa_obj_to_dict(qry)
        elif choice =="description":
            query = dbConn.session.query(dbConn.Image)
            qry = query.filter(and_(dbConn.Image.description==value,dbConn.Image.status ==1)).all() 
            res = sa_obj_to_dict.sa_obj_to_dict(qry)
        else:
            res = {'Error':'Do nothing!,please try other choice!'}
        
        return res