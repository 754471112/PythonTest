#enum测试(定义等)
from enum import Enum,unique
@unique
class DataType(Enum):
    LockUnLock=0
    LiftLimit=1
    SpeedLimit=2

if __name__=="__main__":
    dataType=DataType.LockUnLock
    if dataType==DataType.LockUnLock:
        print("锁车解锁")
    else:
        print("其他")
