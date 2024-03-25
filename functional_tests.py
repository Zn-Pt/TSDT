from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):

        # 张三听说有一个很棒的办事列表的应用
        # 他去看了这个应用的首页
        self.browser.get('http://localhost:8000')

        # 他注意到浏览器的标题包含“To-Do”这个词
        self.assertIn('To-Do', self.browser.title, "browser title was:" + self.browser.title)
        self.fail('Finish the test!')

        # 应用邀请他输入一个办事列表的文本框

        # 他在文本框输入了“Buy flowers"

# 他访问那个URL，发现他的待办事项列表还在
# 他感到非常满足

if __name__ == '__main__':
    unittest.main()
