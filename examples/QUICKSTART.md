# Quick Start Guide - 快速入门指南

## 🚀 5分钟上手 | Get Started in 5 Minutes

### Step 1: 选择你的平台 | Choose Your Platform

根据你使用的 AI Agent 平台选择对应的技能格式：

| 平台 / Platform | 格式 / Format | 目录 / Directory |
|----------------|--------------|-----------------|
| Claude Desktop, Anthropic AI | MCP | `skills/mcp/` |
| ChatGPT, GPT-4 | OpenAI Function Calling | `skills/openai/` |
| LangChain Framework | Custom Integration | See examples |

### Step 2: 克隆仓库 | Clone Repository

```bash
git clone https://github.com/vikiboss/60s-skills.git
cd 60s-skills
```

### Step 3: 配置技能 | Configure Skills

#### 方案 A: Claude Desktop (MCP)

1. 找到配置文件：
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`

2. 添加技能（示例）：

```json
{
  "mcpServers": {
    "60s-news": {
      "command": "node",
      "args": ["/path/to/your/mcp-server.js"],
      "env": {
        "SKILL_PATH": "/path/to/60s-skills/skills/mcp/60s-daily-news.json"
      }
    }
  }
}
```

3. 重启 Claude Desktop

#### 方案 B: OpenAI Function Calling (Python)

```python
import openai
import json

# 读取技能定义
with open('skills/openai/60s-daily-news.json', 'r') as f:
    skill = json.load(f)

# 在 ChatCompletion 中使用
response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "获取今天的新闻"}],
    functions=[skill]
)
```

#### 方案 C: 直接调用 API

最简单的方式 - 直接使用 HTTP 请求：

```bash
# 获取今日新闻
curl "https://60s.viki.moe/v2/60s"

# 查询天气
curl "https://60s.viki.moe/v2/weather/realtime?location=北京"
```

### Step 4: 测试技能 | Test Skills

#### 测试新闻技能

**用户提问：**
- "今天有什么新闻？"
- "给我看看今天的每日简报"
- "获取2024-01-15的新闻"

**预期行为：** Agent 应该调用 `get_daily_news` 函数并返回15条新闻

#### 测试天气技能

**用户提问：**
- "北京今天天气怎么样？"
- "上海明天会下雨吗？"

**预期行为：** Agent 调用 `get_realtime_weather` 或 `get_weather_forecast`

## 📚 推荐学习路径 | Learning Path

### 初学者 | Beginners

1. ✅ 阅读 [README.md](../README.md) 了解项目概况
2. ✅ 查看 [技能索引](../docs/SKILLS_INDEX.md) 了解所有可用技能
3. ✅ 尝试直接调用 API（使用 curl）
4. ✅ 选择一个平台，配置一个技能

### 进阶用户 | Advanced Users

1. ✅ 研究 [使用示例](USAGE.md) 中的代码
2. ✅ 配置多个技能，创建综合应用
3. ✅ 了解技能定义格式，创建自定义技能
4. ✅ 集成到自己的项目中

### 开发者 | Developers

1. ✅ 阅读 [60s API 源码](https://github.com/vikiboss/60s)
2. ✅ 理解技能定义的 JSON Schema
3. ✅ 为其他 API 创建类似的技能定义
4. ✅ 贡献新的技能或改进现有技能

## 🎯 常见用例 | Common Use Cases

### 用例1: 每日新闻机器人

```python
# 简单的新闻机器人示例
import requests

def daily_briefing():
    # 获取新闻
    news = requests.get('https://60s.viki.moe/v2/60s').json()
    
    # 格式化输出
    print(f"📰 {news['date']} 新闻简报\n")
    for i, item in enumerate(news['news'], 1):
        print(f"{i}. {item['title']}")
    
    print(f"\n💭 {news['tip']}")

daily_briefing()
```

### 用例2: 天气提醒助手

```python
def weather_reminder(city):
    weather = requests.get(
        'https://60s.viki.moe/v2/weather/realtime',
        params={'location': city}
    ).json()
    
    print(f"☁️ {city}今日天气：{weather['weather']}")
    print(f"🌡️ 温度：{weather['temperature']}°C")
    
    # 根据天气给出建议
    if '雨' in weather['weather']:
        print("☔ 建议：记得带伞！")

weather_reminder('北京')
```

### 用例3: 多功能智能助手

结合多个技能创建全能助手：

```python
from langchain.agents import initialize_agent
from langchain.llms import OpenAI

# 导入所有工具
tools = [
    DailyNewsTool(),
    WeatherTool(), 
    TranslateTool(),
    HotTopicsTool(),
    # ... 更多
]

# 创建智能助手
assistant = initialize_agent(
    tools, 
    OpenAI(temperature=0),
    agent="zero-shot-react-description"
)

# 多轮对话
while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit', '退出']:
        break
    
    response = assistant.run(user_input)
    print(f"Assistant: {response}")
```

## 🔧 故障排除 | Troubleshooting

### 问题1: 技能无法加载

**可能原因：**
- JSON 格式错误
- 路径配置错误
- 权限问题

**解决方案：**
1. 验证 JSON 格式：`cat skills/mcp/60s-daily-news.json | jq .`
2. 检查文件路径是否正确
3. 确保有读取权限：`ls -la skills/`

### 问题2: API 调用失败

**可能原因：**
- 网络连接问题
- API 服务暂时不可用
- 参数错误

**解决方案：**
1. 测试网络：`ping 60s.viki.moe`
2. 直接测试 API：`curl https://60s.viki.moe/v2/60s`
3. 检查参数格式是否正确

### 问题3: Agent 不调用函数

**可能原因：**
- 函数描述不够清晰
- 用户问题表述不明确
- Agent 配置问题

**解决方案：**
1. 改进函数描述，使其更明确
2. 用更明确的问题重新提问
3. 检查 Agent 配置和日志

## 📖 下一步 | Next Steps

### 探索更多技能
- [热门话题技能](../skills/mcp/hot-topics.json) - 获取各平台热搜
- [实用工具技能](../skills/mcp/utility-tools.json) - 翻译、二维码等
- [娱乐内容技能](../skills/mcp/fun-content.json) - 笑话、名言等

### 深入学习
- 📚 [完整使用示例](USAGE.md)
- 📋 [所有技能索引](../docs/SKILLS_INDEX.md)
- 🔗 [60s API 文档](https://docs.60s-api.viki.moe)

### 参与贡献
- 🐛 [报告问题](https://github.com/vikiboss/60s-skills/issues)
- 💡 [提出建议](https://github.com/vikiboss/60s-skills/issues/new)
- 🤝 [贡献代码](https://github.com/vikiboss/60s-skills/pulls)

## 💬 获得帮助 | Get Help

- **GitHub Issues**: [提问和反馈](https://github.com/vikiboss/60s-skills/issues)
- **原API问题**: [60s API Issues](https://github.com/vikiboss/60s/issues)
- **文档**: [完整文档](../README.md)

---

**祝你使用愉快！Happy coding! 🎉**
