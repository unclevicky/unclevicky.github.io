AUTHOR = 'unclevicky'
SITENAME = '田冲憨娃'
SITEURL = "https://xiongyiduoduo.top"

PATH = "content"

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("宝藏推荐：从0开始学AI", "https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzkxMTIzMzk0Mg==&action=getalbum&album_id=3937704618716561416#wechat_redirect"),
    ("宝藏推荐：Rabbit & Bear", "https://xiongyiduoduo.top/rabbitBear/"),
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

# For static assets
STATIC_PATHS = ['images', 'photos', 'pdfs', 'extra']

# Tell Pelican to move the CNAME file to the root of the output folder.
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
}

# For themes
THEME = 'themes/Flex'
## Show the main menu
MAIN_MENU = True
## This is the new setting to add the navigation menu
MENUITEMS = (
    ('Archives', '/archives.html'),
    ('Categories', '/categories.html'),
    ('Tags', '/tags.html'),
)
## Tell Pelican to generate page for archives, categories and tags
DIRECT_TEMPLATES = ['index', 'categories', 'authors', 'archives', 'tags']

# For Plugins
PLUGINS = ['photos']
## photos
### 图片存储目录（在content下创建）
PHOTO_LIBRARY = 'content/photos'
### 缩略图尺寸（宽x高，单位px，按比例缩放）
PHOTO_THUMB = (250, 180, 60)
### 大图最大尺寸（避免图片过大影响加载）
PHOTO_GALLERY = (1200, 900, 85)           
### 可选：图片加水印（按需开启）
PHOTO_WATERMARK = False
PHOTO_WATERMARK_TEXT = "田冲憨娃"
### 确保使用正确的URL路径
PHOTO_URL = '/photos/'
PHOTO_LIBRARY_URL = '/photos/'
### 启用内联图片和画廊
PHOTO_INLINE_ENABLED = True
PHOTO_INLINE_GALLERY_ENABLED = True
### 移除复杂的PHOTO_PROFILES配置，使用默认配置
# 文件名后缀问题将通过其他方式解决

# 确保在所有平台上都使用正斜杠
PHOTO_LIBRARY = PHOTO_LIBRARY.replace('\\', '/')
PHOTO_URL = PHOTO_URL.replace('\\', '/')
PHOTO_LIBRARY_URL = PHOTO_LIBRARY_URL.replace('\\', '/')