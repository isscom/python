def get_unic(my_list):
    unic = []
    for i in range(len(my_list)):
        if my_list[i] not in my_list[i+1::] and my_list[i] not in my_list[:i-1:]:
            unic.append(my_list[i])
    return unic