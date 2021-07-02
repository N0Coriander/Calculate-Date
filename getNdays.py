#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: N0Coriander
@address: https://github.com/N0Coriander
@desc:
场景一：分析工程师收到项目安排，截图中记录有"最近一次分析时间"，运行脚本输入该时间，可自动计算本次分析周期
场景二：分析工程师收到售前项目或第一分析的售后项目，需要计算往前推的分析周期
"""
import datetime


if __name__ == "__main__":
    user = input('请输入最近一次分析时间(如5.1): ')
    # 考虑到用户手速过快...的情况
    for i in ['.', '。', '-', '，', ',', '/', ';', '；']:
        if i in user:
            a = user.split(i)
    if len(a) < 3:
        data = datetime.datetime(2021, int(a[0]), int(a[1]))
        # 本次分析周期开始日期
        start = data + datetime.timedelta(days=1)
        # 本次分析周期结束日期
        end1 = start + datetime.timedelta(days=6, hours=23, minutes=59, seconds=59)
        end2 = start + datetime.timedelta(days=29, hours=23, minutes=59, seconds=59)
        end3 = start + datetime.timedelta(days=59, hours=23, minutes=59, seconds=59)
        end4 = start + datetime.timedelta(days=89, hours=23, minutes=59, seconds=59)
        print('[+] +7天  分析周期为：', start, '至', end1)
        print('[+] +30天 分析周期为：', start, '至', end2)
        print('[+] +60天 分析周期为：', start, '至', end3)
        print('[+] +90天 分析周期为：', start, '至', end4)
        print('-' * 60)
        # 考虑到少部分项目为第一次分析，需要提供往前推的分析周期
        # 将输入的日期作为分析周期的最后一天
        print('首次出报告时分析周期如下')
        final = data + datetime.timedelta(hours=23, minutes=59, seconds=59)
        # 分析周期的开始日期
        begin1 = final - datetime.timedelta(days=6, hours=23, minutes=59, seconds=59)
        begin2 = final - datetime.timedelta(days=29, hours=23, minutes=59, seconds=59)
        begin3 = final - datetime.timedelta(days=59, hours=23, minutes=59, seconds=59)
        begin4 = final - datetime.timedelta(days=89, hours=23, minutes=59, seconds=59)
        print('[+] -7天  分析周期为：', begin1, '至', final)
        print('[+] -30天 分析周期为：', begin2, '至', final)
        print('[+] -60天 分析周期为：', begin3, '至', final)
        print('[+] -90天 分析周期为：', begin4, '至', final)

    else:
        data = datetime.datetime(int(a[0]), int(a[1]), int(a[2]))
        # 本次分析周期开始日期
        start = data + datetime.timedelta(days=1)
        # 本次分析周期结束日期
        end1 = start + datetime.timedelta(days=6, hours=23, minutes=59, seconds=59)
        end2 = start + datetime.timedelta(days=29, hours=23, minutes=59, seconds=59)
        end3 = start + datetime.timedelta(days=59, hours=23, minutes=59, seconds=59)
        end4 = start + datetime.timedelta(days=89, hours=23, minutes=59, seconds=59)
        print('[+] +7天  分析周期为：', start, '至', end1)
        print('[+] +30天 分析周期为：', start, '至', end2)
        print('[+] +60天 分析周期为：', start, '至', end3)
        print('[+] +90天 分析周期为：', start, '至', end4)
        print('-' * 60)
        # 考虑到少部分项目为第一次分析，需要提供往前推的分析周期
        # 将输入的日期作为分析周期的最后一天
        print('首次出报告时分析周期如下')
        final = data + datetime.timedelta(hours=23, minutes=59, seconds=59)
        # 分析周期的开始日期
        begin1 = final - datetime.timedelta(days=6, hours=23, minutes=59, seconds=59)
        begin2 = final - datetime.timedelta(days=29, hours=23, minutes=59, seconds=59)
        begin3 = final - datetime.timedelta(days=59, hours=23, minutes=59, seconds=59)
        begin4 = final - datetime.timedelta(days=89, hours=23, minutes=59, seconds=59)
        print('[+] -7天  分析周期为：', begin1, '至', final)
        print('[+] -30天 分析周期为：', begin2, '至', final)
        print('[+] -60天 分析周期为：', begin3, '至', final)
        print('[+] -90天 分析周期为：', begin4, '至', final)