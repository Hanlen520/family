# file: login.py
'''首页'''
from iSoft.core.Fun import Fun
from iSoft import auth, login_manager, app
from flask import request, flash, g
from iSoft.dal.UserDal import UserDal
from flask_login import (LoginManager, login_required, login_user,
                         current_user, logout_user, UserMixin)
import iSoft.entity.model
from iSoft.model.AppReturnDTO import AppReturnDTO
from iSoft.core.AlchemyEncoder import AlchemyEncoder
import json


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    '''退出登录'''
    re_ent = UserDal.login_out()
    return json.dumps(Fun.convert_to_dict(re_ent))


@app.route('/auth/UserLogin', methods=['GET', 'POST'])
def user_login():
    '''用户登录'''
    j_data = request.json 
    if j_data is None:
        return Fun.class_to_JsonStr(AppReturnDTO(False, "参数有误"))

    ent = UserDal.user_login(j_data)
    return Fun.class_to_JsonStr(ent)


@app.route('/auth/UserReg', methods=['GET', 'POST'])
def user_reg():
    '''用户注册'''
    j_data = request.json 
    if j_data is None:
        return Fun.class_to_JsonStr(AppReturnDTO(False, "参数有误"))

    ent = UserDal.login_reg(j_data)

    print(ent.__dict__)
    # return json.dumps(ent, cls=AlchemyEncoder)
    return json.dumps(Fun.convert_to_dict(ent), ensure_ascii=False)