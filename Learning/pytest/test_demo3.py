import pytest
'''
fixture 配合conftest.py 使用
1、fixture的scope 有作用范围：
function：默认范围，每一个函数或方法都会调用，不填写时便是它
class：每一个类调用一次
module: 每一个.py文件调用一次，文件中可以有多个function和class
session：多个文件调用一次，可以跨文件，如在.py文件中，每一个.py文件就是module
范围：
session > module > class > function
2、fixture的自动应用autouse
3、conftest中定义多个fixture，一个fixture可以是另一个fixture的前后置，期间还是用field隔开前后置
执行顺序为 前fixture yield之前的代码——引用前fixture的fixture yield之前的代码--用例代码--引用前fixture的fixture yield之后的代码---前fixture yield之后的代码
4、fixture 中的yield 前置和后置 可以用于登录，数据库连接等
5、addfinalizer 也可以起到yield相同的作用：但addfinalizer可以注册使用多次
6、yield 在setup报错后，不会继续执行；但addfinalizer 在setup报错后 可继续执行后续语句
'''
@pytest.mark.usefixtures('classFixture')
@pytest.mark.usefixtures('funcFixture')
class TestDemo3(object):
    def testFixture1(self):
        print('我是方法运行的情况')
        assert 1==1

@pytest.mark.usefixtures('useFixture')
class TestDemo3B(object):
    def testFixture2(self):
        print('我是方法运行的情况2222')
        assert 1==1

@pytest.mark.usefixtures('addFinalizerFixture1')
class TestDemo3C(object):
    def testFixture2(self):
        print('我是方法运行的情况33333')
        assert 1==1
        
if __name__ == "__main__":
    pytest.main(['-s','Learning/pytest/test_demo3.py'])
