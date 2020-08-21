import pytest

oneList=['Lily','Luke',33,'susu']

class TestDemo4(object):
   
    @pytest.mark.parametrize('getInfo',oneList,indirect=True) 
    def test_printName(self,getInfo):
        info=getInfo
        print('\n111用例获取的数据为%s'%info)
        assert 'Luke'==info

        
if __name__ == "__main__":
    pytest.main(['-s','Learning/pytest/test_demo4.py'])
