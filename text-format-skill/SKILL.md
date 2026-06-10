---
name: text-format-skill
description: 通过删除多余空格、修正大小写和纠正标点符号来格式化和清理文本内容
---

# 文本格式化器

当被要求格式化文本时,执行python脚本 `./scripts/format_text.py`，并返回格式化后的文本内容。

## 示例

**输入**: "hello   world"
**调用脚本**: `python3 ./scripts/format_text.py "hello   world"`**
**输出**: "Hello world."

**输入**: "this is  a    test"
**调用脚本**: `python3 ./scripts/format_text.py "this is  a    test"`**
**输出**: "This is a test."

## 指南
- 不要自己格式化文本，请调用脚本