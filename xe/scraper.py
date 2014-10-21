from lxml import html
from lxml.cssselect import CSSSelector
import re
import urllib2


CurrencyRowSelector = CSSSelector('.cSmbl_bx tbody tr.row1, tr.row2')
CurrencyNameSelector = CSSSelector('td :first-child')
CurrencyAbbrevSelector = CSSSelector('td :nth-child(2)')
CurrencySymbolSelector = CSSSelector('td.cSmbl_Fnt_AU')

def currencies_and_symbols():
  '''Scrape xe.com and output a list of currencies and their symbols.'''
  tree = html.parse('http://www.xe.com/symbols.php')
  root = tree.getroot()
  currency_rows = CurrencyRowSelector(root)
  alphabetical_currencies = []
  for currency in currency_rows:
    country_currency = CurrencyNameSelector(currency)[0].text
    abbrev = CurrencyAbbrevSelector(currency)[0].text
    symbol = CurrencySymbolSelector(currency)[0].text
    alphabetical_currencies.append({
      'name': country_currency,
      'abbrev': abbrev,
      'symbol': symbol
    })

  import json
  return json.dumps(alphabetical_currencies)
