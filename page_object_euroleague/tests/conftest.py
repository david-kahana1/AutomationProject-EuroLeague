import os

import allure
import pytest
from playwright.sync_api import sync_playwright

from page_object_euroleague.config import BROWSER, IS_HEADLESS, BASE_URL, CONTEXT_SETTINGS, BROWSER_ARGS

from page_object_euroleague.pages.home_page import homePage
from page_object_euroleague.pages.players_page import playersPage
from page_object_euroleague.pages.teams_page import teamsPage


def pytest_runtest_makereport(item, call):
    if "setup_euroleague" in item.fixturenames:
        if call.when == "call":
            item.rep_call = call

            if call.excinfo is not None:
                page = getattr(item, "page", None)
                if page:
                    allure.attach(
                        page.screenshot(),
                        name="Failure screenshot",
                        attachment_type=allure.attachment_type.PNG
                    )


@pytest.fixture

def setup_euroleague(request):
    with sync_playwright() as p:
        if BROWSER == "Chromium": browser = p.chromium.launch(headless=IS_HEADLESS, **BROWSER_ARGS)
        else: browser = p.firefox.launch(headless=IS_HEADLESS)
        context = browser.new_context(**CONTEXT_SETTINGS)
        page = context.new_page()

        page.goto(BASE_URL)
        page.wait_for_load_state("networkidle")
        try:
            page.locator("button:has-text('Reject All Cookies')").click(timeout=10000)
        except Exception as e:
            print(f"Cookie banner not shown - continuing. Error: {e}")

        request.node.page = page

        home_page = homePage(page)
        players_page = playersPage(page)
        teams_page = teamsPage(page)

        yield page, home_page, players_page, teams_page
        print("### Test End ###")
        context.close()
        browser.close()



@pytest.fixture(scope="session", autouse=True)

def create_allure_environment():
    os.makedirs("allure-results", exist_ok=True)
    env_file = os.path.join("allure-results", "environment.properties")

    browser = BROWSER
    headless = "True" if IS_HEADLESS else "False"
    environment = "QA"

    with open(env_file, "w") as f:
        f.write(f"Environment={environment}\n")
        f.write(f"Browser={browser}\n")
        f.write(f"Headless={headless}\n")
        f.write(f"URL={BASE_URL}\n")
