import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://zorgvinder.menzis.nl/")
    page.get_by_placeholder("Bijvoorbeeld: Fysiotherapie").click()
    page.get_by_placeholder("Bijvoorbeeld: Fysiotherapie").fill("Ziekenhuis")
    page.get_by_placeholder("Bijvoorbeeld: Fysiotherapie").press('Space')  # Simuleer een spatiebalkdruk
    page.wait_for_selector('text="Ziekenhuis / ZBC"')  # Wacht tot de tekst "Ziekenhuis / ZBC" zichtbaar is
    page.get_by_text("Ziekenhuis / ZBC").click()
    page.get_by_placeholder("Postcode of woonplaats").click()
    page.get_by_placeholder("Postcode of woonplaats").fill("Bedum")
    page.get_by_placeholder("Postcode of woonplaats").press('Space')  # Simuleer een spatiebalkdruk
    page.get_by_text("Bedum").click()
    page.get_by_role("combobox").select_option("50")
    page.get_by_role("button", name="Zoeken").click()
