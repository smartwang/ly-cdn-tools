desc
-----------------

当前仅实现了阿里云CDN的资源预热功能，后续功能待开发


install
-----------------

`pip install ly-cdn-tools`


example
----------

```
    from ly_cdn_tools.warmup.aliyun import AliyunManager
    
    ak = os.getenv("AK", "")
    
    secret = os.getenv("SECRET", "")
    
    region = os.getenv("REGION", "")
    
    url_file = os.getenv("URL_FILE", "")
    
    manager = AliyunManager(ak=ak, secret=secret, region=region)
    
    manager.warn_up(url_file)
``` 
