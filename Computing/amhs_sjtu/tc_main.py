import tc_class_sets
import tc_in
import tc_assign
import tc_out
import warnings

class Amhs():
    def __init__(self) -> None:
        self.runBool = True
        pass
    
    # 开启数据
    def start(self):
        d = tc_class_sets.Dataset()
        self.Node = d
        if d.pattern == 1:
            d = tc_in.generating(d)
            d = tc_assign.task_assign_new(d)
        elif d.pattern == 0:
            d = tc_in.generating(d)
            d = tc_assign.task_assign_new(d)
    
    # 关闭数据库
    def over(self):
        tc_out.output_close_connection(self.d)
        
    # 暂停数据库读取
    def setRunBool(self,bool=True):
        self.Node.runBool = bool

