# 60s Skills - AI Agent Skills Collection

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Source API](https://img.shields.io/badge/Source-vikiboss%2F60s-blue)](https://github.com/vikiboss/60s)

A collection of [Agent Skills](https://agentskills.io) for the [60s API](https://github.com/vikiboss/60s).

## About

This repository contains skills that enable AI agents to work with the 60s API, providing access to daily news, weather, trending topics, utilities, entertainment, data queries, and media information.

## What are Agent Skills?

[Agent Skills](https://agentskills.io) are a simple, open format for giving agents new capabilities and expertise. They are folders of instructions, scripts, and resources that agents can discover and use to perform better at specific tasks.

## Repository Structure

```
60s-skills/
├── skills/                    # Individual skills directory
│   ├── daily-news-60s/       # Daily news skill
│   ├── weather-query/        # Weather information
│   ├── hot-topics/           # Trending content
│   ├── utility-tools/        # Translation, IP, QR, etc.
│   ├── entertainment/        # Fun content
│   ├── data-query/           # Exchange rates, calendar, etc.
│   └── media-info/           # Music and movie info
├── README.md                 # This file
└── LICENSE                   # MIT License
```

## Available Skills

### 1. daily-news-60s
获取每天60秒读懂世界的每日新闻，包含15条精选国内外新闻和每日微语。

Get daily curated news with 15 selected items and a daily quote, updated every 30 minutes.

**Use when**: Users need daily news summaries, current events, or want to stay informed.

### 2. weather-query
查询中国各地实时天气和天气预报，包括温度、湿度、风速、空气质量等信息。

Query real-time weather and forecasts for locations in China including temperature, humidity, wind, and air quality.

**Use when**: Users ask about weather conditions, forecasts, or climate information.

### 3. hot-topics
获取微博、知乎、百度、抖音、今日头条、B站等主流平台的实时热搜榜单。

Get trending topics and hot searches from major Chinese platforms (Weibo, Zhihu, Baidu, Douyin, Toutiao, Bilibili).

**Use when**: Users want to know what's trending on social media.

### 4. utility-tools
提供实用工具功能，包括IP查询、文本翻译、二维码生成、哈希计算、网页元数据提取、WHOIS查询和密码生成。

Utility functions including IP lookup, translation, QR code generation, hashing, OG metadata extraction, WHOIS, and password generation.

**Use when**: Users need translation, IP lookup, QR codes, or other utility functions.

### 5. entertainment
获取娱乐内容，包括一言名句、笑话、段子、运势预测、KFC梗文案和摸鱼日历。

Fun content including quotes, jokes, luck predictions, memes, and slacking calendars.

**Use when**: Users want entertainment, jokes, quotes, or fun content.

### 6. data-query
查询各类数据信息，包括汇率、农历、历史事件、百科、油价、金价和化学元素。

Query various data including exchange rates, lunar calendar, historical events, encyclopedia, fuel/gold prices, and chemical elements.

**Use when**: Users need reference data, currency conversion, calendar info, or encyclopedia lookups.

### 7. media-info
获取音乐和影视信息，包括网易云音乐排行榜、歌词搜索、电影票房、电视剧收视率和网剧排行。

Get music and entertainment information including music charts, lyrics, movie box office, TV ratings, and web series rankings.

**Use when**: Users need music charts, lyrics, movie info, or entertainment rankings.

## Using Skills

Skills in this repository follow the [Agent Skills specification](https://agentskills.io/specification). Each skill:

- Has a unique name following the format: `[a-z0-9-]+`
- Contains a `SKILL.md` file with YAML frontmatter and instructions
- Provides clear guidance on when and how to use the skill
- Includes code examples and use cases

## About 60s API

[60s API](https://github.com/vikiboss/60s) is a collection of high-quality, open-source APIs providing:

- 📰 Daily news (60 seconds to read the world)
- 🌤️ Weather information and forecasts
- 🔥 Trending topics from major platforms
- 🛠️ Utility tools (IP, translation, QR codes, etc.)
- 🎉 Entertainment content (jokes, quotes, memes)
- 📊 Data queries (exchange rates, calendar, encyclopedia)
- 🎵 Music and movie information

**Features:**
- ✅ Free, no authentication required
- ✅ Millisecond-level cached responses
- ✅ Global CDN acceleration
- ✅ Regular updates
- ✅ High-quality curated data

## Quick Start

### For AI Agents

Simply provide agents access to the skills in this repository. Each `SKILL.md` file contains all the information needed to use that skill effectively.

### For Developers

Each skill provides:
- Clear API endpoint documentation
- Python code examples
- Common use cases
- Best practices
- Troubleshooting tips

Example from `daily-news-60s`:

```python
import requests

response = requests.get('https://60s.viki.moe/v2/60s')
news = response.json()

print(f"📰 {news['date']} 新闻简报")
for i, item in enumerate(news['news'], 1):
    print(f"{i}. {item['title']}")
```

## Contributing

Contributions are welcome! To add improvements:

1. Fork this repository
2. Make your changes to skills or add new skills
3. Ensure each skill follows the Agent Skills specification
4. Submit a pull request

When creating new skills:
- Use lowercase with hyphens for directory names
- Include YAML frontmatter in SKILL.md
- Provide clear instructions and examples
- Test with actual API endpoints

## Related Resources

- **60s API Project**: https://github.com/vikiboss/60s
- **API Documentation**: https://docs.60s-api.viki.moe
- **Official Instance**: https://60s.viki.moe
- **Agent Skills Specification**: https://agentskills.io/specification

## License

This repository is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

The 60s API project is also licensed under MIT.

---

Made with ❤️ for the AI Agent Community
