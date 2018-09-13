#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/12 10:15

import pickle
from conf import settings

class Base(object):
    def __init__(self):
        #读取数据库
        with open(settings.db, 'rb') as db_f:
            self.db = pickle.load(db_f)
        #执行各管理视图
        self.run()
        #退出各管理视图界面后，存储数据
        with open(settings.db, 'wb') as db_f:
            pickle.dump(self.db, db_f)
    def run(self):
        print("This is base class!")
        print(self.db)


    def check_classes(self):
        self.unassigned_classes = [] #未分配班级列表
        if not self.sch_obj.classes:
            print("当前无班级，请创建班级！")
        else:
            print("【%s】所有班级信息:" % self.school_choise)
            # print(self.sch_obj.classes)
            has_teachers_classes = []  # 已经分配讲师的班级列表
            for key in self.sch_obj.classes:  #
                classes_obj = self.sch_obj.classes[key]
                for key2 in self.sch_obj.teacher:
                    teacher_obj = self.sch_obj.teacher[key2]
                    # print("讲师：",teacher_obj.__dict__)
                    for key3 in teacher_obj.classes:
                        # print(teacher_obj.classes[key3].__dict__)
                        if classes_obj.name == teacher_obj.classes[key3].name:
                            has_teachers_classes.append(classes_obj.name)
                            # print(teacher_obj.classes[key3].name)
                            print("班级:【%s】,关联课程：【%s】，周期:【%s】月,价格:【%s】,授课老师:【%s】" % (classes_obj.name, classes_obj.course_obj.name,
                                                                          classes_obj.course_obj.period,
                                                                          classes_obj.course_obj.price,
                                                                          teacher_obj.name))
                            break
                        else:
                            # print("班级:%s,关联课程：%s，周期:%s月,价格:%s,授课老师: 【暂未分配】 " % (
                            #     classes_obj.name, classes_obj.course_obj.name, classes_obj.course_obj.period,
                            #     classes_obj.course_obj.price))
                            # no_teachers_classes.append(classes_obj.name)
                            pass
            for key in self.sch_obj.classes:
                if key not in has_teachers_classes:
                    classes_obj = self.sch_obj.classes[key]
                    self.unassigned_classes.append(classes_obj.name)
                    print("班级:【%s】,关联课程：【%s】，周期:【%s】月,价格:【%s】,授课老师:【%s】" % (classes_obj.name, classes_obj.course_obj.name,
                                                                  classes_obj.course_obj.period,
                                                                  classes_obj.course_obj.price, '暂未分配'))

    def check_course(self):
        if not self.sch_obj.course:
            print("当前无课程！")
        else:
            print("所有课程信息:")
            for key in self.sch_obj.course:
                course_obj = self.sch_obj.course[key]
                print("课程：【%s】, 周期: 【%s】月, 价格: 【%s】 元 " % (course_obj.name, course_obj.period, course_obj.price))

    def check_teacher(self):
        if not self.sch_obj.teacher:
            print("当前无讲师,请添加！")
        else:
            print("所有老师信息:")
            for key in self.sch_obj.teacher:
                teacher_obj = self.sch_obj.teacher[key]
                teacher_classes_list = []
                for key2 in teacher_obj.classes:
                    d = {}
                    classes_obj = teacher_obj.classes[key2]
                    course_name = classes_obj.course_obj.name
                    d[key2] = course_name
                    teacher_classes_list.append(d)
                print("姓名：【%s】, 薪水：【%s】，授课班级及课程: %s " % (teacher_obj.name, teacher_obj.salary, teacher_classes_list))

    #执行退出
    def logout(self):
        with open(settings.db, 'wb') as db_f:
            pickle.dump(self.db, db_f)
        exit(0)

if __name__ == "__main__":
    pass