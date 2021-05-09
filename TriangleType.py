s = float(input('tell me the first straight segment '))
s2 = float(input('tell me the second straight segment '))
s3 = float(input('tell me the third straight segment '))
if s < s2 + s3 and s2 < s + s3 and s3 < s + s2:
    print('i could be a triangle')
    if s != s2 and s != s3 and s2 != s3:
        print('And it would be an scalene triangle')
    elif s == s2 and s == s3:
        print('And it would be an equilateral triangle')
    elif s == s2 or s == s3 or s2 == s3:
        print('And it would be a isosceles triangle')
else:
    print('it could not be a triangle')
