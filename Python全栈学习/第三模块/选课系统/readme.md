# 选课系统开发

------

## 1.需求：
角色:学校、学员、课程、讲师
要求:
1. 创建北京、上海 2 所学校
2. 创建linux , python , go 3个课程 ， linux\py 在北京开， go 在上海开
3. 课程包含，周期，价格，通过学校创建课程 
4. 通过学校创建班级， 班级关联课程、讲师
5. 创建学员时，选择学校，关联班级
5. 创建讲师角色时要关联学校， 
6. 提供两个角色接口
6.1 学员视图， 可以注册， 交学费， 选择班级，
6.2 讲师视图， 讲师可管理自己的班级， 上课时选择班级， 查看班级学员列表 ， 修改所管理的学员的成绩 
6.3 管理视图，创建讲师， 创建班级，创建课程

7. 上面的操作产生的数据都通过pickle序列化保存到文件里

## 2.开发思路

> * 系统共涉及五个模块：学校、课程、班级、讲师、学员，每个模块一个class类用来实例化相应数据，并提供简单的数据处理方法，通过学员视图、讲师视图、管理视图三个不同维度对系统数据进行操作。
> * 前期考虑每个模块的数据单独存储，但考虑到相互之间复杂的关联关系，如存取多个数据文件，每次操作均需要频繁读取和写入多个文件，对IO性能上可能会有影响，故设计将数据存储到一个文件中，每次启动系统即将数据一次行读取到内存中，退出系统时再pickle保存到数据文件中。
> * 不同学校的课程、班级、讲师、学员是相对独立存在的，设计时将这些对象数据都直接存储到了学校对象中，便于数据处理。

## 3.数据结构

### 数据存储结构
>* db
{"北京校区":北京校区的school实例,"上海校区":"上海校区的school实例"}
>* school的实例：
{name:北京校区，addr：北京，course：{"python课程"："python课程实例","linux课程"："linux课程实例"}，teacher：{"teacher名称1"："teacher名称1对应的实例"，"teacher名称2"："teacher名称2对应的实例"}，classes：{"classes名称1"："classes名称1对应的实例"，"classes名称2"："classes名称2对应的实例"}，student：{"张同学":"张同学的student的实例"，"于同学":"于同学的student的实例"}}
>* course的实例：
{name:"python课程",period:"培训周期",price:"价格"}
>* teacher的实例：
{name："teacher名称1"，salary:"工资"，skills:"Go,Python,Java等", classes:{"classes名称1"："classes名称1对应的实例","classes名称2"："classes名称2对应的实例"}}
>* classes的实例：
{name: 'python自动化班', course_obj: "课程实例", course_student: ["李同学"，"王同学"],course_score:{"李同学":85,"王同学":90}}
>* student的实例：
{name:"李同学"，age:31，school_name："北京校区"，classes_list:['classes名称1']}

## 4.程序目录结构
选课系统/
├── bin    
│   ├── __init__.py
│   └── startup.py  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-------执行文件
├── conf  
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-36.pyc
│   │   └── settings.cpython-36.pyc
│   └── settings.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-------配置文件
├── controller   
│   ├── base_manager.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-------定义管理系统的父类
│   ├── __init__.py
│   ├── school_manage.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-------学校管理视图
│   ├── student_manage.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-------学生管理视图
│   └── teacher_manage.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-------教师管理视图
├── core
│   ├── __init__.py
│   ├── main.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-------主方法文件
├── db
│   ├── __init__.py
│   ├── school.dat&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-------数据文件
│   └── 初始化数据.py&nbsp;&nbsp;&nbsp;&nbsp;-------初始化数据文件
├── __init__.py
├── modules
│   ├── classes.py &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-------班级类
│   ├── course.py  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-------课程类
│   ├── __init__.py
│   ├── school.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-------学校类
│   ├── student.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-------学生类
│   └── teacher.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-------讲师类
└── readme.md