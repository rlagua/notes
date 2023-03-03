# subproZZss_module_study
------------------------------------------------------------------------------
*case 1*
```python
import subprocess

def run_cmd(cmd: str):
    cmd = cmd.split()
    ret = subprocess.run(cmd, capture_output=False).stdout
    return ret
```
in this function, run_cmd().its include a subprocess instance which run the cmd, and return a stdout message if capture_out is Ture


