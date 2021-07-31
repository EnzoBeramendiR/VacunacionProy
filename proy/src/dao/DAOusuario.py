import pymysql

class DAOusuario:
    def __init__(self):
        pass

    def connect(self):
        return pymysql.connect(host="localhost",user="root",password="",database="db_proyecto")

    def read(self,id):
        con = DAOusuario.connect(self)
        cursor = con.cursor()
        
        try:
            if id == None:
                cursor.execute("select * from usuario order by nomb")
            else:    
                cursor.execute("select * from usuario where id=%s order by nomb",(id,))
            return cursor.fetchall()
        except:
            return()
        finally:
            con.close()    

    def insert(self,data):
        con = DAOusuario.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("insert into usuario(nomb, pass, func, lugar, distri, edad) values(%s, %s, %s, %s, %s, %s)",(data['nomb'],data['pass'],data['func'],data['lugar'],data['distri'],data['edad'],))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()

    def update_doc(self,id,data):
        con = DAOusuario.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("update usuario set nomb=%s,pass=%s, func=%s, lugar=%s, distri=%s, edad=%s where id=%s",(data['nomb'],data['pass'],data['func'],data['lugar'],data['distri'],data['edad'],id,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()


    def update_pac(self,id,data):
        con = DAOusuario.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("update usuario set nomb=%s, lugar=%s, distri=%s, edad=%s where id=%s",(data['nomb'],data['lugar'],data['distri'],data['edad'],id,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()

    def delete(self,id):
        con = DAOusuario.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("delete from usuario where id=%s",(id,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()                    