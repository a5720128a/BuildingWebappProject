from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        
        # Chris heard about MBTI test
        # He want to know his personality
        # to check out its homepage
        browser.get('http://localhost:8000')
        
        # He notices the page title "Index"
        self.assertIn('Index', self.browser.title)

        # He clicked play button
        link = self.browser.find_element_by_tag_name("play")
        link.click()
	
	# He notices the page title "MBTI Test"
	self.assertIn('MBTI Test', self.browser.title)
	# He answer the test
        # He choosed all green choices
        for i in range(1,41):
            browser.find_elements_by_css("input[type='radio'][id="+i+"][value>0]").click
        
        # He type his name "Chris" and his facebook "Chris Deedee"
        inputbox = self.browser.find_element_by.name('addPlayer')
        inputbox.send_keys('Chris')
        inputbox2 = self.browser.find_element_by.name('add_Facebook')
        inputbox.send_keys('Chris Deedee')
	link = self.browser.find_elements_by_class_name("button button1")
        link.click()
        
        # He notices the page title "Result"
        self.assertIn('Result', self.browser.title)
        # He found he is "ESTJ"
        # He clicked info button
        html_source = browser.page_source
        if "ESTJ" in html_source:
            link = self.browser.find_element_by_tag_name("info")
            link.click()
        else:
            self.fail('fail')

        # The page linked to his personality
        self.assertIn('ESTJ', self.browser.title)

        # He found his facebook below
        # He clicked "ESFJ" for see Get along well with personality
        if "Chris Deedee" in html_source:
            link = self.browser.find_element_by_tag_name("ESFJ")
            link.click()
        else:
            self.fail('fail')
        

        # He visits index agian and clicked about
        link = self.browser.find_element_by_tag_name("home")
        link.click()
        # He notices the page title "About"
        link = self.browser.find_element_by_tag_name("about")
        link.click()

        # He goes back to sleep
	self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
