from models import User, engine, ModelBase, Session

session = Session()


def createUser(username, join_date, password):
    user = User(username=username, date_joined=join_date, password=password)
    session.add(user)
    session.commit()


def deleteUser(username):
    user = session.query(User).filter(User.username == username).first()
    session.delete(user)
    session.commit()


def getUser(username):
    user = session.query(User).filter_by(username=username).first()
    return user


def getAll():
    all_user = session.query(User).filter()
    return all_user


def editUser(username):
    user = session.query(User).filter_by(username=username).first()

    while True:
        options = input('请输入要编辑的选项((1)->修改用户名(2)->修改密码):')
        if options == '1':
            user.username = input('请输入新的用户名:')
            yesNo = input('用户名已更改，你要保存吗Y/n:')
            if yesNo == 'Y' or yesNo == 'y':
                session.commit()
            elif yesNo == 'N' or yesNo == 'n':
                session.rollback()
        elif options == '2':
            user.password = input('请输入新的密码:')
            yesNo = input('密码已更新，你要保存吗Y/n:')
            if yesNo == 'Y' or yesNo == 'y':
                session.commit()
            elif yesNo == 'N' or yesNo == 'n':
                session.rollback()
        exitFlag = input('您要退出编辑吗Y/n:')
        if exitFlag == 'Y' or exitFlag == 'y':
            break


def getUserCount():
    userCount = session.query(User).count()
    return userCount


while True:
    options = input(
        "//C:创建用户 | D:删除用户 | E:编辑用户 | SD:查询单个用户 | ALL:查询所有用户 | num:查询用户数量 | Q:退出//\n>>>")
    if options == 'C' or options == 'c':
        username = input("请输入用户名:")
        date_joined = input('请输入日期格式/(2010-12-05):')
        password = input('请输入密码：')
        createUser(username=username, join_date=date_joined, password=password)
    elif options == 'D' or options == 'd':
        user = input('请输入要删除的用户名:')
        deleteUser(user)
    elif options == 'E' or options == 'e':
        user = input('请输入要编辑的用户名:')
        editUser(user)
    elif options == 'SD' or options == 'sd':
        username = input('请输入要查询的用户名:')
        user = getUser(username)
        print("\n\nusername: %s\njoined_date: %s\npassword: %s\n\n" % (
            user.username, user.date_joined, user.password))
    elif options == 'ALL' or options == 'all':
        for user in getAll():
            print("\nusername: %s\njoined_date: %s\npassword: %s\n" % (
                user.username, user.date_joined, user.password))
    elif options == 'NUM' or options == 'num':
        print('用户数量: %s\n' % getUserCount())
    elif options == 'Q' or options == 'q':
        session.close()
        break
