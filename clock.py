import math
import datetime
import sys
import time
import os
# def circle(radius):
#     print radius
#     hour_hand, minute_hand, second_hand = str(datetime.datetime.now().time()).split('.')[0].split(':')
#     hour_hand = int(hour_hand) - 12 if int(hour_hand) > 12 else int(hour_hand)
#     minute_hand = int(minute_hand)
#     second_hand = int(second_hand)
#     print hour_hand, minute_hand, second_hand
#     for i in range((radius * 2) + 1):
#         for j in range((radius * 2) + 1):
#             # theta = math.asin(arc_chord / (2 * radius))
#             # arc_len = radius * theta
#             dis = math.sqrt(((i - radius) ** 2) + ((j - radius) ** 2))
#             if dis > radius - 0.5 and dis < radius + 0.5:
#                 print ' ',
#             else:
#                 print ".",
#         print ""

# circle(20)
def combine(list_nums):
    list_new = []
    for arr in list_nums:
        temp_list = arr.split('\n')
        list_new.append(temp_list)
    # print len(list_new[0])
    for i in range(len(list_new[0])):
        for j in range(len(list_new)):
            print list_new[j][i],
        print ""
    
    for i in range(len(list_new[0])):
        for j in range(len(list_new)):
            sys.stdout.write("\033[F")
        # sys.stdout.write("\033[F")


def digital_clock():
    
    print "\n\n\n\n\n"
    one = '      ::\n      ::\n      ::\n      ::\n      ::\n      ::\n      ::'
    two = '::::::::\n      ::\n      ::\n::::::::\n::      \n::      \n::::::::'
    thr = '::::::::\n      ::\n      ::\n::::::::\n      ::\n      ::\n::::::::'
    fou = '::    ::\n::    ::\n::    ::\n::::::::\n      ::\n      ::\n      ::'
    fiv = '::::::::\n::      \n::      \n::::::::\n      ::\n      ::\n::::::::'
    six = '::::::::\n::      \n::      \n::::::::\n::    ::\n::    ::\n::::::::'
    sev = '::::::::\n      ::\n      ::\n      ::\n      ::\n      ::\n      ::'
    eig = '::::::::\n::    ::\n::    ::\n::::::::\n::    ::\n::    ::\n::::::::'
    nin = '::::::::\n::    ::\n::    ::\n::::::::\n      ::\n      ::\n::::::::'
    zer = '::::::::\n::    ::\n::    ::\n::    ::\n::    ::\n::    ::\n::::::::'
    sep = '        \n   ::   \n        \n        \n        \n   ::   \n        '
    dict_clock = {'1': one, '2': two, '3' :thr, '4': fou, '5': fiv, '6': six, '7': sev, '8': eig, '9': nin, '0': zer}
    while 1:
        hour_hand, minute_hand, second_hand = str(datetime.datetime.now().time()).split('.')[0].split(':')
        c_list = []
        for i in hour_hand:
            c_list.append(dict_clock[i])
        
        c_list.append(sep)

        for j in minute_hand:
            c_list.append(dict_clock[j])
        
        c_list.append(sep)

        for k in second_hand:
            c_list.append(dict_clock[k])
        
        combine(c_list)
        time.sleep(1)

digital_clock()
