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
    # 1.3658344745635986 seconds
    print(f"multi thread cost {end - start} seconds")