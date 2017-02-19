# encoding=utf8

import top.api
import sys

reload(sys)
sys.setdefaultencoding('utf8')

appkey=''
secret=''
sign=''
msgTemplate=""

"""



"""

def send_mes(tel,json):#有余票了
     req = top.api.AlibabaAliqinFcSmsNumSendRequest()
     req.set_app_info(top.appinfo(appkey,secret))
     req.extend = ""
     req.sms_type = "normal"
     req.sms_free_sign_name = sign
     req.sms_param = json
     req.rec_num = tel
     req.sms_template_code = msgTemplate
     try :
          resp = req.getResponse()
          print (resp)
     except Exception,e:
          print (e)
