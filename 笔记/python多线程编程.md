[(90条消息) python多线程编程-基础篇_princezf的博客-CSDN博客_python多线程编程](https://blog.csdn.net/princezf/article/details/113110550)

## 进程的创建步骤

```python
# 导入进程包
import multiprocessing
# 2.通过进程类创建对象
进程对象 = multiprocessing.Process()
# 3 启动进程执行任务
进程对象.start()
```

```
multiprocessing.Process(target= 任务名)
target 执行目标任务名，这里指函数名
name 进程名
group 进程组，目前只能使用None
```

## 案例

### 单任务

```python
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
```

### 多进程

```python
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



if __name__ == '__main__':
    # 创建进程对象
    sing_process = multiprocessing.Process(target=sing)
    dance_process = multiprocessing.Process(target=dance)
    # 使用进程对象执行
    sing_process.start()
    dance_process.start()

```

## 进程执行带有参数的任务

```
sing_process = multiprocessing.Process(target= sing, args=())

```

| 参数名 |            说明            |
| :----: | :------------------------: |
|  args  | 以元组的方式给执行任务传参 |
| kwargs |  以字典方式给执行任务传参  |

```python
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

```

注意事项：

- 元组传参要和参数顺序一致’
- 字典方式字典的key要和参数名一致

## 获取进程编号

- os.getpid()
- os.getppid()
- 当程序中进程的数量越来越多时，如果没有办法区分主进程和子进程还有不同的子进程，那么就无法进行有效的进程管理，为了方便管理实际上每个进程都是有自己的编号的。

```python
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
# 主进程会等待所有子进程执行结束再结束
```

## 进程注意点

```python
import time
import multiprocessing


def work():
    for i in range(10):
        print("工作中")
        time.sleep(0.2)


if __name__ == '__main__':
    work_process = multiprocessing.Process(target=work)
    work_process.start()
    time.sleep(1)
    print("主进程结束")
工作中
工作中
工作中
工作中
工作中
主进程结束
工作中
工作中
工作中
工作中
工作中
```

### 设置守护进程

主进程结束后不再继续执行子进程中剩余的工作

```python
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
工作中。。。。
工作中。。。。
工作中。。。。
工作中。。。。
工作中。。。。
主进程结束
```

## 案例-多进程实现视频文件夹多任务拷贝器

1. 需求分析
   - 目标文件夹是否存在，如果不存在就创建，存在则不创建
   - 遍历源文件夹中所有文件，并拷贝到目标文件夹
   - 采用进程实现多任务，并完成拷贝
2. 实现步骤
   - 定义源文件夹所在的路径，目标文件夹所在路径
   - 创建目标文件夹
   - 通过`os.listdir`获取源目录中的文件列表
   - 遍历每个文件，定义一个函数，专门实现文件拷贝
   - 采用进程实现多任务，完成高并发拷贝

```

```

