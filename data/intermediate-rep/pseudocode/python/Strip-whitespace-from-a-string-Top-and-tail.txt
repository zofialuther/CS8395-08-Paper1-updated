s = ' \t \r \n String with spaces  \t  \r  \n  '
output1 = s.lstrip()  # 'String with spaces  \t  \r  \n  '
output2 = s.rstrip()  # ' \t \r \n String with spaces'
output3 = s.strip()  # 'String with spaces'