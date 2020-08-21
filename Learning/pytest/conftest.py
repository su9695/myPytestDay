import pytest
'''
不同层级的conftest 文件，作用域也不同
'''
@pytest.fixture(scope='module',autouse=True) # autouse 自动调用该fixture
def  moudleFixture():
    print('\n----hello everyone-----')

@pytest.fixture(scope='class')
def  classFixture():
    print('\n每个类运行开始前都要打印')
    yield
    print('\n每个类运行结束后都要打印!!!!')

@pytest.fixture(scope='function')
def funcFixture():
    print('\n每个方法运行开始前都要打印')
    yield
    print('\n每个方法运行结束后都要打印')

@pytest.fixture
def useFixture(funcFixture):
    '''
    funcFixture yield之前--useFixture yield之前--用例---useFixture yield之后---funcFixture yield之后
    '''
    print('\nhello 我是useFixture yield之前')
    yield
    print('\nhello 我是useFixture yield之后')

@pytest.fixture
def addFinalizerFixture1(request):
    print('\n我是addFinalizerFixture1前面的打印')
    def afterFinalizerFixture1():
        print('\n我是addFinalizerFixture1后面的打印')
    def afterFinalizerFixture2():
        print('\n我是addFinalizerFixture2后面的打印')
    def afterFinalizerFixture3():
        print('\n我是addFinalizerFixture3后面的打印')
    # 注册afterFinalizerFixture 函数
    request.addfinalizer(afterFinalizerFixture1)
    request.addfinalizer(afterFinalizerFixture2)
    request.addfinalizer(afterFinalizerFixture3)


@pytest.fixture(scope='module')
def getInfo(request):
    info=request.param
    print('\nconftest获取的数据%s'%info)
    return info

