# 📌 На семинаре 13 был создан проект по работе с
# пользователями (имя, id, уровень).
# 📌 Напишите 3-7 тестов pytest для данного проекта.
# 📌 Используйте фикстуры.

import pytest

from sem_13_05 import Project
from sem_13_03 import AccessException, LevelException
from sem_13_04 import User


# фикстура создание проекта
@pytest.fixture
def project():
    filename = "HW_14\\hw_task\\users.json"
    return Project.load(filename)

# фикстура проект + user
@pytest.fixture
def user(project):
    u_1 = User("54321", "var")
    return project, u_1

# фикстура проект + admin
@pytest.fixture
def project_admin(project):
    project.login("54321", "var")
    return project


# создание экземпляра класса Project
def test_create(project):
    assert isinstance(project, Project), 'type mismatch'

# проверка добавления админа
def test_login(user):
    project, u_1 = user
    assert u_1 in project.users, 'User missin'
    project.login("54321", "var")
    assert project.admin == u_1, 'User did not admin'

# проверка ошибки "пользователь остуствует"
def test_login_missin(project):
    with pytest.raises(AccessException):
        project.login('7', 'temp')


# добавление пользователя без администратора в проекте
def test_not_add_user(project):
    with pytest.raises(AttributeError):
        project.add_user('7', 'temp', 2)

# добавление пользователя
def test_add_user(project_admin):
    u_1 = User('010', 'Мустафа', '7')
    assert u_1 not in project_admin.users
    project_admin.add_user('010', 'Мустафа', "5")
    assert u_1 in project_admin.users

# удаление пользователя из проекта
def test_del_user(project_admin):
    u_1 = User('010', 'Мустафа', '7')
    project_admin.add_user('010', 'Мустафа', "5")
    assert u_1 in project_admin.users
    project_admin.del_user(u_1)
    assert u_1 not in project_admin.users, 'User did not delete'

if __name__ == '__main__':
    pytest.main(['-v'])