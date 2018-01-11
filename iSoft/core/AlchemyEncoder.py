#!~\app\core\AlchemyEncoder.py
#
'''
class转JSON
'''

# from flask import json
import json
import datetime
import decimal
from sqlalchemy.ext.declarative import DeclarativeMeta
from iSoft.core.Fun import Fun 

class AlchemyEncoder(json.JSONEncoder):
    '''用于把实体类换成JSON'''
    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'parent' and x != 'metadata' and x != "query" and x != "query_class"]:
                data = obj.__getattribute__(field)
 
                if data!=None and data !='':
                    try:
                        if hasattr(data,"__dict__"):
                            break
                        elif isinstance(data, decimal.Decimal):
                            fields[field] = float(data)
                        elif isinstance(data, datetime.datetime):
                            fields[field] = data.strftime("%Y-%m-%d %H:%M") 
                        elif isinstance(data, datetime.date):
                            fields[field] = data.strftime("%Y-%m-%d") 
                        elif isinstance(data, datetime.timedelta):
                            fields[field] = (datetime.datetime.min + data).time().isoformat()
                        else:
                            json.dumps(data)     # this will fail on non-encodable values, like other classes
                            fields[field] = data
                    except TypeError:    # 添加了对datetime的处理
                            fields[field] = None
            # a json-encodable dict
            return fields
        return json.JSONEncoder.default(self, obj)