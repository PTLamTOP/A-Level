
class FourDigitYearConverter:
    regex = '[0-9]{4}'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return '%04d' % value

# nnsss
class TwoDigitThreeLetter:
    regex = '\d{2}\w{3}'

    def to_python(self, value):
        return str(value)

    def to_url(self, value):
        return str(value)

# /n-s-n/
class TestWithHyphen:
    regex = '\d{1}[-]\w{1}[-]\d{1}'

    def to_python(self, value):
        return str(value)

    def to_url(self, value):
        return str(value)

# /099-602-52-41/
class PhoneNumber:
    regex = '0(3|6|9|5)([0-4]|[6-9])-\d{3}-\d{2}-\d{2}'

    def to_python(self, value):
        return str(value)

    def to_url(self, value):
        return str(value)

