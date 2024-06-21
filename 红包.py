'''
   0__________$1_________________$2__________$3________$4_____$..._________$n________max
list[0]     list[1]           list[2]      list[3]   list[4]            list[n]   list[n+1]
           第1个线段          第2个线段   第3个线段  第4个线段          第n个线段   

如果将最大值max视为一个从0开始的线段 如果在线段上任意分部n个点 
则可知的 n个点组成的n+1个子线段长度之和等于max 而每个子线段长度是相邻两个点的值之差。

翻译成红包的逻辑 n+1个子线段就是红包数量 每个子线段长度就是红包的数值。

'''



import random
def hongbao(total,num): #num就是红包数
    if num*0.01>total:
        print('国小')
        return None
    else:
        result=[]
        lst=random.sample(range(1,int(total*100)),num-1) 
        #生成中间的随机数元素，元素数量即列长度为num减一(下标为0到num减二)

        lst.append(0) #增加值为0的数列初始元素
        lst.append(total*100) #增加值为最大值的数列末尾元素
        lst.sort()  #从小到大排序，最左边为0最右边为max
        # 此时列表长度为num+1（下标为0到num）print(len(lst),lst[0],lst[num])

        for i in range(1,len(lst)): #i的范围从1开始，到len(lst)的小一个数，即红包数
        #当i=1，线段为list[1]-list[0],即第2个元素减第1个元素，即第1个线段长度
        #当i=红包数时，刚好list[红包数]就是最后一个元素，list[num]-list[num-1]的线段也是最后一个
            result=(lst[i]-lst[i-1])/100
            print(result)
        
       
print(hongbao(100,20))
