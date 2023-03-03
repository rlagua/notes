# pytest note

## Get Started

- install
```txt
pip install -U pytest
```
-----------------
## pytest simple param
- -v 显示测试的详细参数信息
- -s 显示测试的输出信息
- vs：这两个参数一起用
- n：支持多线程或者分布式运行测试用例。
- -x：表示只要要一个用例报错，那么测试停止。
- –maxfail=2 出现两个用例失败就停止。
- k：根据测试用例的部分字符串指定测试用例。 如：pytest -vs ./testcase -k “ao”

## pytest mark
- pytest --markers	#可以查看到刚刚定义的标记
- pytest	-m hello   #可以运行test_one用例
- pytest -m "not hello"	#运行不包含hello标记的用例
- pytest 	-m webtest  # 可运行TestMyClass 类下的全部用例

## pytest.ini setting
- addopts = -vs #命令行的参数，用空格分隔
- testpaths = ./testcase #测试用例的路径
- python_files = test_*.py #模块名的规则
- python_classes = Test* #类名的规则
- python_functions = test #方法名的规则
- markers = smoke: 冒烟用例
- usermanage:用户管理模块
- productmanage:商品管理模块

## write hook function
```python
def pytest_collection_modifyitems(config, items):
    # called after collection is completed
    # you can modify the ``items`` list
    ...

import pytest


@pytest.hookimpl(hookwrapper=True)
def pytest_pyfunc_call(pyfuncitem):
    do_something_before_next_hook_executes()

    outcome = yield
    # outcome.excinfo may be None or a (cls, val, tb) tuple

    res = outcome.get_result()  # will raise if outcome was exception

    post_process_result(res)

    outcome.force_result(new_res)  # to override the return value to the plugin system

```
```markdown
root
└── pytest_cmdline_main
    ├── pytest_plugin_registered
    ├── pytest_configure
    │   └── pytest_plugin_registered
    ├── pytest_sessionstart
    │   ├── pytest_plugin_registered
    │   └── pytest_report_header
    ├── pytest_collection
    │   ├── pytest_collectstart
    │   ├── pytest_make_collect_report
    │   │   ├── pytest_collect_file
    │   │   │   └── pytest_pycollect_makemodule
    │   │   └── pytest_pycollect_makeitem
    │   │       └── pytest_generate_tests
    │   │           └── pytest_make_parametrize_id
    │   ├── pytest_collectreport
    │   ├── pytest_itemcollected
    │   ├── pytest_collection_modifyitems
    │   └── pytest_collection_finish
    │       └── pytest_report_collectionfinish
    ├── pytest_runtestloop
    │   └── pytest_runtest_protocol
    │       ├── pytest_runtest_logstart
    │       ├── pytest_runtest_setup
    │       │   └── pytest_fixture_setup
    │       ├── pytest_runtest_makereport
    │       ├── pytest_runtest_logreport
    │       │   └── pytest_report_teststatus
    │       ├── pytest_runtest_call
    │       │   └── pytest_pyfunc_call
    │       ├── pytest_runtest_teardown
    │       │   └── pytest_fixture_post_finalizer
    │       └── pytest_runtest_logfinish
    ├── pytest_sessionfinish
    │   └── pytest_terminal_summary
    └── pytest_unconfigure

```
