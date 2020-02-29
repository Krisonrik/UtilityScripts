import os
import sys


def IsNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


def DigitCount(sequence_number):
    digi_cnt = 1
    while sequence_number >= 10:
        sequence_number /= 10
        digi_cnt += 1
    return digi_cnt


def GetExtension(file_name):
    segs = file_name.split(".")
    return segs[len(segs)-1]


def GetSequenceNumber(file_name):
    pure_name = file_name.split(".")[0]
    pos = len(pure_name)-1
    while(IsNumber(pure_name[pos])):
        pos -= 1
    return int(pure_name[pos+1: len(pure_name)])


def GetPureName(file_name):
    pure_name = file_name.split(".")[0]
    pos = len(pure_name)-1
    while(IsNumber(pure_name[pos])):
        pos -= 1
    pure_name = pure_name[0:pos+1]
    return pure_name


def Analyze(file_list, name_list, ext_list):
    for f in file_list:
        pure_name = GetPureName(f)
        ext = GetExtension(f)
        if name_list.has_key(pure_name) == True:
            tmp_val = name_list[pure_name]
            name_list[pure_name] = tmp_val + 1
        else:
            name_list[pure_name] = 1
            ext_list[pure_name] = ext

    for n in name_list:
        cnt = name_list[n]
        digi_cnt = DigitCount(cnt)
        # while cnt > 1:
        #    cnt /= 10
        #    digi_cnt += 1
        name_list[n] = digi_cnt


def main(argv):

    name_list = {}
    ext_list = {}
    print (len(argv))
    # for e in argv:
    #     print e
    dir = argv[0] + "/"
    file_list = os.listdir(dir)
    Analyze(file_list, name_list, ext_list)

    for f in file_list:
        pure_name = GetPureName(f)
        seq_num = GetSequenceNumber(f)
        # print seq_num
        total_digi_cnt = name_list[pure_name]
        seq_digi_cnt = DigitCount(seq_num)
        digi_dif = total_digi_cnt - seq_digi_cnt
        padded_num = ""
        while digi_dif > 0:
            digi_dif -= 1
            padded_num += "0"
        padded_num += str(seq_num)
        final_name = pure_name + padded_num + "." + ext_list[pure_name]
        os.rename(dir+f, dir+final_name)
        # print final_name


if __name__ == "__main__":
    main(sys.argv[1:])
