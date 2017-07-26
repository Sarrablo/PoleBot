# PoleBot

Version 0.1: <br/>

## Features Availables:
Post message <br/>
Read "General" main page

## Usage:
Load Api:
<br/>
```
from fcgapi import FcGuerrillaApi
api = FcGuerrillaApi()
```

Post message: <br/>
```
url = 'https://www.forocoches.com/foro/showthread.php?t=1338462'
message = 'Hello world!'
api.post_message(url,message)
```

Get general main page:<br/>
It returns a Link list.<br/>
 - Link<br/>
   - link<br/>
   - text<br/>
   - answ<br/>
```
api.get_general_main()
```
