import random
import urllib.request
def down_pic(url):
    name = random.randrange(1,1000)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url,full_name)
down_pic("http://img5.poco.cn/mypoco/myphoto/20080724/4521774520080724234149098_640.jpg")
