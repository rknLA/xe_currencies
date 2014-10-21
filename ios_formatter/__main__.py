from __future__ import unicode_literals
import sys

if __name__ == '__main__':
  import formatter
  from xe import scraper
  currencies = scraper.currencies_and_symbols()
  formatted = formatter.format_for_obj_c(currencies)
  args = sys.argv
  if (len(args) > 0):
    with open(args[1], 'wb') as f:
      f.write(formatted.encode('utf-8'))
  else:
    print formatted
