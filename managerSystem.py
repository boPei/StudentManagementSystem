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
        print('\t\t\tShow student information-----5')
        print('\t\t\tSave student information-----6')
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
            print(f'There is no such a {del_name} existing currently...')

    def modify_student(self):
        '''
        1.首先,利用input()输入一个学生的姓名；
        2. 在self.student_list中查询是否存在这样一个学生，如果存在，则利用input进行赋值修改
        3. 如果不存在，则在for循环外部，进行else判断的另一项操作
        :return:
        '''
        print('Modify the information of a student')
        modi_stud = input('Please input a student name whose information you want to modify')
        for stud in self.student_list:
            if stud.name == modi_stud:
                stud.name = input('Please input a name you want to update')
                stud.gender = input('Please input a gender you want to update')
                stud.tel = input('Please input a tel no you want to update')
                print(f'Student {modi_stud} information update successfully!')
                break
        else: #表示遍历了所有的元素都没有找到满足条件的值
            print('There is no such a student existing in the system.')


    def search_student(self):
        '''
        1. input输入要查询的学生的姓名
        2. 判断是否存在于学生的列表中，如果存在显示其信息
        3. 如果不存在显示提示信息
        :return:
        '''
        print('Search a student')
        search_stud = input('Please input a student name that you want to search in the student list:')
        for stud in self.student_list:
            if stud.name == search_stud:
                print(f"Student info:\nName: {stud.name}, Gender: {stud.gender}, Tel: {stud.tel}")
                break
        else:
            print('There is no such a student existing in the system.')

    def show_student(self):
        '''
        显示所有的学员的信息
        :return:
        '''
        print('Show the information of a student')
        print('Name\tGender\tTel')
        for stud in self.student_list:
            print(f'{stud.name}\t{stud.gender}\t{stud.tel}')

    def save_student(self):
        print('Save the information of a student')
        '''
        类的一个对象的__dict__属性能够将该对象的所有的属性与其值组成一个字典
        for stud in self.student_list:
            print(stud.__dict__)
        '''

        with open('data\student.data', 'w') as file:
            for stud in self.student_list:
                # file.write(f'Name: {stud.name}\tGender: {stud.gender}\tTel: {stud.tel}\n')
                file.write(str(stud.__dict__)+'\n')
            file.close()

    def load_student(self):
        '''
        1. 打开文件
            try:
            except:
            只读形式打开，如果打不开则说明文件不存在，就用w形式打开
        2. 写入数据--注意self.student_list中存放的是学生对象，因此应该把数据转换成对象
        :return:
        '''
        print('Load student data...')
        try:
            f = open('data\student.data', 'r')
        except: # 如果不存在则直接新建一个文件
            f = open('data\student.data', 'w')
        else:
            # eval的用法，----去字符串化，将字符串形式的数据转换成本来的样子
            stud_list = [eval(student) for student in f.readlines()]
            self.student_list = [Student(stud['name'], stud['gender'], stud['tel']) for stud in stud_list]
            print('Student data has been loaded!')
        finally:
            f.close()
        # ##################################################################
        # f.read()方法能够一次性读出所有的数据
        # for t in f.read().split('\n'):
        #     print(t)
        #     print(type(t))
        #     print(eval(t)['name'])




