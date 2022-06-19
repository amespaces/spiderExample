# 导入进程包

# start
import multiprocessing
import time


# 唱歌
def sing():
    for i in range(3):
        print("唱歌")
        time.sleep(0.5)


# 跳舞
def dance():
    for i in range(3):
        print("跳舞")
        time.sleep(0.5)


# 会发现先执行三次唱歌，三次跳舞
if __name__ == '__main__':
    # 创建进程对象
    sing_process = multiprocessing.Process(target=sing)
    dance_process = multiprocessing.Process(target=dance)
    # 使用进程对象执行
    sing_process.start()
    dance_process.start()
