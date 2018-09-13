#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/11 22:47


from controller.base_manager import Base

class TeacherManage(Base):
    def __init__(self):
        super().__init__()
    # def run(self):
    #     print("This is TeacherManager class !")
    #     print(self.db)

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
                ---%s-教师管理系统---
                      1.班级管理
                      2.讲师管理
                      3.班级分配
                      4.班级学生查询
                      5.学员成绩管理
                      b.返回上一层
                      q.退出程序 
                """
                operation_list = {
                    "1": self.manage_classes,
                    "2": self.manage_teacher,
                    "3": self.assign_classes,
                    "4": self.check_classes_student,
                    "5": self.manage_students_score,
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

    def manage_classes(self, name=None):
        teacher_name = name or input("请输入讲师姓名：").strip()
        print(self.sch_obj)
        if teacher_name in self.sch_obj.teacher:
            teacher_obj = self.sch_obj.teacher[teacher_name]
            print("讲师【%s】讲授的班级如下： ")
            for classes_name in teacher_obj.classes:
                # print(teacher_obj.classes[classes_name].__dict__)
                course_obj = teacher_obj.classes[classes_name].course_obj
                # print(course_obj.__dict__)
                print("班级：【%s】 课程：【%s】 周期：【%s】月" % (classes_name, course_obj.name, course_obj.period))

            # print(teacher_obj.__dict__)
        else:
            print("未找到对应的讲师！")
    def manage_teacher(self):
        self.sch_obj.show_teacher()

    def assign_classes(self):
        self.check_classes()
        classes_name = input("请输入要分配的班级名称：").strip()
        teacher_name = input("请输入要分配的讲师姓名：").strip()
        if classes_name in self.unassigned_classes:
            classes_obj = self.sch_obj.classes[classes_name]
            if teacher_name in self.sch_obj.teacher:
                self.sch_obj.teacher[teacher_name].add_classes(classes_name,classes_obj)
                print("班级【%s】分配讲师【%s】成功！" %(classes_name, teacher_name))
            else:
                print("讲师姓名输入错误！")
        else:
            print("输入的班级名称不存在或者已经分配讲师！")

        # print(self.unassigned_classes)  # 未分配讲师的班级列表

    def check_classes_student(self):
        self.check_classes()
        classes_name = input("请输入要查询的班级名称：").strip()
        if classes_name in self.sch_obj.classes:
            classes_obj = self.sch_obj.classes[classes_name]
            if classes_obj.course_student:
                print("班级【%s】的学员信息如下：" % classes_name )
                for student_name in classes_obj.course_student:
                    student_score = classes_obj.course_score[student_name]
                    student_obj = self.sch_obj.student[student_name]
                    print("学员姓名：【%s】 年龄： 【%s】 课程得分：【%s】" %(student_name, student_obj.age, student_score ))
            else:
                print("该班级暂无学员报名！")
        else:
            print("查询的班级不存在！")

    def manage_students_score(self):
        self.check_classes()
        classes_name = input("请输入要查询的班级名称：").strip()
        if classes_name in self.sch_obj.classes:
            classes_obj = self.sch_obj.classes[classes_name]
            if classes_obj.course_student:
                print("班级【%s】的学生分数如下：" % classes_name)
                for student_name in classes_obj.course_student:
                    student_score = classes_obj.course_score[student_name]
                    print("学员姓名：【%s】  课程得分：【%s】" % (student_name,  student_score))
                student_name = input("请输入你要修改成绩的学员姓名：").strip()
                student_score = input("请输入该学员新的成绩: ").strip()
                if student_name in classes_obj.course_student:
                    classes_obj.course_score[student_name] = student_score
                    print("修改班级【%s】的学员【%s】成绩【%s】成功！"%(classes_name, student_name, student_score))
                else:
                    print("班级无该学员信息")
            else:
                print("该班级暂无学员成绩信息！")
        else:
            print("查询的班级不存在！")
if __name__ == "__main__":
    pass