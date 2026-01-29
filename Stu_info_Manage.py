class StudentManager:
    #初始化存储学生信息列表
    def __init__(self):
        self.students=[]
    def print_menu(self):
        print("="*30)
        print("1.添加学生：输入姓名、年龄、学号，判断学号是否重复，若不重复则添加到系统")
        print("2.查询学生：输入学号，查询对应的学生的完整信息；若不存在，提示“未找到该学生“")
        print("3.修改年龄：输入学号和新年龄，修改对应学生的年龄；若学号不存在，提示“未找到该学生”")
        print("4.删除学生：输入学号，删除对应学生信息；若学号不存在，提示”未找到该学生“")
        print("5.退出系统：输入指定指令，退出控制台程序")
    #功能1 添加学生
    def add_student(self):
        print("请开始添加学生：")
        try:
            name=input("请输入学生姓名：")
            age=int(input("请输入学生年龄（0-120）："))
            id=int(input("请输入学生学号："))
            if age>=0 and age<=120:
                for student in self.students:
                    if id==student['id']:
                        print("该学生已存在，请输入新的学生信息！")
                        return
                self.students.append({'name':name,'age':age,'id':id})
                print("该学生的信息添加完成！")
            else:
                print("请输入正确的学生年龄！")
                return
        except (ValueError,TypeError):
            print("请输入正确的年龄格式！")
            return

    #功能2  查询学生
    def query_student(self):
        print("请开始查询学生信息：")
        try:
            id=int(input("请输入学生学号："))
            for student in self.students:
                if id==student['id']:
                    print("查询到该学生的信息：")
                    print(f"姓名：{student['name']},年龄:{student['age']}，学号：{student['id']}")
                    return
            print("未找到该学生")
            return
        except (ValueError,TypeError):
            print("请输入正确的学号格式！")
            return

    #功能3  修改学生年龄
    def modify_age(self):
        print("请开始修改学生信息：")
        try:
            id=int(input("请输入学生学号："))
            age=int(input("请输入要修改的学生年龄："))
            for student in self.students:
                if id==student['id']:
                    if age >= 0 and age <= 120:
                        student['age']=age
                        print("该学生的年龄信息修改完成！")
                    else:
                        print("请输入正确的学生年龄！")
                    return
            print("未找到该学生")
            return
        except (ValueError,TypeError):
            print("请输入正确的学号或年龄格式！")
            return

    #功能4  删除学生信息
    def delete_student(self):
        print("请开始删除学生信息：")
        try:
            id=int(input("请输入要删除的学生的学号："))
            for student in self.students:
                if id==student['id']:
                    self.students.remove(student)
                    print("已删除该学生的信息！")
                    return
            print("未找到该学生！")
            return
        except (ValueError,TypeError):
            print("请输入正确的学号格式！")
            return


    #运行功能：
    def run(self):
        self.print_menu()
        while True:
            try:
                choice = int(input("请输入你要执行的功能编号（1-5）："))
                if choice == 1:
                    self.add_student()
                elif choice == 2:
                    self.query_student()
                elif choice == 3:
                    self.modify_age()
                elif choice == 4:
                    self.delete_student()
                elif choice == 5:
                    print("👋 感谢使用简易学生信息管理系统，系统即将退出！")
                    break
                else:
                    print("❌ 功能编号输入错误！请输入1-5之间的数字！")
            except ValueError:
                print("❌ 输入错误！功能编号必须为数字！")
            print("\n" + "-" * 50 + "\n")




if __name__=="__main__":
    sm=StudentManager()
    sm.run()