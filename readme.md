Run dev
----
/System/Library/Frameworks/Python.framework/Versions/2.7/bin/python /Users/okku/dev/google-cloud-sdk/bin/dev_appserver.py --port 4350 --host 127.0.0.1 --admin_port 9002 /Users/okku/dev/passepartout_hosting

### Pip

```bash
pip install -t lib --upgrade -r requirements.txt
```

Upload to server
---
- Build prod in passepartout project
- update /Users/okku/dev/passepartout_hosting