import pytest
'''
--html=路径/报告名称.html
'''

class TestDemo7(object):
    
    def test001(self):
        print('\n白日依山尽')
        assert 1==1
    def test002(self):
        print('\n黄河入海流')
        assert 1==2
    def test003(self):
        print('\n欲穷千里目')
        assert 1==1
    def test004(self):
        print('\n更上一层楼')
        assert 1==3
        
if __name__ == "__main__":
   pytest.main(['-s',__file__,'--html=Learning/pytest/report/report.html','--self-contained-html'])

