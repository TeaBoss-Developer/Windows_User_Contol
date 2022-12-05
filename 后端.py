import os
from flask import Flask,request
from datetime import datetime
from Method import Method
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_MIMETYPE'] = "application/json;charset=utf-8"
@app.route('/', methods=['GET'])
def home():
    mode = str(request.args.get("mode"))
    qq = str(request.args.get("qq"))
    user = str(request.args.get("user"))
    pwd = str(request.args.get("pwd"))
    npwd = str(request.args.get("npwd"))
    dkey = str(request.args.get("key"))
    if(mode == "getkey"):
        array_datetime = str(datetime.now()).split(" ")[0].split("-");
        strs = str(int(array_datetime[0])*1.5).replace('.','')+str(int(array_datetime[1])*5)+str(int(array_datetime[2])*8)+str(int(gethour())*4)
        return(strs)
    if(user == "Administrator" or user == "administrator"):
        return("权限错误,请检查用户名是否为管理用户名.")
    if(mode == "add"):#添加用户
        if(dkey == key()):
            fp = str(os.popen("net user "+user+" "+pwd+" /add","r").read())
            os.system("net localgroup administrators "+user+" /add")
            Method.WriteIni(Method.RunPath()+"\\User.ini",user,"Owner",qq)
            Method.WriteIni(Method.RunPath()+"\\User.ini",user,"Password",pwd)
            return(fp)
    if(mode == "change"):#更改用户密码
        if(dkey == key()):
            if(pwd == Method.ReadIni(Method.RunPath()+"\\User.ini",user,"Password",)):
                Method.WriteIni(Method.RunPath()+"\\User.ini",user,"Password",npwd)
                fp = str(os.popen("net user "+user+" "+npwd,"r").read())
                return(fp)
    if(mode == "del"):#删除用户
        if(dkey == key()):
            fp = str(os.popen("net user "+user+" /del","r").read())
            Method.WriteIni(Method.RunPath()+"\\User.ini",user,"Deleted?","Yes")
            return(fp)
    if(mode == "ban"):#封禁用户
        if(dkey == key()):
            fp = str(os.popen("net user "+user+" /active:no","r").read())
            Method.WriteIni(Method.RunPath()+"\\User.ini",user,"Baned?","Yes")
            return(fp)
    if(mode == "unban"):#解封用户
        if(dkey == key()):
            fp = str(os.popen("net user "+user+" /active:y","r").read())
            Method.WriteIni(Method.RunPath()+"\\User.ini",user,"Baned?","Yes")
            return(fp)
    if(mode == "check"):#检查用户是否存在
        if(dkey == key()):
            fp = str(os.popen("net user "+user,"r").read())
            if("找不到用户名" in fp):
                return("False")
def key():
    array_datetime = str(datetime.now()).split(" ")[0].split("-");
    strs = str(int(array_datetime[0])*1.5).replace('.','')+str(int(array_datetime[1])*5)+str(int(array_datetime[2])*8)+str(int(gethour())*4)
    return(strs)
def gethour():
    return(str(datetime.now()).split(":")[0].split("-")[2].split(" ")[1])
if __name__ == '__main__':

    app.run(host="0.0.0.0", port=2220)