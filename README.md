# Selenium WebDriver
> A small suite of Selenium WebDriver tests against the x-kom.pl online store — comparing listed and basket prices, and tracking the priciest item in a category across runs.

## What it does
* `first_test.py` – finds the most expensive smartwatch in a category and compares it against the result from the previous run, stored in `results.csv`
* `second_test.py` – adds a single product to the basket and checks its price matches what's shown in the basket
* `third_test.py` – adds two products to the basket and checks their combined price matches the basket total
* `product.py` – a small `Product` class with overloaded comparison operators (`==`, `<`, `>`); not used by the three tests above

## Setup
```
pip install -r requirements.txt
python first_test.py   # or second_test.py / third_test.py
```
Uses the bundled `drivers/chromedriver.exe`, so a matching local Chrome install is expected.

## Status
**Archived** — not actively maintained. The tests rely on hardcoded XPath selectors written against x-kom.pl's 2019 page layout, so they'll likely no longer work against the current site.

Written in mid-2019 as a coursework project to practice UI test automation with Selenium.
