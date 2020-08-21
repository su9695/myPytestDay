import pytest
'''
 @pytest.mark.run(order=)   按照设定的顺序执行
 @pytest.mark.flaky(reruns=3,reruns_delay=1) 失败后重跑 重跑间隔设置

'''

class TestDemo5(object):
    
    def test001(self):
        print('\ntest000000001')
        assert 1==1
    @pytest.mark.run(order=1)   
    def test004(self):
        print('\ntest000000004')
        assert 1==1
    @pytest.mark.run(order=2)   
    @pytest.mark.flaky(reruns=3,reruns_delay=1) # 失败后再重新跑3次;每次重跑间隔1秒
    def test002(self):
        print('\ntest000000002')
        assert 1==2
    
    def test003(self):
        print('\ntest000000003')
        pytest.assume(1==2)
        pytest.assume(1==3)
        pytest.assume(1==1)

        
if __name__ == "__main__":
  #  pytest.main(['-s','--reruns=4','Learning/pytest/test_demo5.py'])  作用和mark.flaky(reruns=X)相同
    pytest.main(['-s','Learning/pytest/test_demo5.py'])
