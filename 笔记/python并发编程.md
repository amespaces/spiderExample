[TOC]



# python并发编程

1.python速度慢的两大原因

- 动态类型语言，边编译边执行
- GIL

2.全局解释器锁（Global Interpreter Lock)

是计算机程序设计语言解释器用于同步线程的一个机制，它使得任何时刻仅有一个线程在执行，即便在多核处理器上，使用GIL的解释器也只允许同一时间执行一个线程

3.设计初期，为了规避并发问题引入GIL

4.怎么规避GIL带来的限制

- 多线程threading用于IO密集型计算，在I/O期间线程会释放GIL,实现CPU和IO的并行，但是多线程用于CPU密集型计算只会拖慢速度
- 使用multiprocessing的多进程机制实现并行计算、利用多核CPU优势，应对GIL问题



## 多线程

### python 创建多线程的方法

```python
# 1.准备一个函数
def my_func(a, b):
    do_craw(a, b)
# 2.创建线程
import threading
t = threading.Thread(target = my_func, agrs = (100,200))
# 启动线程
t.start()
# 等待结束
t.join()
```



### 改写爬虫程序，变成多线程爬取

```python
import blog_spider
import threading
import time


def single_thread():
    print("single_thread begin")
    for url in blog_spider.urls:
        blog_spider.craw(url)


def multi_thread():
    print("multi_thread begin")
    threads = []
    for url in blog_spider.urls:
        threads.append(threading.Thread(target=blog_spider.craw, args=(url,)))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


if __name__ == '__main__':
    start = time.time()
    single_thread()
    end = time.time()
    # 10.44405484199524 seconds
    print(f"single thread cost {end - start} seconds")

    start = time.time()
    multi_thread()
    end = time.time()
    # 1.3658344745635986 seconds 加速了10倍
    print(f"multi thread cost {end - start} seconds")
```

## Python实现生产者消费者爬虫

### 多组件的Pipeline技术架构

### 生产者消费者爬虫架构

### 多线程数据通信的queue.Queue

queue.Queue可以用于多线程之间线程安全的数据通信

```python
# 1. 导入类库
import queue

q = queue.Queue()

q.put(item)

item = q.get()

q.qsize()
q.empty()
q.full()
```



### 代码编写实现生产者消费者爬虫



