import multiprocessing
import time
import os


def sing(name, num):
    print("唱歌进程的编号：", os.getpid())
    print("唱歌的父进程编号", os.getppid())
    for i in range(num):
        print(f"{name} 在唱歌")
        time.sleep(0.5)


def dance(num):
    print("跳舞进程的编号：", os.getpid())
    print("跳舞的父进程编号", os.getppid())
    for i in range(num):
        print("跳舞")
        time.sleep(0.5)


if __name__ == '__main__':
    print("主进程编号：", os.getpid())
    # 以元组方式传参
    sing_process = multiprocessing.Process(target=sing, args=("小明", 3))

    dance_process = multiprocessing.Process(target=dance, kwargs={"num": 3, })

    sing_process.start()
    dance_process.start()
