# Windows_User_Contol
共享机开户系统
作用:有一些组织可能会需要一个操控系统,来创建用户.
所以此系统将为他们提供接口支持
用到的PIP支持库:
flask
datetime
os
HTTP[GET]所需要参数:
mode   指定模式,支持:[getkey,add,change,del,ban,unban,check]
qq   注册时QQ
user  rdp用户名
pwd  rdp密码
npwd  更改密码时新密码
key  敏感操作时校验的动态密钥
鸣谢:
Flask支持库:提供WebAPI
许可协议: 本源码许可协议为Apache License
