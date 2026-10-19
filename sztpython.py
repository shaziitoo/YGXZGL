import os.path

filename = 'employee.txt'


def main():
    while True:
        menu()
        choice = int(input('请选择功能'))
        if choice in [0, 1, 2, 3, 4, 5, 6, 7]:
            if choice == 0:
                answer = input('您确定退出系统吗？y/n')
                if answer == 'y' or answer == 'Y':
                    print("欢迎您的使用！！")
                    break
                else:
                    continue
            elif choice == 1:
                insert()
            elif choice == 2:
                search()
            elif choice == 3:
                delete()
            elif choice == 4:
                modify()
            elif choice == 5:
                sort()
            elif choice == 6:
                total()
            elif choice == 7:
                show()
        input()


def menu():
    print('==================员工薪资信息管理系统==============')
    print('===============功能菜单==================')
    print('\t\t\t1. 录入员工信息')
    print('\t\t\t2. 查找员工信息')
    print('\t\t\t3. 删除员工信息')
    print('\t\t\t4. 修改员工信息')
    print('\t\t\t5. 对员工进行排序')
    print('\t\t\t6. 统计员工总人数')
    print('\t\t\t7. 显示所有员工信息')
    print('\t\t\t0. 退出程序')
    print('======================================')


def insert():
    employee_list = []
    while True:
        id = input("请输入ID：")
        if not id:
            break
        name = input("请输入姓名：")
        if not name:
            break
        try:
            ticheng = int(input("请输入提成："))
            bonus = int(input("请输入奖金："))
            wage = int(input("请输入基本工资："))
        except:
            print("输入无效，请重新输入")
        employee = {'id': id, 'name': name, 'ticheng': ticheng, 'bonus': bonus, 'wage': wage}

        employee_list.append(employee)
        answer = input("是否继续添加y/n?")
        if answer == 'y':
            continue
        else:
            break

    save(employee_list)
    print("员工信息保存成功")


def save(lst):
    try:
        stu_txt = open(filename, 'a', encoding='utf-8')
    except:
        stu_txt = open(filename, 'w', encoding='utf-8')
    for item in lst:
        stu_txt.write(str(item) + '\n')
    stu_txt.close()


def search():
    employee_query = []
    while True:
        id = ''
        name = ''
        if os.path.exists(filename):
            mode = input("按ID查找请按1，按姓名查找请按2：")
            if mode == '1':
                id = input("请输入员工ID：")
            elif mode == '2':
                name = input("请输入员工姓名：")
            else:
                print("输入有误，请重新输入")
                search()
            with open(filename, 'r', encoding='utf-8') as file:
                employee = file.readlines()
                for item in employee:
                    d = dict(eval(item))
                    if id != '':
                        if d['id'] == id:
                            employee_query.append(d)
                    elif name != '':
                        if d['name'] == name:
                            employee_query.append(d)
            show_query(employee_query)

            employee_query.clear()
            answer = input("是否继续查询？y/n")
            if answer == 'y':
                continue
            else:
                break
        else:
            print("无员工信息")
            return


def show_query(lst):
    if len(lst) == 0:
        print("无相关信息")
        return

    format_title = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    print(format_title.format('ID', '姓名', '提成', '奖金', '工资', '总薪资'))

    format_data = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    for item in lst:
        print(format_data.format(item.get('id'),
                                 item.get('name'),
                                 item.get('ticheng'),
                                 item.get('ticheng'),
                                 item.get('wage'),
                                 int( item.get('ticheng')) + int( item.get('ticheng')) + int( item.get('wage'))
                                 ))


def delete():
    while True:
        employee_id = input("请输入删除员工的ID：")
        if employee_id != '':
            if os.path.exists(filename):
                with open(filename,'r',encoding='utf-8') as file:
                    employee_old = file.readlines()
            else:
                employee_old = []
            flag = False
            if employee_old:
                with open(filename,'w',encoding='utf-8') as wfile:

                    d = {}
                    for item in employee_old:
                        d = dict(eval(item))
                        if d['id'] != employee_id:
                            wfile.write(str(d)+'\n')
                        else:
                            flag = True
                    if flag:
                        print(f'id为{employee_id}的员工信息已被删除')
                    else:
                        print(f'没有找到员工ID为{employee_id}的员工')
            else:
                print("无员工信息")
                break
            show()
            answer = input("是否继续删除？y/n")
            if answer == 'y':
                continue
            else:
                break


def modify():
    show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            employee_old = file.readlines()
    else:
        return
    employee_id = input("请输入修改员工的ID：")
    with open(filename, 'w', encoding='utf-8') as wfile:
        for item in employee_old:
            d = {}
            d = dict(eval(item))
            if d['id'] == employee_id:
                print("已经找到员工信息，请修改相关信息")
                while True:
                    try:
                        d['name'] = input("请输入姓名")
                        d['ticheng'] = input("请输入提成")
                        d['bonus'] = input("请输入奖金")
                        d['wage'] = input("请输入基本工资")
                    except:
                        print("输入有误，请重新输入")
                    else:
                        break
                    wfile.write(str(d) + '\n')
                    print("修改成功")
            else:
                wfile.write(str(d)+'\n')
            answer = input("是否继续修改其他员工信息？y/n")
            if answer == 'y':
                modify()
            else:
                return


def sort():
    show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding= 'utf-8') as file:
            employee = file.readlines()
        employee_new = []
        for item in employee:
            d = dict(eval(item))
            employee_new.append(d)
    else:
        return

    asc_or_desc = input("请选择升序 0 还是降序 1？")
    if asc_or_desc == '0':
        asc_or_desc_bool = False
    elif asc_or_desc == '1':
        asc_or_desc_bool = True
    else:
        print("输入有误，请重新输入")
        sort()
    mode = input("请选择排序方式(1.提成 2.奖金 3.基本工资 4.总薪资)：")
    if mode == '1':
        employee_new.sort(key=lambda x : int(x['ticheng']), reverse=asc_or_desc_bool)

    elif mode == '2':
        employee_new.sort(key=lambda x: int(x['bonus']), reverse=asc_or_desc_bool)
    elif mode == '3':
        employee_new.sort(key=lambda x: int(x['wage']), reverse=asc_or_desc_bool)
    elif mode == '4':
        employee_new.sort(key=lambda x: int(x['ticheng']) + int(x['bonus']) + int(x['wage']), reverse=asc_or_desc_bool)
    else:
        print("输入有误，请重新输入")
    show_query(employee_new)


def total():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            employee = file.readlines()
            if employee:
                print(f"总共有{len(employee)}名员工")
            else:
                print("无员工信息")
    else:
        print("无员工信息")

def show():
    employee_query = []
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            employee = file.readlines()
            for item in employee:
                d = dict(eval(item))
                employee_query.append(d)
        show_query(employee_query)

        employee_query.clear()
    else:
        print("无员工信息")
        return


if __name__ == '__main__':
    main()





