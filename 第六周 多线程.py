# coding:utf-8

"""
进程负责拿到资源（cpu、内存） 线程负责具体的执行
进程的创建模块 multiprocessing
函数名     介绍          参数      返回值
Process  创建一个进程  target,arg  进程对象

start     执行进程       无        无
join     阻塞程序         无       无
kill      杀死进程       无        无
is_alive 进程是否存活    无       bool

不足：通过进程模块执行的函数无法获取返回值，多个进程同时修改文件可能出现错误，数量太多占用资源多
"""

"""
进程池与进程锁
进程池的创建multiprocessing
函数名     介绍          参数      返回值
Pool    进程池创建   Processcount    进程池对象

apply_async  任务加入进程池(异步) func,args  无
close    关闭进程池        无        无
join     等待进程池任务结束  无      无
"""