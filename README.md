# SMS-Gateway

## Install
```
pip install flask
pip install git+https://github.com/pmarti/python-messaging.git
```

## Setting env variables
Set username and password as environment variables.
```
export SMS_GATEWAY_USER=username
export SMS_GATEWAY_PASS=yourpassword
```

## Running on startup
Add following to `/etc/rc.local` file.
```
nohup python /home/pi/projects/sms-gateway/server.py >/home/pi/sms.log 2>&1 &
```

[Related blog post](http://wathmal.me/blog/create-your-own-sms-gateway/)
