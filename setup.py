#!/usr/bin/python
import os, subprocess, sys
#subprocess.call(['python3:', 'virtualenv.py', 'flask'])
#if sys.platform == 'win32':
#    bin = 'Scripts'
#else:
subprocess.call(['pip', 'install', 'flask'])
subprocess.call(['pip', 'install', 'flask-login'])
subprocess.call(['pip', 'install', 'flask-openid'])
subprocess.call(['pip', 'install', 'flask-mail'])
subprocess.call(['pip', 'install', 'sqlalchemy'])
subprocess.call(['pip', 'install', 'flask-sqlalchemy'])
subprocess.call(['pip', 'install', 'sqlalchemy-migrate'])
subprocess.call(['pip', 'install', 'flask-whooshalchemy'])
subprocess.call(['pip', 'install', 'flask-wtf'])
subprocess.call(['pip', 'install', 'flask-babel'])
subprocess.call(['pip', 'install', 'flask-cors'])
subprocess.call(['pip', 'install', 'Flask-HTTPAuth'])
#subprocess.call(['pip', 'install', 'flup'])
