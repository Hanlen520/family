from iSoft import app, auth
from iSoft.entity.role import RoleDal
import json
from iSoft.core.Fun import Fun
from iSoft.core.model.AppReturnDTO import AppReturnDTO

@app.route('/role/all')
def all():
    ent=RoleDal.GetAll()
    reEnt= AppReturnDTO(True, "登录成功", ent, "token")
    
    print(reEnt)
    return json.dumps(Fun.convert_to_dict(reEnt), ensure_ascii=False)