import pytest

class TestDemo(object):
    '''
    1、pytest执行以test开头的function
    2、断言的不同形式
    3、skip和skipif(需要有condition判断)
    4、xfail 方法中则后续语句不执行；方法前则方法会执行，根据断言显示为xfail或xpassed
    '''
    def test001(self):
        print('first to print')
        assert 1==1

    @pytest.mark.skip(reason='just skip this case') # skip 后可填写原因
    def test005(self):
        assert 1==1
    
    def test002(self):
        str='china'
        assert 'h' in str

    isRun='N'
    @pytest.mark.skipif(isRun=='N',reason='Y执行，N跳过') # 根据变量判断是否跳过
    def test003(self):
        tag=True
        assert  tag
       
    def test004(self):
        l1={1,2,3,4}
        assert {2,3,4}==l1
    
    def test_xfail(self):
        print('--day day up---start')
        pytest.xfail(reason='not finished')  # 后续语句不执行
        print('--good good study--end')
        assert 1==1
    
    @pytest.mark.xfail()
    def test005(self):
        print('xpassed but excute')
        assert 1==1   # 执行并且被标记为xpassed

    @pytest.mark.xfail()
    def test006(self):
        print('xfailed but excute')
        assert 1==2 # 执行并且被标记为xfailed

if __name__ == "__main__":
    pytest.main(['-sr','Learning/pytest/test_demo1.py'])