import pytest
'''
1、-m 配合mark 后的标记，可以只执行标记的用例；-m not 则不执行标记的用例
2、A/B::C::C1 模式可以只执行指定的类或方法
3、-k 'A and B' 'A or B'  'B'  'not B'  模糊匹配类和方法名称  and 是 类且方法； or 是 类或方法； 单独B或not B 则只模糊匹配方法名称
'''
class TestDemo2(object):

    def test1(self):
        print('我是func 1')
        assert 1==1

    @pytest.mark.website
    def test2(self):
        print('我是func 2')
        assert 2==3
      
class TestDemo2B(object):

    def test1B(self):
        print('我是func 1B')
        assert 1==1

    def test2B(self):
        print('我是func 2B')
        assert 2==3  

    def testtest2B(self):
        print('我是func 222B')
        assert 2==2  


if __name__ == "__main__":
    #pytest.main(['-sv','Learning/pytest/test_demo2.py','-m=website'])  
    #pytest.main(['-sv','Learning/pytest/test_demo2.py::TestDemo2B']) # 只执行TestDemo2B 类
    #pytest.main(['-sv','Learning/pytest/test_demo2.py::TestDemo2B::test1B']) # 只执行TestDemo2B类中test1B方法
    #pytest.main(['-svk','TestDemo2 and test1']) # 只执行类名称包含TestDemo2 且方法名称中包含test1的测试用例,模糊匹配到 TestDemo2下的test1和TestDemo2B下的test1B
    #pytest.main(['-svk','TestDemo2B or test1']) # 执行类包含关键字TestDemo2B下所有的方法；或者其他类中方法包含test1 的用例
    pytest.main(['-svk',' test2'])  #执行方法名称不包含test2的用例