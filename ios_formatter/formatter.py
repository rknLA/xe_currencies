OUTPUT_PRE_TEXT = 'NSDictionary *currencyMap = @{\n'
CURRENCY_ITEM_FORMAT = '    @"%s": @{\n\
        @"symbol": @"%s",\n\
        @"name": @"%s",\n\
        @"abbrev": @"%s"\n\
    }'
ITEM_SEPARATOR = ',\n'
OUTPUT_POST_TEXT = '};'

def format_for_obj_c(currencies):
  output = OUTPUT_PRE_TEXT
  formatted_currencies = []
  for currency in currencies:
    formatted = CURRENCY_ITEM_FORMAT % (currency['abbrev'],
                                        currency['symbol'],
                                        currency['name'],
                                        currency['abbrev'])
    formatted_currencies.append(formatted)
  body = ITEM_SEPARATOR.join(formatted_currencies)
  output += body
  output += OUTPUT_POST_TEXT
  return output
