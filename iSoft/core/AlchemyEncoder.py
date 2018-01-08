#!~\app\core\AlchemyEncoder.py
#
'''
class转JSON
'''

# from flask import json
import json
import datetime
from sqlalchemy.ext.declarative import DeclarativeMeta
class AlchemyEncoder(json.JSONEncoder):
    '''用于把实体类换成JSON'''
    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
 
                if data!=None and data !='' and field != "query" and field != "query_class":
                    try:
                        json.dumps(data)     # this will fail on non-encodable values, like other classes
                        fields[field] = data
                    except TypeError:    # 添加了对datetime的处理
                        if isinstance(data, datetime.datetime):
                            fields[field] = data.isoformat()
                        elif isinstance(data, datetime.date):
                            fields[field] = data.isoformat()
                        elif isinstance(data, datetime.timedelta):
                            fields[field] = (datetime.datetime.min + data).time().isoformat()
                        else:
                            fields[field] = None
            # a json-encodable dict
            return fields
        return json.JSONEncoder.default(self, obj)