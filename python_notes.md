# built-in function
*abs*
```python
a = abs(-1)
b = abs(-1.1)
print('a', a)
print('b', b)
```
return a 

---
# keyword : yield
```python
def func_yield():
    for i in range(4):
        ret = yield i
        print(ret)

func = func_yield()
print('func', next(func)) # print yield return value 0
next(func) # run print(ret), because i return,so ret = None
next(func) # run print(ret), because i return,so ret = None
func.senf(999) # ret = 999, so print 999

# case about range
def my_range(num):
    i = 0
    while i < num:
        yield num
        num += 1

for i in my_range(19):
    print(i)
    

```

---
# standard library : subprocess 
*case 1*
```python
import subprocess

def run_cmd(cmd: str):
    cmd = cmd.split()
    ret = subprocess.run(cmd, capture_output=False).stdout
    return ret
```
in this function, run_cmd().its include a subprocess instance which run the cmd, and return a stdout message if capture_out is Ture

---
# standard library : logging
*case 1*
```python{.line-numbers}
import logging

logging.basicConfig(level=logging.DEBUG, filename='cpu_collect_excel.log', format="%(asctime)s - %(levelname)s - %(message)s")
```
this is a simple usage for a single python file

---
# external library : uiautomator2
**定位元素，进行操作**
```python
import uiautomator2 as u2

d = u2.connect()


```

---
# standard : ftplib

**case1**
```python
import ftplib
ftp_client = ftplib.FTP(host=self.ip, user='root', passwd='111111')
ftp_client.login(user='root', passwd='111111')
```

---
# external : paramiko
```python
import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(self.ip, 22, 'root', '111111', timeout=5, allow_agent=False, look_for_keys=False)

```

# json
```python
import json

json.dump(str, fp)

```
# exit
os._exit(n)会直接将python程序终止，之后的所有代码都不会继续执行。以状态码 n 退出进程，不会调用清理处理程序，不会刷新 stdio，等等。
sys.exit([arg])会引发一个异常：SystemExit，如果这个异常没有被捕获，那么python解释器将会退出。如果有捕获此异常的代码，那么这些代码还是会执行。捕获这个异常可以做一些额外的清理工作。可选参数 arg 可以是表示退出状态的整数（默认为 0），也可以是其他类型的对象。如果它是整数，则 shell 等将 0 视为“成功终止”，非零值视为“异常终止”。大多数系统要求该值的范围是 0–127，否则会产生不确定的结果。