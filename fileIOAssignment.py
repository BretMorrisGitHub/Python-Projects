import os
import time
for file in os.listdir('C:\\B\\'):
    if file.endswith('.txt'):
        timeStamp = os.path.getmtime(os.path.join('C:\\B\\', file))
        convert_time = time.localtime(timeStamp)
        format_time = time.strftime('%d%m%Y', convert_time)
        print(os.path.join('C:\\B\\', file), format_time)
