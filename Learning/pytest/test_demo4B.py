import pytest
'''
1、通过conftest中 getInfo  request.param 获取[] 数据源的数据，如果是纯list 则直接使用；若果是list嵌套其他形式的数据，需要二次提取
2、[{},{}] 此类数据类型是从excel 读取封装的；还需要一个 excel 第一行key 返回的list，用作ids
3、pytest.mark.parametrize('getInfo',moreList,indirect=True) 第一个参数为conftest中函数名称，第二个为excel获取的封装数据；第三个参数是把第一个参数当做函数运行
'''


moreList=[{'name':'suqiangqiang','age':30,'phone':'15895557475'},{'name':'Luke','age':22,'phone':'13852403166'}]

ids=['name','age','phone']

class TestDemo4B(object):

    @pytest.mark.parametrize('getInfo',moreList,indirect=True) 
    def test_printName(self,getInfo):
        info1=getInfo[ids[0]]
        info2=getInfo[ids[1]]
        info3=getInfo[ids[2]]
        print('姓名为%s'%info1)
        print('年龄为%s'%info2)
        print('电话为%s'%info3)
        
if __name__ == "__main__":
    pytest.main(['-s','Learning/pytest/test_demo4B.py'])
