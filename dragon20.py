import os, platform
try:
   import requests
except:
   os.system('pip2 install requests')

import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from dragon20 import subscribe
    subscribe()
elif bit == '32bit':
    from dragon20 import subscribe
    subscribe()