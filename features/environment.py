from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application
# from selenium.webdriver.chrome.options import ChromeOptions
# from selenium.webdriver.chrome.service import Service


def browser_init(context):
    """
    :param context: Behave context
    """
    # context.driver = webdriver.Chrome()
    # context.driver = webdriver.Safari()
    context.driver = webdriver.Firefox()

    # HEADLESS MODEg
    # service = Service('/Users/willsterling/careerist/wc-qa_auto-cureskin/chromedriver')
    #
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # context.driver = webdriver.Chrome(
    #     chrome_options=options,
    #     service=service
    # )

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(context.driver)

def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
