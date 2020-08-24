import pytest
import allure

@allure.feature('omplogin-分销商登录')
class TestDemo8_omplogin(object):
    
    @allure.story('omp登录有效类')
    @allure.title('1111111111111')
    @allure.severity('Normal')
    @allure.step('输入正确的用户名和密码')
    def test_loginYXL(self):
        '''
        用例描述：输入正确的用户名和密码可正常登录
        '''
        print('我是有效类1111')
        assert 1==1
    
    @allure.story('omp登录无效类')
    @allure.title('2222222222222')
    @allure.severity('Critical')
    @allure.issue('http://www.baidu.com',name='链接地址')
    @allure.testcase('http://obp.888ly.cn',name='bug地址')
    @allure.step('输入错误的用户名和密码组合')
    def test_loginWXL(self):
        '''
        用例描述：用户名+密码 各种错误或者为空的组合验证
        '''
        with allure.step('输入用户名'):
            print('我是无效类1111')
        with allure.step('输入密码'):
            print('输入密码')
        with allure.step('输入错误的用户名{0}，输入正确的密码{1}'.format(None,'abc123')):
            print('33333333333')
        with open(r'C:\Users\suqiangqiang\Desktop\33.png','rb') as f:
            file=f.read()
            allure.attach(file,'登录无效类--用户名为空',allure.attachment_type.PNG) 
        assert 1==1


        
if __name__ == "__main__":
   pytest.main(['-s',__file__,'--alluredir','Learning/pytest/report/'])


