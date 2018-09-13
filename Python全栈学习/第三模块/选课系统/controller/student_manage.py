#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/11 22:47

from controller.base_manager import Base
from modules.student import Student
class StudentManage(Base):
    def __init__(self):
        super().__init__()
        # self.run()
    def run(self):
        while True:
            # print(self.db) # {'Oldboy北京校区': <modules.school.School object at 0x000002984B56B668>, 'Oldboy上海校区': <modules.school.School object at 0x000002984B69CDD8>}
            schools = []
            for key in self.db:
                print("学校名称：【%s】  所在城市：【%s】" % (key, self.db[key].addr))
                schools.append(key)
            # print("\033[32m添加学校,输入#\033[5m")
            school_choise = input("输入需要进入的学校名称,b.返回上一层>>:").strip()
            # if school_choise == "#":
            #     self.add_school()
            if school_choise in schools:
                self.school_choise = school_choise  # 学校名称
                self.sch_obj = self.db[school_choise]  # 获取学校实例 {'name': '北京', 'addr': '北京市', 'course': {}, 'teacher': {}, 'classes': {}}
                # 管理员管理操作执行，字典操作
                msg = """
                ---%s-学生管理系统---
                      1.学生注册
                      2.选课缴费
                      3.学生信息查询
                      b.返回上一层
                      q.退出程序 
                """
                operation_list = {
                    "1": self.add_student,
                    "2": self.choice_classes,
                    "3": self.check_student,
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

    def add_student(self):
        name = input("请输入学生姓名： ").strip()
        age = input("请输入学生年龄: ").strip()
        school_name = self.school_choise
        # print(self.db[self.school_choise].__dict__)
        if name not in self.sch_obj.student:
            new_student = Student(name, age, school_name)
            self.sch_obj.student[name] = new_student
            print("注册新学员【%s】成功！" % name)
        else:
            print("姓名【%s】已存在！" % name )

    def choice_classes(self):

        # print(self.sch_obj.__dict__)
        course_list = []
        if self.sch_obj.classes:
            stu_name = input("请输入要选课的学员名字: ").strip()
            if stu_name in self.sch_obj.student: # 判断该学员是否注册
                self.check_classes()
                classes_name = input("请输入要选的课程对应的班级名称： ").strip()
                if classes_name in self.sch_obj.classes:  # 判断是否有该课程
                    # print(self.sch_obj.classes[classes_name].course_student)
                    if classes_name not in self.sch_obj.student[stu_name].classes_list:
                        self.sch_obj.student[stu_name].classes_list.append(classes_name)
                        # print(self.sch_obj.classes[classes_name].course_student)
                        self.sch_obj.classes[classes_name].course_student.append(stu_name)
                        self.sch_obj.classes[classes_name].course_score[stu_name] = 0
                        print("选课成功")
                    else:
                        print("学员已经在该班级")
                else:
                    print("无该课程！")
            else:
                print("系统中无该学员信息，需重新注册！")
        else:
            print("学校暂无可报名班级！")


    # def choice_classes(self):
    #     pass

    def check_student(self):
        # print(self.sch_obj.student)  # {'蔡德阳': <modules.student.Student object at 0x000001FD52DD1128>, '蔡先生': <modules.student.Student object at 0x000001FD52DD1978>, '周同学': <modules.student.Student object at 0x000001FD52DBAF98>}
        stu_name = input("请输入要查看的学生姓名：").strip()
        if stu_name in self.sch_obj.student:
            # print(self.sch_obj.student)
            stu_age = self.sch_obj.student[stu_name].age
            print("学员：【%s】 年龄：【%s】,学习信息如下：" %( stu_name, stu_age))
            # print(self.sch_obj.student[stu_name])
            if self.sch_obj.student[stu_name].classes_list:
                for classes_name in self.sch_obj.student[stu_name].classes_list:
                    classes_obj = self.sch_obj.classes[classes_name]
                    course_name = classes_obj.course_obj.name
                    if stu_name in classes_obj.course_score:
                        classes_score = classes_obj.course_score[stu_name]
                    else:
                        classes_score = 0
                    stu_teacher = None
                    for teacher_name in self.sch_obj.teacher:
                        teacher_obj = self.sch_obj.teacher[teacher_name]
                        if classes_name in teacher_obj.classes:
                            stu_teacher = teacher_name

                    print("班级：【%s】 课程: 【%s】 分数: 【%s】  讲师： 【%s】 " %(classes_name, course_name, classes_score, stu_teacher or "未分配"))

            else:
                print("【未选择任何课程】")
        else:
            print("要查看的学生不存在！")
    # def check_classes(self):
    #     pass

    # def check_teacher(self):
    #     pass


if __name__ == "__main__":
    pass