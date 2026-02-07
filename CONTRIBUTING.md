# Contributing to 60s Skills - 贡献指南

感谢你对 60s Skills 项目的关注！我们欢迎任何形式的贡献。

Thank you for your interest in contributing to 60s Skills! We welcome all forms of contributions.

## 🤝 如何贡献 | How to Contribute

### 报告问题 | Report Issues

如果你发现了 bug 或有功能建议：

1. 在 [Issues](https://github.com/vikiboss/60s-skills/issues) 页面搜索是否已有相关问题
2. 如果没有，创建一个新 Issue
3. 清晰描述问题或建议
4. 如果是 bug，请提供复现步骤

### 贡献代码 | Contribute Code

#### 开发流程

1. **Fork 仓库**
   ```bash
   # 点击 GitHub 页面右上角的 Fork 按钮
   ```

2. **克隆到本地**
   ```bash
   git clone https://github.com/YOUR_USERNAME/60s-skills.git
   cd 60s-skills
   ```

3. **创建分支**
   ```bash
   git checkout -b feature/your-feature-name
   # 或
   git checkout -b fix/your-bug-fix
   ```

4. **进行更改**
   - 遵循现有代码风格
   - 确保 JSON 格式正确
   - 更新相关文档

5. **测试更改**
   ```bash
   # 验证 JSON 格式
   cat skills/mcp/your-skill.json | jq .
   
   # 测试 API 调用
   curl "https://60s.viki.moe/v2/your-endpoint"
   ```

6. **提交更改**
   ```bash
   git add .
   git commit -m "feat: add your feature description"
   # 或
   git commit -m "fix: fix your bug description"
   ```

7. **推送到 GitHub**
   ```bash
   git push origin feature/your-feature-name
   ```

8. **创建 Pull Request**
   - 访问你 fork 的仓库页面
   - 点击 "New Pull Request"
   - 填写 PR 描述，说明你的更改
   - 等待审核

## 📝 贡献类型 | Types of Contributions

### 1. 添加新技能 | Add New Skills

如果 60s API 新增了接口，你可以为其创建技能定义：

**需要包含：**
- MCP 格式定义 (`skills/mcp/your-skill.json`)
- OpenAI 格式定义 (`skills/openai/your-skill.json`)（可选）
- 更新 `skills/index.json`
- 更新 `docs/SKILLS_INDEX.md`
- 添加使用示例到 `examples/USAGE.md`

**示例：**
```json
{
  "name": "your-skill-name",
  "version": "1.0.0",
  "description": "Clear description of what this skill does",
  "protocol": "mcp",
  "tools": [
    {
      "name": "function_name",
      "description": "What this function does",
      "inputSchema": {
        "type": "object",
        "properties": {
          "param_name": {
            "type": "string",
            "description": "Parameter description"
          }
        },
        "required": ["param_name"]
      },
      "endpoint": {
        "url": "https://60s.viki.moe/v2/endpoint",
        "method": "GET"
      }
    }
  ],
  "metadata": {
    "author": "vikiboss",
    "license": "MIT"
  }
}
```

### 2. 改进现有技能 | Improve Existing Skills

- 优化函数描述，使其更清晰
- 添加更多参数选项
- 改进错误处理
- 添加更多示例

### 3. 改进文档 | Improve Documentation

- 修正错别字
- 改进说明和示例
- 添加更多使用场景
- 翻译文档（中英双语）

### 4. 添加示例 | Add Examples

在 `examples/` 目录添加更多实际应用示例：
- 不同编程语言的实现
- 不同平台的配置示例
- 实际应用场景的完整代码

## 📋 编码规范 | Coding Standards

### JSON 格式

- 使用 2 个空格缩进
- 所有字符串使用双引号
- 确保 JSON 格式有效（可用 `jq` 验证）

```bash
# 格式化 JSON
cat skills/mcp/your-skill.json | jq . > temp.json
mv temp.json skills/mcp/your-skill.json
```

### 命名约定

- **文件名**: 使用 kebab-case（如 `daily-news.json`）
- **技能名**: 使用 kebab-case（如 `60s-daily-news`）
- **函数名**: 使用 snake_case（如 `get_daily_news`）

### 描述规范

- **中文在前，英文在后** 或 **英文在前，中文在后**（保持一致）
- 描述要清晰、准确、简洁
- 包含参数的具体说明和示例

### 文档规范

- 使用 Markdown 格式
- 中英双语（English + 中文）
- 代码示例要完整可运行
- 包含实际的输出示例

## ✅ Pull Request 检查清单 | PR Checklist

提交 PR 前，请确认：

- [ ] 代码遵循项目的编码规范
- [ ] JSON 格式正确（通过 `jq` 验证）
- [ ] 添加或更新了相关文档
- [ ] 更新了 `skills/index.json`
- [ ] 如果添加新技能，更新了 `docs/SKILLS_INDEX.md`
- [ ] 提供了使用示例
- [ ] Commit 信息清晰明确
- [ ] PR 描述详细说明了更改内容

## 🔍 代码审查 | Code Review

所有 PR 都需要经过审查。审查者会检查：

1. **功能正确性**: 技能定义是否正确反映了 API 功能
2. **代码质量**: JSON 格式、命名规范等
3. **文档完整性**: 是否有足够的文档和示例
4. **一致性**: 与现有技能的风格是否一致

## 💡 开发建议 | Development Tips

### 测试技能定义

```bash
# 1. 验证 JSON 格式
cat skills/mcp/your-skill.json | jq .

# 2. 测试 API 端点
curl "https://60s.viki.moe/v2/your-endpoint"

# 3. 查看 API 文档
# 访问 https://docs.60s-api.viki.moe
```

### 使用工具

推荐使用以下工具：

- **jq**: JSON 处理和验证
- **curl**: API 测试
- **VS Code**: 编辑器（带 JSON 语法检查）
- **Postman**: API 测试（可选）

### 参考现有技能

最好的学习方式是查看现有技能定义：
- 查看 `skills/mcp/60s-daily-news.json` 作为模板
- 参考 `skills/mcp/utility-tools.json` 了解复杂技能
- 学习 `examples/USAGE.md` 中的示例

## 📞 联系方式 | Contact

有问题或需要帮助？

- **GitHub Issues**: [提问](https://github.com/vikiboss/60s-skills/issues)
- **原项目**: [60s API](https://github.com/vikiboss/60s)

## 📄 许可证 | License

贡献的代码将采用与项目相同的 MIT 许可证。

通过贡献，你同意你的贡献将在 MIT 许可证下发布。

---

**感谢你的贡献！🎉 Thank you for contributing!**
