import re
import time
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://menzis.nl/zorgvinder")
    # page.get_by_role("button", name="Accept All Cookies").click()
    time.sleep(3)
    page.get_by_placeholder("Bijvoorbeeld: Fysiotherapie").click()
    time.sleep(2)
    page.get_by_placeholder("Bijvoorbeeld: Fysiotherapie").fill("Ziekenhuis")
    # Simuleer een spatie
    page.keyboard.press("Space")
    time.sleep(2)  # even wachten om ervoor te zorgen dat het effect heeft
    page.get_by_text("Ziekenhuis / ZBC").click()
    time.sleep(3)
    page.get_by_placeholder("Postcode of woonplaats").click()
    page.get_by_placeholder("Postcode of woonplaats").fill("Bedum")
    # Simuleer een spatie
    page.keyboard.press("Space")
    time.sleep(2)  # even wachten om ervoor te zorgen dat het effect heeft
    page.get_by_text("Bedum").click()
    page.get_by_role("combobox").select_option("50")
    page.get_by_role("button", name="Zoeken").click()
    time.sleep(3)
