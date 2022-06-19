import time
import multiprocessing


def sing(name, num):
    for i in range(num):
        print(f"{name} 在唱歌")
        time.sleep(0.5)


def dance(num):
    for i in range(num):
        print("跳舞")
        time.sleep(0.5)


if __name__ == '__main__':
    # 以元组形式传参
    s1 = multiprocessing.Process(target=sing, args=('夏明', 3))
    # 以字典形式传参
    s2 = multiprocessing.Process(target=dance, kwargs={"num": 5, })

    s1.start()
    s2.start()
