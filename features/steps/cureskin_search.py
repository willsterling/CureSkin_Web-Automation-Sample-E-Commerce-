from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then

@given('Open shop_cureskin main page')
def open_cureskin(context):
    context.app.main_page.open_main()

@when('Input text into main-search-bar {search_word}')
def input_search_word(context, search_word):
    context.app.header.input_search_text(search_word)

@when('Click search icon')
def click_search_button(context):
    context.app.header.click_search()

@when('Close pop up')
def close_popup(context):
    context.app.main_page.close_popup()


@then('Verify search results are shown')
def verify_search_results(context):
    context.app.search_results_page.verify_search_results_shown()

