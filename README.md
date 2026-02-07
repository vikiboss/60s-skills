# 60s Skills - AI Agent Skills Collection

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Source API](https://img.shields.io/badge/Source-vikiboss%2F60s-blue)](https://github.com/vikiboss/60s)

将 [60s API](https://github.com/vikiboss/60s) 转换为各大 AI Agent 平台支持的技能定义格式。

Convert the [60s API](https://github.com/vikiboss/60s) capabilities into standardized skill definitions for major AI agent platforms.

## 📚 什么是 60s API? | What is 60s API?

60s API 是一个高质量、开源、可靠的开放 API 集合，提供了丰富的数据获取能力，包括：

60s API is a high-quality, open-source collection of APIs providing rich data capabilities including:

- 📰 每日新闻（每天 60 秒读懂世界）
- 🌤️ 天气信息和预报
- 🔥 各大平台热搜榜（微博、知乎、百度等）
- 🎵 音乐排行榜和歌词搜索
- 🎬 电影票房和影视排行
- 🛠️ 实用工具（IP查询、翻译、二维码生成等）
- 🎉 娱乐内容（笑话、运势、名言等）
- 📊 数据查询（汇率、农历、历史上的今天等）

## 🎯 项目目的 | Project Purpose

本项目将 60s API 的能力转换为标准化的 Agent Skills 定义，使其可以被各大 AI Agent 平台直接使用：

This project converts 60s API capabilities into standardized agent skill definitions for use with major AI platforms:

- 🤖 **MCP (Model Context Protocol)** - Claude, Anthropic AI systems
- 🔧 **OpenAI Function Calling** - ChatGPT, GPT-4
- 🦜 **LangChain Tools** - LangChain framework
- 🌐 **OpenAPI/Swagger** - Universal API specification

## 📁 项目结构 | Project Structure

```
60s-skills/
├── skills/
│   ├── mcp/              # MCP格式技能定义 (Model Context Protocol)
│   │   ├── 60s-daily-news.json
│   │   ├── weather.json
│   │   ├── hot-topics.json
│   │   ├── utility-tools.json
│   │   ├── fun-content.json
│   │   ├── data-info.json
│   │   └── music-movies.json
│   ├── openai/           # OpenAI Function Calling 格式
│   │   ├── 60s-daily-news.json
│   │   └── weather.json
│   └── langchain/        # LangChain Tools 格式
├── examples/             # 使用示例
└── docs/                 # 详细文档
```

## 🚀 快速开始 | Quick Start

### 使用 MCP 格式 (Claude, Anthropic)

```json
{
  "mcpServers": {
    "60s-daily-news": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-fetch"],
      "env": {
        "FETCH_CONFIG": "./skills/mcp/60s-daily-news.json"
      }
    }
  }
}
```

### 使用 OpenAI Function Calling

```python
import openai
import json

with open('skills/openai/60s-daily-news.json', 'r') as f:
    skill_def = json.load(f)

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "获取今天的新闻"}],
    functions=[skill_def]
)
```

## 📖 可用技能列表 | Available Skills

### 1. 60s Daily News (60s-daily-news)
获取每日精选新闻 - 15 条国内外新闻 + 每日微语

**主要功能：**
- ✅ 获取最新每日新闻
- ✅ 查询历史日期新闻
- ✅ 支持多种格式输出（JSON、文本、Markdown、图片）

**API端点：** `GET /v2/60s`

### 2. Weather Information (weather)
天气信息查询 - 实时天气和多日预报

**主要功能：**
- ✅ 实时天气查询
- ✅ 多日天气预报
- ✅ 空气质量信息

**API端点：** 
- `GET /v2/weather/realtime`
- `GET /v2/weather/forecast`

### 3. Hot Topics (hot-topics)
各大平台热搜榜单

**主要功能：**
- ✅ 微博热搜
- ✅ 知乎热榜
- ✅ 百度热搜
- ✅ 抖音热点
- ✅ 今日头条
- ✅ B站热门

### 4. Utility Tools (utility-tools)
实用工具集合

**主要功能：**
- ✅ IP地址查询
- ✅ 文本翻译
- ✅ 二维码生成
- ✅ 哈希计算
- ✅ OG元数据提取
- ✅ WHOIS查询
- ✅ 随机密码生成

### 5. Fun Content (fun-content)
娱乐内容

**主要功能：**
- ✅ 一言（随机名言）
- ✅ 英文笑话
- ✅ 中文段子
- ✅ 运势预测
- ✅ KFC疯狂星期四文案
- ✅ 摸鱼日历

### 6. Data Info (data-info)
数据信息查询

**主要功能：**
- ✅ 汇率查询
- ✅ 农历转换
- ✅ 历史上的今天
- ✅ 百科搜索
- ✅ 油价查询
- ✅ 金价查询
- ✅ 化学元素查询

### 7. Music & Movies (music-movies)
音乐和影视信息

**主要功能：**
- ✅ 网易云音乐排行榜
- ✅ 歌词搜索
- ✅ 猫眼电影信息
- ✅ 实时票房
- ✅ 电视剧收视率
- ✅ 网剧排行

## 💻 使用示例 | Usage Examples

### 示例 1: 获取每日新闻

```bash
# 直接调用API
curl "https://60s.viki.moe/v2/60s?encoding=json"

# 使用Agent Skill
# Agent会自动调用 get_daily_news 函数
User: "给我看看今天的新闻"
Agent: [调用 60s-daily-news skill] → 返回15条新闻
```

### 示例 2: 查询天气

```bash
# 直接调用API
curl "https://60s.viki.moe/v2/weather/realtime?location=北京"

# 使用Agent Skill
User: "北京今天天气怎么样？"
Agent: [调用 weather skill 的 get_realtime_weather] → 返回天气信息
```

### 示例 3: 翻译文本

```bash
# 使用Agent Skill
User: "把'Hello World'翻译成中文"
Agent: [调用 utility-tools skill 的 translate_text] → 返回"你好世界"
```

## 🔧 技能定义格式说明 | Skill Definition Format

### MCP 格式结构

```json
{
  "name": "skill-name",
  "version": "1.0.0",
  "description": "Skill description",
  "protocol": "mcp",
  "tools": [
    {
      "name": "function_name",
      "description": "Function description",
      "inputSchema": {
        "type": "object",
        "properties": { /* parameters */ }
      },
      "endpoint": {
        "url": "https://api.example.com/endpoint",
        "method": "GET"
      }
    }
  ],
  "metadata": { /* additional info */ }
}
```

### OpenAI 格式结构

使用标准的 OpenAPI 3.0 规范，包含：
- API 基本信息
- 服务器地址
- 路径和操作定义
- 参数和响应模式

## 🌟 特性 | Features

- ✅ **多平台支持** - MCP, OpenAI, LangChain 等主流格式
- ✅ **完整文档** - 每个技能都有详细的参数说明和示例
- ✅ **标准化** - 遵循各平台的技能定义规范
- ✅ **开箱即用** - 可直接导入到支持的Agent平台
- ✅ **持续更新** - 跟随 60s API 更新

## 📝 贡献指南 | Contributing

欢迎贡献！如果你想添加新的技能定义或改进现有定义：

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/new-skill`)
3. 提交更改 (`git commit -am 'Add new skill'`)
4. 推送到分支 (`git push origin feature/new-skill`)
5. 创建 Pull Request

## 🔗 相关链接 | Related Links

- **60s API 源项目**: https://github.com/vikiboss/60s
- **API 文档**: https://docs.60s-api.viki.moe
- **官方实例**: https://60s.viki.moe
- **MCP 文档**: https://modelcontextprotocol.io
- **OpenAI Function Calling**: https://platform.openai.com/docs/guides/function-calling

## 📄 许可证 | License

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情

原始 60s API 项目同样采用 MIT 许可证

## 🙏 致谢 | Acknowledgments

- 感谢 [vikiboss](https://github.com/vikiboss) 创建和维护 60s API
- 感谢所有为 60s API 做出贡献的开发者
- 感谢各大 AI Agent 平台提供的技能标准

## 📮 联系方式 | Contact

- 问题反馈: [GitHub Issues](https://github.com/vikiboss/60s-skills/issues)
- 原 API 问题: [60s Issues](https://github.com/vikiboss/60s/issues)

---

Made with ❤️ for the AI Agent Community
