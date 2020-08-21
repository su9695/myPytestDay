import pytest
'''
用例之间都是独立的，没有先后顺序，随机都能执行，可重复运行不 影响其他用例 
.在windows下想用多进程的选pytst-xdist； 想用多线程的选pytest-parallel
xdist 不支持多线程
xdist -n=X 进程数；
parallel   '--workers=x','--tests-per-worker=y' x为进程数(windows下只能为1) y为线程数  
'''

class TestDemo5(object):
    
    def test001(self):
        print('\ntest000000001')
        assert 1==1
    def test002(self):
        print('\ntest000000002')
        assert 1==1
    def test003(self):
        print('\ntest000000003')
        assert 1==1
    def test004(self):
        print('\ntest000000004')
        assert 1==2
    def test005(self):
        print('\ntest000000005')
        assert 1==1
    def test006(self):
        print('\ntest000000006')
        assert 1==1
    def test007(self):
        print('\ntest000000007')
        assert 1==1
    def test008(self):
        print('\ntest000000008')
        assert 1==1
    def test009(self):
        print('\ntest000000009')
        assert 1==1
    def test0010(self):
        print('\ntest0000000010')
        assert 1==2
        
if __name__ == "__main__":
   pytest.main(['-s','-n=3'])
   #  pytest.main(['-s','--workers=1','--tests-per-worker=4',__file__])
