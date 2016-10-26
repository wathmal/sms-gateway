# sms-gateway

## install
```
pip install flask
pip install git+https://github.com/pmarti/python-messaging.git
```


## running on startup
add following to `/etc/rc.local` file.
```
nohup python /home/pi/projects/sms-gateway/server.py >/home/pi/sms.log 2>&1 &
```

[related blog post](http://wathmal.me/blog/create-your-own-sms-gateway/)