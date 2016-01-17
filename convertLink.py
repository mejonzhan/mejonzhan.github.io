# -*- coding: utf-8 -*-

def main():
    
    file = input("输入要处理的文件名：")
    selectData = excel_table_byindex(file)
    sortedKeyList = get_sort_data_key(selectData)
    write_table_to_excel(0, sortedKeyList, selectData)
        
#     for i in selectData: 
#         print ("dict[%s]=" % i, selectData[i])
    

if __name__=="__main__":
    main()
