---
name: text-format-skill
description: 当被要求格式化文本时执行
---

# 文本格式化器
通过删除多余空格、修正大小写和纠正标点符号来格式化文本内容

## 可用脚本
1. `scripts/process.py`


## 示例
### windows平台
**输入**: python process.py " hello  world  "
**输出**: "Hello world."

### linux平台、macOS平台
**输入**: python3 process.py "this is  a    test"
**输出**: "This is a test."

## 指南