# scripts/process.py
def format_text(text):
    print(f"原始文本: '{text}'")
    # 删除多余空格
    text = ' '.join(text.split())

    # 首字母大写
    text = text.capitalize()

    # 添加句号（如果缺失）
    if not text.endswith(('.', '!', '?')):
        text += '.'
    print(f"格式化后的文本: '{text}'")

    return text

if __name__ == '__main__':
    # 获取输入的参数文本
    import sys

    if len(sys.argv) > 1:
        text = ' '.join(sys.argv[1:])
    else:
        raise ValueError("请提供文本参数")

    formatted_text = format_text(text)
    print(f"格式化后的文本: '{formatted_text}'")