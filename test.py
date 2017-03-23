import rpn
result = rpn.calculate("1 1 +")
assert(2 == result)
result = rpn.calculate("2 0 -")
assert(2 == result)
result = rpn.calculate("2 0 ^")
assert(1 == result)

