# Markdown 语法学习笔记

## 标题
支持两种标题语法，Setext类以及atx类
- Setext类：以底线形式标注一级标题及二级标题
```markdown
this is an H1
==============

this is an H2
---------------
```
- Atx形式：标题行首插入1 到 6个# 对应1-6级标题（#后添加空格）
```markdown
# this is an H1
## this is an H2
###### this is an H6
```

-------------------------------------------
## 字体
- Markdown 以*和_作为强调字符
```markdown
**这是加粗**
__这也是加粗__
*这是倾斜*
_这也是倾斜_
***这是加粗倾斜***
___also___
```

## 分割线
-可以通过三个以上的*或-
```markdown
***
* * *
**********
---
----------------
```

## 引用
引用语句语句前添加“>”即可，换行中间空行
```markdown
>this is quote,
>and continue
>
>next 
```
