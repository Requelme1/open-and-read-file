import os

def new_file():
    text1 = '1.txt'
    text2 = '2.txt'
    text3 = '3.txt'
    os.chdir('sorted')
    out_file = 'new_file.txt'
    file1 = os.path.join(os.getcwd(), text1)
    file2 = os.path.join(os.getcwd(), text2)
    file3 = os.path.join(os.getcwd(), text3)
    with open(file1, 'r', encoding='UTF-8') as f1:
        file1_ = f1.readlines()
    with open(file2, 'r', encoding='UTF-8') as f2:
        file2_ = f2.readlines()
    with open(file3, 'r', encoding='UTF-8') as f3:
        file3_ = f3.readlines()
    with open(out_file, 'w', encoding='UTF-8') as f_total:
        if len(file1_) < len(file2_) and len(file1_) < len(file3_):
            f_total.write(text1 + '\n')
            f_total.write(str(len(file1_)) + '\n')
            f_total.writelines(file1_)
            f_total.write('\n')
        elif len(file2_) < len(file1_) and len(file2_) < len(file3_):
            f_total.write(text2 + '\n')
            f_total.write(str(len(file2_)) + '\n')
            f_total.writelines(file2_)
            f_total.write('\n')
        elif len(file3_) < len(file1_) and len(file3_) < len(file2_):
            f_total.write(text3 + '\n')
            f_total.write(str(len(file3_)) + '\n')
            f_total.writelines(file3_)
            f_total.write('\n')
        if len(file2_) > len(file1_) > len(file3_) or len(file2_) < len(file1_) < len(file3_):
            f_total.write(text1 + '\n')
            f_total.write(str(len(file1_)) + '\n')
            f_total.writelines(file1_)
            f_total.write('\n')
        elif len(file1_) > len(file2_) > len(file3_) or len(file2_) > len(file1_) and len(file2_) < len(file3_):
            f_total.write(text2 + '\n')
            f_total.write(str(len(file2_)) + '\n')
            f_total.writelines(file2_)
            f_total.write('\n')
        elif len(file1_) > len(file3_) > len(file2_) or len(file3_) > len(file1_) and len(file3_) < len(file2_):
            f_total.write(text3 + '\n')
            f_total.write(str(len(file3_)) + '\n')
            f_total.writelines(file3_)
            f_total.write('\n')
        if len(file1_) > len(file2_) and len(file1_) > len(file3_):
            f_total.write(text1 + '\n')
            f_total.write(str(len(file1_)) + '\n')
            f_total.writelines(file1_)
        elif len(file2_) > len(file1_) and len(file2_) > len(file3_):
            f_total.write(text2 + '\n')
            f_total.write(str(len(file2_)) + '\n')
            f_total.writelines(file2_)
        elif len(file3_) > len(file1_) and len(file3_) > len(file2_):
            f_total.write(text3 + '\n')
            f_total.write(str(len(file3_)) + '\n')
            f_total.writelines(file3_)
        else:
            return 'FAIL'
        return
print(new_file())