aa_name_dict = {}
fin=open('aa_name_dic.txt','r')
for input_string in fin:
    table=input_string.split(',')
    aa_name_dict[table[0]]=table[1].strip('\n')
print aa_name_dict
