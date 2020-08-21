import pytest
'''
用例之间都是独立的，没有先后顺序，随机都能执行，可重复运行不 影响其他用例 
.在windows下想用多进程的选pytst-xdist； 想用多线程的选pytest-parallel
xdist 不支持多线程  适合多目录结果下的用例一起执行
xdist -n=X 进程数；
parallel '--workers=x','--tests-per-worker=y' x为进程数(windows下只能为1) y为线程数  

conftest.py
│  __init__.py
│              
├─baidu
│  │  conftest.py
│  │  test_1_baidu.py
│  │  test_2.py
│  │  __init__.py 
│          
├─blog
│  │  conftest.py
│  │  test_2_blog.py
│  │  __init__.py  
'''

class TestDemo6(object):
    
    def test001(self):
        print('\ntest000000001')
        assert 1==1
        
if __name__ == "__main__":
   pytest.main(['-s','-n=3'])
   #  pytest.main(['-s','--workers=1','--tests-per-worker=4',__file__])
