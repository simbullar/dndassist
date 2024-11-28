import login
from variables import *

name_returned = login.login(layoutRegister=layoutRegister, key=key, layoutLogin=layoutLogin, layoutPopup=layoutPopup)

if name_returned == 'simbullar':
    print("first account") 