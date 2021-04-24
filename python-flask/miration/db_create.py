from library.DAL.models import *
from library.controllers import loadAndInsertData, insertCategories, initAdminAccount, initRoles

db.create_all()
loadAndInsertData()
insertCategories()
initRoles()
initAdminAccount()
