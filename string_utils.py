def reverse_words(s):
    """反转单词顺序：'hello world' -> 'world hello'"""
    words = s.split()        # 拆成单词列表
    words = words[::-1]      # 倒序
    return " ".join(words)   # 拼回字符串


def count_vowels(s):
    """统计元音字母数量（不区分大小写）"""
    vowels = "aeiou"
    count = 0
    for char in s.lower():   # 转小写，大写也能数到
        if char in vowels:
            count += 1
    return count


def is_palindrome(s):
    """判断是否回文（忽略大小写和空格）"""
    cleaned = s.lower().replace(" ", "")   # 转小写 + 去空格
    return cleaned == cleaned[::-1]


# 直接运行这个文件时做个简单自测
if __name__ == "__main__":
    print(reverse_words("hello world"))   # world hello
    print(count_vowels("Python"))          # 1
    print(is_palindrome("level"))          # True