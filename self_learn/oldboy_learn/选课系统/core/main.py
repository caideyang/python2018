#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/11 22:05

# main
import shelve, os, sys, time
from config import settings
from module.school import school


# 启动Home
class home:

    # 显示登录页面项目
    @classmethod
    def show_home(cls):
        home = {
            '1': manage_student,
            '2': manage_teacher,
            '3': manage_school,
            'q': exit
        }
        while True:
            print("\n\033[1m\033[36m社会大学选课系统\n\033[0m"
                  "\033[4m1.学生视图\n\033[0m"
                  "\033[4m2.老师视图\n\033[0m"
                  "\033[4m3.管理员视图\n\033[0m"
                  "\033[4mq.退出系统\n\033[0m")
            inp = input("\033[34;0m输入访问页面id >>:\033[0m").strip()
            if inp in home:
                obj = home[inp]
                obj()  # 执行功能
            else:
                print("\033[31m输入有误！请重新输入\033[0m")
                continue


# 管理员创建学校，创建课程，创建老师，创建班级，创建学员,及查询信息信息功能
class manage_school:

    def __init__(self):
        if os.path.exists(settings.school_db + ".dat"):
            self.school_db = shelve.open(settings.school_db)
            self.run_manage()
            self.school_db.close()
        else:
            print("初始化系统信息....")
            self.initialize_school()
            self.run_manage()
            self.school_db.close()

    def initialize_school(self):  # 预设创建两所学校
        self.school_db = shelve.open(settings.school_db)
        sh = school("上海", "上海市")
        bj = school("北京", "北京市")
        self.school_db["北京"] = bj
        self.school_db["上海"] = sh
        # self.school_db.close() 初始化后不需要关闭，run_manage()运行操作

    def run_manage(self):

        while True:
            # 显示已有学校
            schs = []
            for key in self.school_db:
                print("名称：%s  坐标：%s" % (key, self.school_db[key].addr))
                schs.append(key)
            print("\033[32m添加学校,输入#\033[5m")
            sch = input("\033[34;0m输入需要管理的学校名称,b.返回上一层>>:\033[0m").strip()
            if sch == "#":
                self.add_school()
            elif sch in schs:
                self.sch = sch  # 学校名称
                self.sch_obj = self.school_db[
                    sch]  # 获取学校实例 {'name': '北京', 'addr': '北京市', 'course': {}, 'teacher': {}, 'classes': {}}
                # print(self.sch_obj.__dict__)
                # 管理员管理操作执行，字典操作
                while True:
                    print("\033[32m\n社会大学%s校区管理后台\n\033[4m"
                          "\033[4m1.添加课程 \n\033[0m"
                          "\033[4m2.添加班级 \n\033[0m"
                          "\033[4m3.添加老师 \n\033[0m"
                          "\033[4m4.查看课程 \n\033[0m"
                          "\033[4m5.查看班级 \n\033[0m"
                          "\033[4m6.查看老师 \n\033[0m"
                          "\033[4mb.返回上一层\n\033[0m"
                          "\033[4mq.退出程序 \n\033[0m" % self.sch_obj.name
                          )

                    operation_items = {
                        "1": self.add_course,
                        "2": self.add_classes,
                        "3": self.add_teacher,
                        "4": self.check_course,
                        "5": self.check_classes,
                        "6": self.check_teacher,
                        "q": exit
                    }
                    oper_id = input("\033[34;0m输入操作项序号:>>\033[0m").strip()
                    if oper_id in operation_items:
                        func = operation_items[oper_id]
                        func()
                    elif oper_id == "b":
                        break
                    else:
                        print("\033[31m输入有误，请重新输入！\033[0m")
            elif sch == "b":
                break
            else:
                print("\033[31m学校名称错误，请重新输入！\033[4m")

    def add_school(self):
        sch_name = input("输入学校名称:>>").strip()
        sch_addr = input("输入学校坐标:>>").strip()
        if sch_name not in self.school_db:
            self.school_db[sch_name] = school(sch_name, sch_addr)
            print("\033[36m【%s】校区创建成功！\n\033[0m" % sch_name)
        else:
            print("\033[31m【%s】学校已经存在！\n\033[4m" % sch_name)

    def add_course(self):
        course_name = input("输入课程名称:>>").strip()
        course_period = input("输入该课程的周期(月):>>").strip()
        course_price = input("输入该课程的价格(元):>>").strip()
        self.sch_obj.create_course(course_name, course_period, course_price)
        self.school_db[self.sch] = self.sch_obj
        print("\033[36m【%s】课程创建成功！\n\033[0m" % course_name)

    def add_classes(self):
        sch_course = self.sch_obj.course
        classes_id = input("输入班级名称:>>").strip()
        course_name = input("输入课程名字:>>").strip()
        if sch_course:
            if course_name in sch_course:
                course_obj = sch_course[course_name]
                self.sch_obj.create_classes(classes_id, course_obj)
                self.school_db[self.sch] = self.sch_obj
                print("\033[36m【%s】班级创建成功！\n\033[0m" % classes_id)
            else:
                print("\033[31m该课程不存在,请创建该课程\033[4m")

    def add_teacher(self):
        teacher_name = input("输入老师名字:>>").strip()
        teacher_salary = input("薪水(元):>>").strip()
        classes_id = input("输入授课班级名称:").strip()
        if teacher_name not in self.sch_obj.teacher:
            if classes_id in self.sch_obj.classes:
                self.sch_obj.create_teacher(teacher_name, teacher_salary, classes_id)
                self.school_db[self.sch] = self.sch_obj
                print("\033[36m【%s】老师新增成功！\n\033[0m" % teacher_name)
            else:
                print("\033[31m输入班级不存在！\033[0m")
        else:
            print("\033[31m该老师已经存！\033[0m")

    def check_course(self):
        if not self.sch_obj.course:
            print("\033[31m当前无课程！\033[0m")
        else:
            print("\033[42m所有课程信息:\033[0m")
            for key in self.sch_obj.course:
                course_obj = self.sch_obj.course[key]
                print("课程：%s, 周期: %s月, 价格: %s元 " % (course_obj.name, course_obj.period, course_obj.price))

    def check_teacher(self):
        if not self.sch_obj.teacher:
            print("\033[31m当前无讲师！请添加！\033[0m")
        else:
            print("\033[42m所有老师信息:\033[0m")
            for key in self.sch_obj.teacher:
                teacher_obj = self.sch_obj.teacher[key]
                teacher_classes_list = []
                for key2 in teacher_obj.classes:
                    d = {}
                    classes_obj = teacher_obj.classes[key2]
                    course_name = classes_obj.course.name
                    d[key2] = course_name
                    teacher_classes_list.append(d)
                print("姓名：%s, 薪水：%s块/月，授课班级及对应课程: %s" % (teacher_obj.name, teacher_obj.salary, teacher_classes_list))

    # 当前班级信息
    def check_classes(self):
        if not self.sch_obj.classes:
            print("\033[31m当前无班级，请创建班级！\033[4m")
        else:
            print("\033[42m所有班级信息:\033[0m")
            for key in self.sch_obj.classes:
                classes_obj = self.sch_obj.classes[key]
                for key2 in self.sch_obj.teacher:
                    teacher_obj = self.sch_obj.teacher[key2]
                    for key3 in teacher_obj.classes:
                        if classes_obj.id == teacher_obj.classes[key3].id:
                            print("班级:%s,关联课程：%s，周期:%s月,价格:%s,授课老师:%s" % (
                            classes_obj.id, classes_obj.course.name, classes_obj.course.period,
                            classes_obj.course.price, teacher_obj.name))
                            break
                        else:
                            continue


# 学员视图，学员选择班级，学院缴费，学院注册
class manage_student:
    def __init__(self):
        if os.path.exists(settings.school_db + ".dat"):
            self.school_db = shelve.open(settings.school_db)
            self.run_manage_student()
            self.school_db.close()
        else:
            print("\033[31m系统管理员还未创建相应的学校，课程，老师，请联系系统管理员！\033[0m")

    # 学员注册，选课一起进行
    def regist_student(self):

        print("\n\033[34m当前校区开设课程:\33[0m")
        for key in self.sch_obj.classes:
            classes_obj = self.sch_obj.classes[key]
            course_obj = classes_obj.course
            print("班级:%s,课程:%s,周期:%s,价格:%s" % (key, course_obj.name, course_obj.period, course_obj.price))
        student_name = input("姓名:>>").strip()
        student_age = input("年龄:>>").strip()
        classes_id = input("选择需要培训的课程对应的班级:>>").strip()
        if classes_id in self.sch_obj.classes:
            classes_obj = self.sch_obj.classes[classes_id]
            self.sch_obj.create_student(student_name, student_age, classes_obj.id)
            self.school_db[self.sch] = self.sch_obj
            # 提示注册成功后显示课程信息
            print("恭喜%s学员注册成功!\n课程信息:%s,周期:%s,价格:%s" % (
            student_name, classes_obj.course.name, classes_obj.course.period, classes_obj.course.price))
        else:
            print("\033[31m班级输入错误！\033[0m")

    # 查看学员信息
    def check_student(self):
        student_name = input("\033[34;0m输入要查看的学员名字:\033[0m>>").strip()
        print("该学员信息:")
        for key in self.sch_obj.classes:
            classes_obj = self.sch_obj.classes[key]
            if student_name in classes_obj.course_student:
                for key2 in classes_obj.course_student:
                    if key2 == student_name:
                        classes_id = classes_obj.id
                        coures_name = classes_obj.course.name
                        course_period = classes_obj.course.period
                        course_price = classes_obj.course.price
                        for key4 in self.sch_obj.teacher:
                            for key3 in self.sch_obj.teacher[key4].classes:
                                if key3 == classes_id:
                                    classes_teacher = self.sch_obj.teacher[key4].name
                                    print("\033[34m学员: %s\n班级: %s\n授课老师: %s\n课程: %s, 周期: %s月, 价格: %s元\033[0m" % (
                                    student_name, classes_id, classes_teacher, coures_name, course_period,
                                    course_price))
                break
        else:
            print("\033[31m无该学员！\033[0m")

    def run_manage_student(self):
        while True:
            # 显示已有学校
            schs = []
            print("\n\033[34m所有校区:\033[0m")
            for key in self.school_db:
                print("校名：%s        位置:%s" % (key, self.school_db[key].addr))
                schs.append(key)
            # print("\033[32m添加学校,输入#\033[5m")
            sch = input("\033[34;0m选择注册校区(b.返回上一层)>>:\033[0m").strip()
            if sch in schs:
                self.sch = sch  # 学校名称
                self.sch_obj = self.school_db[
                    sch]  # 获取学校实例 {'name': '北京', 'addr': '北京市', 'course': {}, 'teacher': {}, 'classes': {}}
                # print(self.sch_obj.__dict__)
                operation_items = {
                    "1": self.regist_student,
                    "2": self.check_student,
                    "q": exit
                }
                while True:
                    print("\033[32m选择操作项>\n\033[0m"
                          "\033[4m1.注册成为学员\n\033[0m"
                          "\033[4m2.查看学员信息\n\033[0m"
                          "\033[4mb.返回上一层\n\033[0m"
                          "\033[4mq.退出程序\n\033[0m")
                    oper = input("输入操作对应序号:>>").strip()
                    if oper in operation_items:
                        func = operation_items[oper]
                        func()
                    elif oper == "b":
                        break
                    else:
                        print("\033[31m输入有误，请重新输入！\033[0m")

            elif sch == "b":
                break
            else:
                print("\033[31m输入有误，请重新输入！\033[0m")
                continue


class manage_teacher:
    def __init__(self):
        if os.path.exists(settings.school_db + ".dat"):
            self.school_db = shelve.open(settings.school_db)
            self.run_manage_teacher()
            self.school_db.close()
        else:
            print("请创建相应学校课程班级！")
            exit()

    def run_manage_teacher(self):
        while True:
            # 显示已有学校
            schs = []
            print("\n\033[34m所有校区:\033[0m")
            for key in self.school_db:
                print("校名：%s      位置: %s" % (key, self.school_db[key].addr))
                schs.append(key)
            # print("\033[32m添加学校,输入#\033[5m")
            sch = input("\033[34;0m选择校区(b.返回上一层)>>:\033[0m").strip()
            if sch in schs:
                self.sch = sch  # 学校名称
                self.sch_obj = self.school_db[
                    sch]  # 获取学校实例 {'name': '北京', 'addr': '北京市', 'course': {}, 'teacher': {}, 'classes': {}}
                # print(self.sch_obj.__dict__)
                operation_items = {
                    "1": self.check_teacher_classes,
                    "q": exit
                }
                while True:
                    print("\033[32m选择操作项>\n\033[0m"
                          "\033[4m1.查看授课班级信息\n\033[0m"
                          "\033[4mb.返回上一层\n\033[0m"
                          "\033[4mq.退出程序\n\033[0m"
                          )
                    oper = input("\033[34;0m输入操作项序号>>:\033[0m")
                    if oper in operation_items:
                        func = operation_items[oper]
                        func()
                    elif oper == "b":
                        break
                    else:
                        print("\033[31m输入有误，请重新输入！\033[0m")
            elif sch == "q":
                break
            else:
                print("\033[31m输入有误，请重新输入！\033[0m")

    # 查看该老师名下的班级信息
    def check_teacher_classes(self):
        teacher_name = input("\033[34;0m输入老师名字>>:\033[0m")
        print("\n\033[34m%s老师授课班级信息如下:\033[0m" % teacher_name)
        if teacher_name in self.sch_obj.teacher:
            teacher_obj = self.sch_obj.teacher[teacher_name]
            for key in teacher_obj.classes:
                classes_obj = teacher_obj.classes[key]
                classes_name = classes_obj.id
                course_name = classes_obj.course.name
                student = []
                for key2 in classes_obj.course_student:
                    student_obj = classes_obj.course_student[key2]
                    student_name = student_obj.name
                    student.append(student_name)
                print("班级%s，课程: %s\n学员:%s\n" % (classes_name, course_name, student))
        else:
            print("\033[31m暂无该【%s】老师信息！\n\033[0m" % teacher_name)


if __name__ == "__main__":
    home().show_home()

if __name__ == "__main__":
    pass