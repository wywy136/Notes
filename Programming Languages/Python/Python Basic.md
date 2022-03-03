# Python积累

- 在确定了类的属性固定的情况下，可以使用`__slots__`来优化内存。
  - 方式：参见《数据结构预算法-python》P170

## 爬虫

### urllib

获取url下的网页，通过get：

```python
rsp = urllib.request.urlopen("http://www.baidu.com")
print(rsp.read().decode('utf-8'))
```

通过post：

```python
data = bytes(urllib.parse.urlencode({"hello": "word"}), encoding="utf-8")
rsp = urllib.request.urlopen("http://httpbin.org/post", data=data)
```

### BeautifulSoup

```python
from bs4 import BeautifulSoup
html = file.read().decode("utf-8")
bs = BeautifulSoup(html, "html.parser")

# 搜索所有与字符串s完全符合的内容
bs.find_all('s') 

# 正则表达式搜索
t = bs.find_all(re.compile('s'))

# kwargs搜索
t = bs.find_all(id='s')

# 通过select
t = bs.select(a)
```

