
import os

# is_debug_server = os.environ.get('SERVER_SOFTWARE', '').startswith('Dev')
# operating_system = os.environ.get("OS", "")
# is_windows = operating_system.startswith("Windows")


# if is_debug_server and not is_windows:
#    import google
#    google.__path__ = ['/Users/okku/dev/NicoleServer/lib/google','/Library/Python/2.7/site-packages/google']
#    google.cloud.__path__ = ['/Users/okku/dev/NicoleServer/lib/google/cloud','/Library/Python/2.7/site-packages/google/cloud']

from google.appengine.ext import vendor
vendor.add('lib')
