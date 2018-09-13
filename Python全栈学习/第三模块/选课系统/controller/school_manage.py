#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/11 22:47



from controller.base_manager import Base
from modules.school import School
class SchoolManage(Base):
    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            # print(self.db) # {'Oldboy北京校区': <modules.school.School object at 0x000002984B56B668>, 'Oldboy上海校区': <modules.school.School object at 0x000002984B69CDD8>}
            # 显示已有学校
            schools = []
            for key in self.db:
                print("学校名称：【%s】  所在城市：【%s】" % (key, self.db[key].addr))
                schools.append(key)
            # print("\033[32m添加学校,输入#\033[5m")
            school_choise = input("输入需要管理的学校名称,b.返回上一层>>:").strip()
            # if school_choise == "#":
            #     self.add_school()
            if school_choise in schools:
                self.school_choise = school_choise  # 学校名称
                self.sch_obj = self.db[school_choise]  # 获取学校实例 {'name': '北京', 'addr': '北京市', 'course': {}, 'teacher': {}, 'classes': {}}
                # 管理员管理操作执行，字典操作
                msg = """
                ---%s-学校管理系统---
                      1.添加课程
                      2.添加班级
                      3.添加老师
                      4.查看课程
                      5.查看班级
                      6.查看老师
                      b.返回上一层
                      q.退出程序 
                """
                operation_list = {
                    "1": self.add_course,
                    "2": self.add_classes,
                    "3": self.add_teacher,
                    "4": self.check_course,
                    "5": self.check_classes,
                    "6": self.check_teacher,
                    "q": self.logout
                }
                while True:
                    print(msg % self.sch_obj.name)
                    oper_id = input("输入操作项序号:>>").strip()
                    if oper_id in operation_list:
                        operation_list[oper_id]()
                    elif oper_id == "b":
                        break
                    else:
                        print("输入有误，请重新输入！")
            elif school_choise == "b":
                break
            else:
                print("学校名称错误，请重新输入！")

    def add_course(self):
        # print(self.sch_obj.course)
        course_name = input("输入课程名称:>>").strip()
        course_period = input("输入该课程的周期(月):>>").strip()
        course_price = input("输入该课程的价格(元):>>").strip()
        if course_name not in self.sch_obj.course:
            self.sch_obj.create_course(course_name, course_period, course_price)
            self.db[self.school_choise] = self.sch_obj
            print("【%s】课程创建成功！" % course_name)
        else:
            print("课程【%s】已经存在！" % course_name)

    def add_classes(self):
        # print(self.sch_obj.classes)
        # print(self.sch_obj.course)
        sch_course = self.sch_obj.course
        classes_name = input("输入班级名称:>>").strip()
        course_name = input("输入课程名字:>>").strip()
        if classes_name not in self.sch_obj.classes:
            if sch_course:
                if course_name in sch_course:
                    course_obj = sch_course[course_name]
                    self.sch_obj.create_classes(classes_name, course_obj)
                    self.db[self.school_choise] = self.sch_obj
                    print("【%s】班级创建成功！" % classes_name)
                else:
                    print("该课程不存在,请创建该课程")
        else:
            print("班级【%s】已经存在！" % classes_name)

    def add_teacher(self):
        # print(self.sch_obj.teacher)
        teacher_name = input("输入老师名字:>>").strip()
        teacher_salary = input("薪水(元):>>").strip()
        skills = input("请输入老师技能：").strip()
        classes_name = input("输入授课班级名称:").strip()
        if teacher_name not in self.sch_obj.teacher:
            if classes_name in self.sch_obj.classes:
                self.sch_obj.create_teacher(teacher_name, teacher_salary, skills, classes_name, self.school_choise)
                # self.db[self.school_choise] = self.sch_obj
                print("【%s】老师新增成功！\n" % teacher_name)
            else:
                print("输入班级不存在！")
        else:
            print("该老师已经存！")


if __name__ == "__main__":
    pass