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
    start = time.time()
    sing()
    dance()
    end = time.time()
    print(f"执行时间共 {end - start} s")