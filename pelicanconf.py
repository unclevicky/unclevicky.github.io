AUTHOR = 'unclevicky'
SITENAME = '田冲憨娃'
SITEURL = ""

PATH = "content"

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("从0开始学AI", "https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzkxMTIzMzk0Mg==&action=getalbum&album_id=3937704618716561416#wechat_redirect"),
    ("Rabbit & Bear", "https://xiongyiduoduo.top/rabbitBear/"),
    #("Pelican", "https://getpelican.com/"),
    #("Python.org", "https://www.python.org/"),
    #("Jinja2", "https://palletsprojects.com/p/jinja/"),
    #("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("CSDN", "https://blog.csdn.net/MissYourKiss/"),
    #("You can add links in your config file", "#"),
    #("Another social link", "#"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# For old site used dated permalinks
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
