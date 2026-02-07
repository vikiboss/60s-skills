# Skills Index - 技能索引

Complete list of all available skills with their capabilities.

## 📊 Skills Overview

| Skill Name | Category | Tools Count | Main Features |
|------------|----------|-------------|---------------|
| 60s-daily-news | Information | 1 | Daily curated news (15 items + quote) |
| weather | Information | 2 | Real-time weather & forecasts |
| hot-topics | Social | 6 | Hot searches from major platforms |
| utility-tools | Utility | 7 | IP, translate, QR, hash, OG, WHOIS, password |
| fun-content | Entertainment | 6 | Quotes, jokes, luck, memes |
| data-info | Data | 7 | Exchange rates, calendar, history, encyclopedia |
| music-movies | Entertainment | 7 | Music charts, lyrics, box office |

## 🔍 Detailed Skills Breakdown

### 1. 60s-daily-news

**技能名称：** 每日新闻 60 秒

**描述：** 获取每日精选新闻，包含 15 条国内外重要新闻和每日微语

**工具列表：**

#### get_daily_news
- **功能：** 获取每日新闻
- **参数：**
  - `date` (可选): 日期 YYYY-MM-DD 格式
  - `encoding` (可选): 输出格式 (json/text/markdown/image/image-proxy)
- **返回：** 新闻列表、日期、农历、微语等
- **示例：**
  ```json
  {
    "encoding": "json"
  }
  ```

**适用场景：**
- 聊天机器人新闻推送
- 每日简报生成
- 网站新闻模块
- 邮件订阅服务

---

### 2. weather

**技能名称：** 天气信息

**描述：** 查询中国各地实时天气和天气预报

**工具列表：**

#### get_realtime_weather
- **功能：** 获取实时天气
- **参数：**
  - `location` (必需): 地点名称（如"北京"、"上海"）
- **返回：** 温度、湿度、风速、空气质量等

#### get_weather_forecast
- **功能：** 获取天气预报
- **参数：**
  - `location` (必需): 地点名称
- **返回：** 多日天气预报

**适用场景：**
- 智能助手天气查询
- 出行规划建议
- 天气预警提醒

---

### 3. hot-topics

**技能名称：** 热门话题

**描述：** 获取各大中文平台的热搜榜单和热门内容

**工具列表：**

#### get_weibo_hot_search
- **功能：** 微博热搜榜
- **返回：** 当前微博热搜话题列表

#### get_zhihu_hot_topics
- **功能：** 知乎热榜
- **返回：** 知乎热门问题和话题

#### get_baidu_hot_search
- **功能：** 百度热搜
- **返回：** 百度搜索热词

#### get_douyin_hot_topics
- **功能：** 抖音热点
- **返回：** 抖音热门视频和话题

#### get_toutiao_hot_news
- **功能：** 今日头条热榜
- **返回：** 头条热门新闻

#### get_bili_trending
- **功能：** B站热门
- **返回：** B站热门视频

**适用场景：**
- 舆情监控
- 内容创作参考
- 趋势分析
- 社交媒体管理

---

### 4. utility-tools

**技能名称：** 实用工具

**描述：** 各种实用工具集合

**工具列表：**

#### lookup_ip_info
- **功能：** IP 地址查询
- **参数：** `ip` (可选) - IP地址，不提供则查询请求者IP
- **返回：** IP归属地、ISP等信息

#### translate_text
- **功能：** 文本翻译
- **参数：**
  - `text` (必需): 待翻译文本
  - `from` (可选): 源语言代码，默认 auto
  - `to` (可选): 目标语言代码，默认 en
- **返回：** 翻译结果

#### generate_qrcode
- **功能：** 生成二维码
- **参数：**
  - `text` (必需): 要编码的文本或URL
  - `size` (可选): 二维码尺寸，默认 200
- **返回：** 二维码图片

#### calculate_hash
- **功能：** 计算哈希值
- **参数：**
  - `text` (必需): 待哈希文本
  - `algorithm` (可选): 算法 (md5/sha1/sha256/sha512)
- **返回：** 哈希值

#### get_og_metadata
- **功能：** 提取网页 OG 元数据
- **参数：** `url` (必需) - 网页URL
- **返回：** 标题、描述、图片等元数据

#### get_whois_info
- **功能：** WHOIS 域名查询
- **参数：** `domain` (必需) - 域名
- **返回：** 域名注册信息

#### generate_password
- **功能：** 生成随机密码
- **参数：**
  - `length` (可选): 密码长度，默认 16
  - `numbers/lowercase/uppercase/symbols` (可选): 包含字符类型
- **返回：** 随机密码

**适用场景：**
- 网络工具
- 开发辅助
- 信息安全
- 文本处理

---

### 5. fun-content

**技能名称：** 娱乐内容

**描述：** 各种有趣的娱乐内容

**工具列表：**

#### get_hitokoto
- **功能：** 一言（随机名言）
- **参数：** `category` (可选) - 分类
- **返回：** 随机名言、出处

#### get_dad_joke
- **功能：** 英文爸爸笑话
- **返回：** 随机英文笑话

#### get_duanzi
- **功能：** 中文段子
- **返回：** 随机搞笑段子

#### get_luck_prediction
- **功能：** 运势预测
- **返回：** 今日运势

#### get_kfc_meme
- **功能：** KFC疯狂星期四文案
- **返回：** 梗文案

#### get_moyu_calendar
- **功能：** 摸鱼日历
- **返回：** 摸鱼日历图片

**适用场景：**
- 聊天娱乐
- 内容填充
- 社交互动
- 心情调节

---

### 6. data-info

**技能名称：** 数据信息

**描述：** 各类数据查询服务

**工具列表：**

#### get_exchange_rate
- **功能：** 汇率查询
- **参数：**
  - `from` (可选): 源货币代码
  - `to` (可选): 目标货币代码
- **返回：** 实时汇率

#### get_lunar_calendar
- **功能：** 农历转换
- **参数：** `date` (可选) - 日期
- **返回：** 农历日期、生肖、节气等

#### get_today_in_history
- **功能：** 历史上的今天
- **参数：** `month`, `day` (可选)
- **返回：** 历史事件列表

#### search_encyclopedia
- **功能：** 百科搜索
- **参数：** `keyword` (必需) - 搜索关键词
- **返回：** 百科条目信息

#### get_fuel_price
- **功能：** 油价查询
- **参数：** `province` (可选) - 省份
- **返回：** 各类燃油价格

#### get_gold_price
- **功能：** 金价查询
- **返回：** 各类黄金价格

#### search_chemical
- **功能：** 化学元素查询
- **参数：** `query` (必需) - 元素名/符号/原子序数
- **返回：** 元素详细信息

**适用场景：**
- 数据查询
- 知识问答
- 信息检索
- 学习辅助

---

### 7. music-movies

**技能名称：** 音乐影视

**描述：** 音乐和影视相关信息查询

**工具列表：**

#### get_netease_music_rank
- **功能：** 网易云音乐榜单列表
- **返回：** 所有榜单信息

#### get_netease_music_rank_detail
- **功能：** 榜单详情
- **参数：** `id` (必需) - 榜单ID
- **返回：** 榜单歌曲列表

#### search_lyrics
- **功能：** 歌词搜索
- **参数：** `keyword` (必需) - 歌曲名或歌手
- **返回：** 歌词内容

#### get_maoyan_all_movies
- **功能：** 所有电影信息
- **返回：** 电影数据库

#### get_maoyan_realtime_movie_boxoffice
- **功能：** 实时电影票房
- **返回：** 票房排行

#### get_maoyan_realtime_tv_ratings
- **功能：** 实时电视剧收视率
- **返回：** 收视率排行

#### get_maoyan_realtime_web_series
- **功能：** 实时网剧排行
- **返回：** 网剧热度排行

**适用场景：**
- 娱乐推荐
- 音乐查询
- 影视信息
- 票房追踪

---

## 🔧 技能使用指南

### 选择合适的技能

根据您的需求选择合适的技能：

1. **信息获取** → 60s-daily-news, weather, data-info
2. **社交趋势** → hot-topics
3. **工具辅助** → utility-tools
4. **娱乐互动** → fun-content, music-movies

### 集成方式

1. **MCP格式** - 适用于 Claude 等支持 MCP 的平台
2. **OpenAI格式** - 适用于 ChatGPT、GPT-4
3. **LangChain格式** - 适用于 LangChain 框架

### API调用限制

- 大部分接口使用智能缓存，响应速度快
- 公共实例无明确速率限制
- 建议合理使用，避免滥用
- 生产环境建议自行部署

---

## 📚 更多资源

- [快速开始指南](../examples/QUICKSTART.md)
- [API文档](https://docs.60s-api.viki.moe)
- [源代码](https://github.com/vikiboss/60s)
