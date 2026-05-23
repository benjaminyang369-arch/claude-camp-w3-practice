from string_utils import reverse_words, count_vowels, is_palindrome


# ---------- 测试 reverse_words ----------
def test_reverse_words_normal():
    # 正常情况
    assert reverse_words("hello world") == "world hello"

def test_reverse_words_single():
    # 边界情况：只有一个单词，反转后还是它自己
    assert reverse_words("hello") == "hello"

def test_reverse_words_empty():
    # 异常情况：空字符串
    assert reverse_words("") == ""


# ---------- 测试 count_vowels ----------
def test_count_vowels_normal():
    # 正常情况
    assert count_vowels("hello") == 2

def test_count_vowels_uppercase():
    # 边界情况：大写也要数到
    assert count_vowels("AEIOU") == 5

def test_count_vowels_none():
    # 异常情况：没有元音
    assert count_vowels("xyz") == 0


# ---------- 测试 is_palindrome ----------
def test_is_palindrome_true():
    # 正常情况：是回文
    assert is_palindrome("level") == True

def test_is_palindrome_false():
    # 正常情况：不是回文
    assert is_palindrome("hello") == False

def test_is_palindrome_with_space():
    # 边界情况：忽略空格和大小写
    assert is_palindrome("Race car") == True