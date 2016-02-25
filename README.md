# PolishIDCard
A tiny tool to generate a fake polish id card (document) number for testing purposes.

Based on the data from [this article](https://en.wikipedia.org/wiki/Polish_identity_card).

# Usage
```python
from polishidcard import PolishIDCard
card = PolishIDCard()

# generate a new random card number
card.generate()
'JON554756'

# get an already generated number
card.get()
'JON554756'

# you can set own card number if you wish
card.set('ABC123456')
card.get()
'ABC123456'

# validate an existing id card number length & check digit
card.validate('ABC123456')
False

card.validate('XGG765762')
True
```
# Useful tools
* [tiny-pesel-generator](https://github.com/dwabece/tiny-pesel-generator) - polish person identification number generator
