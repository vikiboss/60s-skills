# Usage Examples - 使用示例

本文档提供在不同 AI Agent 平台上使用 60s Skills 的详细示例。

## 📋 目录

- [MCP (Model Context Protocol)](#mcp-model-context-protocol)
- [OpenAI Function Calling](#openai-function-calling)
- [LangChain](#langchain)
- [直接 API 调用](#direct-api-calls)

---

## MCP (Model Context Protocol)

### Claude Desktop 配置

1. 打开 Claude Desktop 配置文件：
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`

2. 添加技能配置：

```json
{
  "mcpServers": {
    "60s-daily-news": {
      "command": "node",
      "args": ["/path/to/mcp-server.js"],
      "env": {
        "SKILL_CONFIG": "/path/to/skills/mcp/60s-daily-news.json"
      }
    },
    "weather": {
      "command": "node",
      "args": ["/path/to/mcp-server.js"],
      "env": {
        "SKILL_CONFIG": "/path/to/skills/mcp/weather.json"
      }
    }
  }
}
```

3. 重启 Claude Desktop

### 使用示例

```
User: 今天有什么新闻？

Claude: [自动调用 60s-daily-news skill]
让我为您获取今天的新闻...

返回15条今日新闻：
1. 新闻标题1...
2. 新闻标题2...
...
```

---

## OpenAI Function Calling

### Python 示例

```python
import openai
import json
import requests

# 加载技能定义
with open('skills/openai/60s-daily-news.json', 'r', encoding='utf-8') as f:
    skill_spec = json.load(f)

# 提取函数定义
functions = []
for path, methods in skill_spec['paths'].items():
    for method, details in methods.items():
        functions.append({
            "name": details['operationId'],
            "description": details['description'],
            "parameters": {
                "type": "object",
                "properties": {
                    param['name']: {
                        "type": param['schema']['type'],
                        "description": param.get('description', ''),
                        "enum": param['schema'].get('enum')
                    }
                    for param in details.get('parameters', [])
                }
            }
        })

# 调用 OpenAI API
response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "user", "content": "获取今天的新闻"}
    ],
    functions=functions,
    function_call="auto"
)

# 如果模型决定调用函数
message = response["choices"][0]["message"]
if message.get("function_call"):
    function_name = message["function_call"]["name"]
    function_args = json.loads(message["function_call"]["arguments"])
    
    # 调用实际的API
    if function_name == "getDailyNews":
        api_url = "https://60s.viki.moe/v2/60s"
        params = function_args
        result = requests.get(api_url, params=params).json()
        
        # 将结果返回给模型
        second_response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": "获取今天的新闻"},
                message,
                {
                    "role": "function",
                    "name": function_name,
                    "content": json.dumps(result)
                }
            ]
        )
        
        print(second_response["choices"][0]["message"]["content"])
```

### Node.js 示例

```javascript
const OpenAI = require('openai');
const fs = require('fs');
const axios = require('axios');

const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY
});

// 加载技能定义
const skillSpec = JSON.parse(
  fs.readFileSync('skills/openai/60s-daily-news.json', 'utf-8')
);

// 转换为 OpenAI 函数格式
const functions = Object.entries(skillSpec.paths).flatMap(([path, methods]) => {
  return Object.entries(methods).map(([method, details]) => ({
    name: details.operationId,
    description: details.description,
    parameters: {
      type: 'object',
      properties: Object.fromEntries(
        (details.parameters || []).map(param => [
          param.name,
          {
            type: param.schema.type,
            description: param.description,
            ...(param.schema.enum && { enum: param.schema.enum })
          }
        ])
      )
    }
  }));
});

async function chat(userMessage) {
  const messages = [{ role: 'user', content: userMessage }];
  
  const response = await openai.chat.completions.create({
    model: 'gpt-4',
    messages: messages,
    functions: functions,
    function_call: 'auto'
  });
  
  const responseMessage = response.choices[0].message;
  
  if (responseMessage.function_call) {
    const functionName = responseMessage.function_call.name;
    const functionArgs = JSON.parse(responseMessage.function_call.arguments);
    
    // 调用实际的API
    let functionResult;
    if (functionName === 'getDailyNews') {
      const apiResponse = await axios.get('https://60s.viki.moe/v2/60s', {
        params: functionArgs
      });
      functionResult = apiResponse.data;
    }
    
    // 将结果返回给模型
    messages.push(responseMessage);
    messages.push({
      role: 'function',
      name: functionName,
      content: JSON.stringify(functionResult)
    });
    
    const secondResponse = await openai.chat.completions.create({
      model: 'gpt-4',
      messages: messages
    });
    
    return secondResponse.choices[0].message.content;
  }
  
  return responseMessage.content;
}

// 使用
chat('获取今天的新闻').then(console.log);
```

---

## LangChain

### Python LangChain 示例

```python
from langchain.tools import Tool
from langchain.agents import initialize_agent, AgentType
from langchain.llms import OpenAI
import requests

# 定义工具函数
def get_daily_news(date=None, encoding='json'):
    """获取每日新闻"""
    params = {}
    if date:
        params['date'] = date
    if encoding:
        params['encoding'] = encoding
    
    response = requests.get('https://60s.viki.moe/v2/60s', params=params)
    return response.json()

def get_weather(location):
    """获取天气信息"""
    response = requests.get(
        'https://60s.viki.moe/v2/weather/realtime',
        params={'location': location}
    )
    return response.json()

def translate_text(text, from_lang='auto', to_lang='en'):
    """翻译文本"""
    response = requests.post(
        'https://60s.viki.moe/v2/fanyi',
        json={'text': text, 'from': from_lang, 'to': to_lang}
    )
    return response.json()

# 创建 LangChain 工具
tools = [
    Tool(
        name="GetDailyNews",
        func=get_daily_news,
        description="获取每日新闻。可以指定日期(YYYY-MM-DD格式)和输出格式(json/text/markdown)。"
    ),
    Tool(
        name="GetWeather",
        func=get_weather,
        description="获取指定地点的实时天气信息。需要提供中文地点名称，如'北京'、'上海'。"
    ),
    Tool(
        name="TranslateText",
        func=translate_text,
        description="翻译文本。需要提供要翻译的文本，可选源语言和目标语言代码。"
    )
]

# 初始化 Agent
llm = OpenAI(temperature=0)
agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# 使用示例
result = agent.run("获取今天的新闻，并告诉我北京的天气")
print(result)
```

### TypeScript LangChain 示例

```typescript
import { Tool } from 'langchain/tools';
import { initializeAgentExecutorWithOptions } from 'langchain/agents';
import { OpenAI } from 'langchain/llms/openai';
import axios from 'axios';

// 创建自定义工具
class DailyNewsTool extends Tool {
  name = 'get_daily_news';
  description = '获取每日新闻。可以指定日期(YYYY-MM-DD格式)。';

  async _call(input: string): Promise<string> {
    const params: any = {};
    try {
      const parsed = JSON.parse(input);
      if (parsed.date) params.date = parsed.date;
    } catch {
      // 如果不是JSON，直接使用
    }
    
    const response = await axios.get('https://60s.viki.moe/v2/60s', { params });
    return JSON.stringify(response.data);
  }
}

class WeatherTool extends Tool {
  name = 'get_weather';
  description = '获取指定地点的天气信息。需要提供地点名称。';

  async _call(location: string): Promise<string> {
    const response = await axios.get('https://60s.viki.moe/v2/weather/realtime', {
      params: { location }
    });
    return JSON.stringify(response.data);
  }
}

// 使用工具
async function main() {
  const tools = [new DailyNewsTool(), new WeatherTool()];
  const llm = new OpenAI({ temperature: 0 });
  
  const executor = await initializeAgentExecutorWithOptions(tools, llm, {
    agentType: 'zero-shot-react-description',
    verbose: true,
  });
  
  const result = await executor.call({
    input: '获取今天的新闻，并查询上海的天气'
  });
  
  console.log(result.output);
}

main();
```

---

## Direct API Calls

### 直接使用 cURL

```bash
# 获取今日新闻（JSON格式）
curl "https://60s.viki.moe/v2/60s"

# 获取今日新闻（纯文本格式）
curl "https://60s.viki.moe/v2/60s?encoding=text"

# 获取特定日期的新闻
curl "https://60s.viki.moe/v2/60s?date=2024-01-15"

# 查询天气
curl "https://60s.viki.moe/v2/weather/realtime?location=北京"

# 翻译文本
curl -X POST "https://60s.viki.moe/v2/fanyi" \
  -H "Content-Type: application/json" \
  -d '{"text": "Hello World", "from": "en", "to": "zh"}'

# 生成二维码
curl "https://60s.viki.moe/v2/qrcode?text=https://github.com" \
  --output qrcode.png

# 获取IP信息
curl "https://60s.viki.moe/v2/ip"

# 查询汇率
curl "https://60s.viki.moe/v2/exchange-rate?from=USD&to=CNY"
```

### Python Requests

```python
import requests

# 获取新闻
response = requests.get('https://60s.viki.moe/v2/60s')
news = response.json()
print(f"今日新闻 ({news['date']}):")
for i, item in enumerate(news['news'], 1):
    print(f"{i}. {item['title']}")

# 查询天气
weather = requests.get(
    'https://60s.viki.moe/v2/weather/realtime',
    params={'location': '北京'}
).json()
print(f"北京天气: {weather}")

# 翻译
translation = requests.post(
    'https://60s.viki.moe/v2/fanyi',
    json={'text': 'Hello World', 'from': 'en', 'to': 'zh'}
).json()
print(f"翻译结果: {translation}")
```

### JavaScript Fetch

```javascript
// 获取新闻
fetch('https://60s.viki.moe/v2/60s')
  .then(res => res.json())
  .then(data => {
    console.log(`今日新闻 (${data.date}):`);
    data.news.forEach((item, i) => {
      console.log(`${i + 1}. ${item.title}`);
    });
  });

// 查询天气
fetch('https://60s.viki.moe/v2/weather/realtime?location=北京')
  .then(res => res.json())
  .then(data => console.log('北京天气:', data));

// 翻译
fetch('https://60s.viki.moe/v2/fanyi', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ text: 'Hello World', from: 'en', to: 'zh' })
})
  .then(res => res.json())
  .then(data => console.log('翻译结果:', data));
```

---

## 🎯 实际应用场景

### 场景1: 智能新闻播报机器人

```python
def news_briefing_bot():
    """每日新闻简报机器人"""
    # 获取新闻
    news = get_daily_news()
    
    # 获取天气
    weather = get_weather('北京')
    
    # 组合播报
    briefing = f"""
    早上好！这里是{news['date']}的新闻简报：
    
    【今日要闻】
    """
    for i, item in enumerate(news['news'][:5], 1):
        briefing += f"\n{i}. {item['title']}"
    
    briefing += f"\n\n【天气提示】\n北京今日天气：{weather['weather']}"
    briefing += f"\n\n【每日微语】\n{news['tip']}"
    
    return briefing
```

### 场景2: 多功能助手

```python
from langchain.agents import initialize_agent

# 集成所有技能
all_tools = [
    DailyNewsTool(),
    WeatherTool(),
    TranslateTool(),
    HotTopicsTool(),
    # ... 更多工具
]

assistant = initialize_agent(all_tools, llm, agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION)

# 用户可以自然语言交互
user_input = "帮我查一下今天的新闻和北京的天气，然后告诉我微博上现在最热的话题是什么"
response = assistant.run(user_input)
```

---

## 📚 更多资源

- [技能索引](../docs/SKILLS_INDEX.md) - 所有技能的详细说明
- [API文档](https://docs.60s-api.viki.moe) - 完整的API文档
- [源码仓库](https://github.com/vikiboss/60s) - 60s API 源码
