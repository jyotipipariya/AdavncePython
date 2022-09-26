import UserBean
from UserBean import *
import UserDao
from UserDao import *
''' 
def testAdd():
    ub = UserBean()
    ub.setFirst_name('Rama')
    ub.setLast_name('Verma')
    ub.setDOB('2001-12-10')
    ub.setEmail_id('ramaverma@gmail.com')
    ub.setPassword(123)
    ub.setMobile('9725378910')

    ud = UserDao()
    ud.add(ub)
    print("Data Added Successfully")
testAdd()


def testGetById():
    md = UserDao()
    md.getById(19)
testGetById()


'''
def testUpdate():
    ub = UserBean()
    ub.setFirst_name('Siya')
    ub.setLast_name('Verma')
    ub.setDOB(2001-12-10)
    ub.setEmail_id('siyaatgmail.com')
    ub.setPassword(123)
    ub.setMobile(9012345678)
    ub.setId(6)

    ud = UserDao()
    ud.update(ub)
    print("Data Updated Successfully")
testUpdate()
