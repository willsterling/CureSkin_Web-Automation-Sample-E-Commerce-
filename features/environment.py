from app.application import Application

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service


#Allure general command:
# behave - f
# allure_behave.formatter: AllureFormatter - o
# allure_test_results / features /
#Note: command to show Allure results: allure serve allure_test_results


def browser_init(context, test_name):
    """
    :param context: Behave context
    """
    # service = Service('/Users/willsterling/careerist/wc-qa_auto-cureskin/chromedriver')
    # context.driver = webdriver.Chrome()
    # context.driver = webdriver.Safari()
    # context.driver = webdriver.Firefox()

    # HEADLESS (start)--
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # options.add_argument("--window-size=1920,1080")
    # options.add_argument("--start-maximized")
    #
    # context.driver = webdriver.Chrome(
    #     chrome_options=options,
    #     service=Service('/Users/willsterling/careerist/wc-qa_auto-cureskin/chromedriver')
    # )
    # HEADLESS (end)---


    # Browerstack Tests:

    bs_user = 'williamchavers_oMdC0R'
    bs_key = 'ufnR7pWam9aybY7Rb2wh'

    desired_cap = {
        'browserName': 'Firefox',
        'bstack:options': {
            'os': 'Windows',
            'osVersion': '10',
            'sessionName': test_name
        }
    }
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)

    # context.driver.maximize_window()
    context.driver.implicitly_wait(5)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(context.driver)

def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name )


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
