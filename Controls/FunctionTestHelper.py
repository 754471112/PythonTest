class FunctionTestHelper(object):
    def __init(self):
        pass
    #字符串格式化
    def __strFormatTest(self):
        print("Hellp %s,%s"%("Mic","this is you Code"))
    #可变集合list
    def __listTest(self):
        tempLst=[1,"2",3,"this is str"]#list,可变集合
        tempValue1=tempLst[1]
        tempValue2=tempLst[3]
        print("输出:%s;输出2:%s,当前list长度%s"%(tempValue1,tempValue2,len(tempLst)))
        tempLst.append("this is str2")
        print("当前list长度%s"%(len(tempLst)))
        tempValue3= tempLst.pop(0)
        print("当前list长度%s,移除的值%s"%(len(tempLst),tempValue3))
        # tempLst.remove(1)  没有remove方法
        # print("当前list长度%s"%(len(tempLst)))
        print("完成list测试")
    #不可变集合tuple
    def __tupleTest(self):
        #tuple初始化后变无法修改
        tempTuple=("1",1,'测试')
        tempValue1=tempTuple[0]
        tempValue2=tempTuple[2]
        print("输出%s;输出2:%s"%(tempValue1,tempValue2))
        tempTuple2=(1,)#初始化只有一个元素1的tuple写法
        tempValue3=tempTuple2[0]
        print("输出%s"%(tempValue3))
        print("完成tuple测试")
    #条件判断
    def __conditionJudTest(self):
        
        age = input("请输入年龄:")#input输入时默认为str类型
        age=int(age)
        if age>=18:
            print("已成年")
        else:
            print("未成年")
    #循环
    def __loopTest(self):
        sumValue = 0
        for fcValue in range(5):
            sumValue += fcValue
        print("累加结果:%s" % (sumValue))
        whileValue = 0
        while whileValue < 10:
            whileValue = whileValue+1
            print("while循环中,当前值%s" % (whileValue))
            print("循环测试结束")
    #字典dict
    def __dictTest(self):
        print("开始字典测试")
        tempDic={1:"值1",2:"值2","test":"testStr"}
        tempDic[3]="值三"
        print("当前字典长度:%s"%(len(tempDic)))
        if 1 in tempDic:
            print("Key(1)存在于字典中")
        tempKeyValue=tempDic.get("1","test")
        print("取出的值:%s"%(tempKeyValue))
        tempKeyValue2=tempDic.pop("test")
        print("当前字典长度:%s,移除的值:%s"%(len(tempDic),tempKeyValue2))
        print("字典测试结束")
    #集合set
    def __setTest(self):
        #初始化方法
        tempSet = set([1, 2, 3, 4, 5, 6, 6, 7])
        #自动过滤重复的元素,可用于数学中的交集、并集操作
        print(tempSet)
        tempSet.add(10)  # 新增元素操作
        tempSet.remove(6)  # 移除元素操作
        print(tempSet)

        tempSet2 = set([1, 11])
        resultSet = tempSet & tempSet2  # 交集
        print(resultSet)
        resultSet = tempSet | tempSet2  # 并集
        print(resultSet)
        print("set测试结束")
    #数据类型转换
    def __dataTypeChangeTest(self):
        int("123")#将字符串转换为int类型
        str(1.2345)#将数字转换为int类型

        value1=255
        changeResult=hex(value1)
        print("整数转换为十六进制字符串:%s"%(changeResult))
        changeResult=int(changeResult,16)
        print("十六进制字符串转换为整数:%s"%(changeResult))
        print("数据类型转换测试结束")
    #参数检查测试
    def __paramCheckTest(self,varParam1):
        
        if not isinstance(varParam1,(str)):
            print("参数有误")
        else:
            print("参数正确")
        print("参数检查测试结束")
    #多参数返回测试
    def __multiReturnTest(self):

        print("开始进行多参数返回测试")
        result1=1
        result2="测试"
        return result1,result2
    #默认参数测试
    def __defaultParamTest(self,name="TestName"):
        if name=="TestName":
            print("参数为默认值")
        else:
            print("传入新的参数")
        print("默认参数测试结束")
    #可变参数
    def __canChangeParamTest(self,*param):
        for fcValie in param:
            print(fcValie)

        print("可变参数测试结束")
    #关键字参数
    def __keyParamTest(self, **param):
        if "value1" in param:
            print("参数‘value1’传入,值为:%s"%(param["value1"]))
        else:
            print("未传入参数名为‘value1’的参数")
        print(param)

    #-------------------------------公共方法---------------------------------------

    def startTest(self):
        # param="Test"
        # self.__paramCheckTest(param)
        #self.__dataTypeChangeTest()
        
        # result=self.__multiReturnTest()
        # print(result)
        #可变参数方法调用
        # testParam=[1,2,3,4,5]
        # self.__canChangeParamTest(*testParam)
        # self.__canChangeParamTest(1,2,3,4,5)
        #关键字参数方法调用
        #self.__keyParamTest(value3="123", value1=32)
        #self.__defaultParamTest("TestName2")
        return
