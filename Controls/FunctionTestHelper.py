class FunctionTestHelper(object):
    def __init(self):
        pass
    def __strFormatTest(self):
        print("Hellp %s,%s"%("Mic","this is you Code"))

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
    #---------------------公共方法-------------------------------
    def startTest(self):

        self.__tupleTest()