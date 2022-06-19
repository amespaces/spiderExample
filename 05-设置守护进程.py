import time
import multiprocessing


def work():
    for i in range(10):
        print("工作中。。。。")
        time.sleep(0.2)


if __name__ == '__main__':
    # 方式一
    work_process = multiprocessing.Process(target=work, daemon=True)

    # 方式二
    # work_process.daemon =True

    work_process.start()
    time.sleep(1)
    print("主进程结束")