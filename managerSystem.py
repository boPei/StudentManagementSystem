from Students import *

class ManagerSystem(object):
    def __init__(self):
        self.student_list = []

    # 程序的入口函数
    def run(self):
        '''
        在这个函数中实现：
        1. 加载数据
        2. 显示功能菜单
        3. 循环判断用户的输入，并根据用户的输入执行相应的操作
        :return:
        '''
        # 加载数据
        self.load_student()

        # 循环监听用户的输入
        while True:
            self.show_menu()
            menu_num = int(input('Please input the no of the function:'))
            if menu_num == 1:
                # 添加学生
                self.add_student()
            elif menu_num == 2:
                # 删除学生
                self.del_student()
            elif menu_num == 3:
                # 修改学生信息
                self.modify_student()
            elif menu_num == 4:
                # 查询学生信息
                self.search_student()
            elif menu_num == 5:
                # 显示学生的信息
                self.show_student()
            elif menu_num == 6:
                # 保存学生信息
                self.save_student()
            else:
                break

        # 功能函数部分
        # 显示功能菜单
        # ----由于该方法是不涉及任何数据信息，因此可以设置为静态方法：
        # '''
        #     @staticmethod
        #     def showMenu():
        #         print()
        # '''

    @staticmethod
    def show_menu():
        print('Please choose the corresponding no of the following functions:')
        print('===============================================================')
        print('\t\t\tAdd a student-----1')
        print('\t\t\tDelete a student-----2')
        print('\t\t\tModify a student information-----3')
        print('\t\t\tSearch a student-----4')
        print('\t\t\tShow a student information-----5')
        print('\t\t\tSave a student information-----6')
        print('\t\t\tExit the system-----7')
        print('================================================================')

    def add_student(self):
        '''
        添加一个用户对象
            1. 提示用户输入相关信息：
                name=input('输入名字')
                gender=input('输入性别')
                tel=input('输入电话号码')
            2. 然后利用Student类，
            3. 将学生对象添加到列表中
        :return:
        '''
        print('Add a student')
        name = input('Please input the student name:')
        gender = input('Please input the student gender:')
        tel = input('Please input the student telephone number:')
        student = Student(name, gender, tel)
        self.student_list.append(student)
        print(self.student_list)
        print(student)


    def del_student(self):
        '''
            输入一个学员的姓名，然后在 self.student_list中查询该名字，如果不存在，输出提示信息；如果存在删除
            self.student_list.remove(item)
        :return:
        '''
        print('Delete a student')
        del_name = input("Please input the student name you want to remove")
        for stud in self.student_list:
            if stud.name == del_name:
                self.student_list.remove(stud)
                print(f'Student {del_name} has been removed successfully from the system.')
                break #注意该处要用退出
        else: #可以在循环体外执行if...else 的另一半
            print(f'There is no such a {del_name} existing currently.')

    def modify_student(self):
        print('Modify the information of a student')

    def search_student(self):
        print('Search a student')

    def show_student(self):
        print('Show the information of a student')

    def save_student(self):
        print('Save the information of a student')

    def load_student(self):
        print('Load student data...')



