#调用其他Python文件测试

#from文件，import类
from Controls.CommonDataHelper import CommonDataHelper
#Controls.CommonDataHelper文件中的CommonDataHelper类
commonDataHelper=CommonDataHelper()
resultShow=commonDataHelper.GetName("TestName")
print(resultShow)

#同上
from Controls.PhotoHelper import PhotoManager
photoHelper=PhotoManager()
resultShow=photoHelper.GetPhotoPro("C:/A/c.jpg")
print(resultShow)

#导入Controls.LocationHelper文件中的所有类、方法等
# from Controls.LocationHelper import *
#导入Controls.LocationHelper文件中的StartTest方法
#from Controls.LocationHelper import StartTest
#导入Controls.LocationHelper文件，如果不使用as，则调用时写法为Controls.LocationHelper.StartTest()
import Controls.LocationHelper as Location
resultShow= Location.StartTest()
print(resultShow)
