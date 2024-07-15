import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://www.booking.com/")
    page.get_by_placeholder("Where are you going?").click()
    page.get_by_role("button", name="Texel Netherlands").click()
    page.get_by_label("24 August").click()
    page.get_by_label("31 August").click()
    page.get_by_role("button", name="Search").click()
    with page.expect_popup() as page1_info:
        page.get_by_role("link", name="Landgoed Hotel Tatenhove").click()
    page1 = page1_info.value
