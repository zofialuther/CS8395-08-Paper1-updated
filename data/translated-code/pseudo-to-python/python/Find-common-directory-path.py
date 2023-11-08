import os
paths = ['/home/user1/tmp/coverage/test', '/home/user1/tmp/covert/operator', '/home/user1/tmp/coven/members']
result = os.path.commonprefix(paths)
print(result)