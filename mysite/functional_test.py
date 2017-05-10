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
        self.fail('Finish the test!')
        
        # He clicked play button
	
	# He notices the page title "MBTI Test"
	self.assertIn('Index', self.browser.title)
	# He answer the test
        # He choosed all green choices

        # He type his name "Chris" and his facebook "Chris Deedee"

        # He notices the page title "Result"
        # He found he is "ESTJ"
        # He clicked info button

        # The page linked to his personality

        # He found his facebook below
        # He clicked "ESFJ" for see Get along well with personality

        # He visits index agian and clicked about
        # He notices the page title "About"

        # He goes back to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')
