# scripts/process.py
def format_text(text):
    """格式化文本  
    1. 删除多余空格（将多个空格替换为单个空格）
    2. 修正大小写（句子首字母大写）
    3. 纠正标点符号（确保正确的结束标点）
    4. 返回清理后的文本
    """
    
    print('原始文本：', text)
    # 删除多余空格
    text = ' '.join(text.split())
    # 首字母大写
    text = text.capitalize()
    # 添加句号（如果缺失）
    if not text.endswith(('.', '!', '?')):
        text += '.'
    print('处理后的文本：', text)
    return text

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print('Usage: python3 format_text.py <input_text>')
        sys.exit(1)

    input_text = sys.argv[1]
    formatted_text = format_text(input_text)
    print(formatted_text)