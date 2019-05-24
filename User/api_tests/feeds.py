from User.api_tests.util import *
import os

user = []
n = 5


def init():
    os.system('cd ../../ && bash migrate.sh reset')
    for i in range(n):
        user.append('user%d' % i)

    for i in range(n):
        register(user[i], 'nick%d' % i)

    for i in range(1, n):
        star(user[0], user[i])

    for i in range(n << 2):
        publish(user[i % n], 'article%d' % i)


if __name__ == '__main__':
    init()
    ret = feeds(user[0], 1, 10)
    for each in ret:
        print(each)
