# Windows_User_Contol
共享机开户系统<br>
作用:有一些组织可能会需要一个操控系统,来创建用户.<br>
所以此系统将为他们提供接口支持<br>
用到的PIP支持库:<br>
flask<br>
datetime<br>
os<br>
HTTP[GET]所需要参数:<br>
mode   指定模式,支持:[getkey,add,change,del,ban,unban,check]<br>
qq   注册时QQ<br>
user  rdp用户名<br>
pwd  rdp密码<br>
npwd  更改密码时新密码<br>
key  敏感操作时校验的动态密钥<br>
鸣谢:<br>
Flask支持库:提供WebAPI<br>
许可协议: 本源码许可协议为Apache License<br>
