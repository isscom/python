# СМОТРЕЛА КАК РАБОТАТЬ С CSV
# f = open('database.csv','w',encoding='utf-8')
# f.writelines('id')
# f.writelines(';')
# f.writelines('name' + '\n')
# f.writelines('123')
# f.writelines(';')
# f.writelines('name' + '\n')
# f.close()

def read_file(file, mod):
    f = open(file, mod) #encoding='utf-8')
    data = f.read().splitlines()
    list = []
    for line in data:
        line = line.split(';')
        list.append(line)
    f.close()
    print(list[1,1])
    return list
# if __name__== '__main__':
data = 'processing_model.csv'
print(read_file(data, 'r'))
