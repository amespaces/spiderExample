import os
import multiprocessing


# 实现了一个源文件读写到目标文件的案例
def copy_file(file_name, source_dir, dest_dir):
    """
    1.拼接源文件路径 和目标文件路径
    2 打开源文件和目标文件
    :param file_name:
    :param source_dir:
    :param dest_dir:
    :return:
    """
    # 拼接路径
    source_path = source_dir + "/" + file_name
    dest_path = dest_dir + "/" + file_name
    print(source_path, "----->", dest_path)
    # 打开源文件、创建目标文件
    with open(source_path, "rb") as source_file:
        with open(dest_path, "wb") as dest_file:
            while True:
                data = source_file.read(1024)
                if data:
                    dest_file.write(data)
                else:
                    # 为空表示读完
                    break


if __name__ == '__main__':
    source_dir = r"C:\Users\朱威煌\Documents\学习笔记"
    dest_dir = r"D:\spiderExample\笔记"
    try:
        os.mkdir(dest_dir)
    except:
        print("目标文件夹已存在了")
    # 读取源文件夹的文件列表
    file_list = os.listdir(source_dir)
    # 遍历文件列表实现拷贝
    for file_name in file_list:
        # copy_file(file_name, source_dir, dest_dir)
        # 使用多进程实现多任务拷贝
        sub_process = multiprocessing.Process(target=copy_file, args=(file_name, source_dir, dest_dir))
        sub_process.start()
