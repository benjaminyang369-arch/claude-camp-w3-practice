# claude-camp-w3-practice

> 数据处理 + 文件 I/O + Git 进阶 —— Phase 0 收官周

本仓库包含 3 个数据处理小项目。项目 2、3 采用 feature branch 工作流开发（独立分支完成后合并回 main）；项目 1 因初次配置仓库时本地与远程历史不同步，直接在 main 上提交。

## 环境准备

```bash
# 激活虚拟环境
source /path/to/.venv/bin/activate

# 项目 3 需要 pytest（项目 1、2 仅用 Python 标准库）
pip install pytest
```

## 项目 1：CSV 学员数据分析器

读取学员 CSV 文件，统计总人数、各国家人数、对赌完成率，并把结果保存为 JSON 报告。
重点：处理脏数据（空邮箱、国家名大小写不统一），做了数据清洗。

运行：
```bash
python3 csv_analyzer.py
```
输出：终端打印统计结果 + 生成 `report.json`

## 项目 2：JSON 配置文件读写器

读取 `config.json`，命令行让用户修改任意设置后写回文件。
重点：加了数据验证——字体大小必须是 8-32 之间的整数，非法输入会被拒绝并要求重输。

运行：
```bash
python3 config_editor.py
```

## 项目 3：带单元测试的字符串工具库

`string_utils.py` 包含 3 个函数：
- `reverse_words(s)` —— 反转单词顺序
- `count_vowels(s)` —— 统计元音字母数量
- `is_palindrome(s)` —— 判断是否回文

`test_string_utils.py` 用 pytest 测试以上 3 个函数，每个函数 3 个用例（正常 / 边界 / 异常），共 9 个测试。

运行测试：
```bash
pytest
```
结果：9 passed ✅

## 本周收获

第一次按"专业开发流程"做事：函数 + 测试 + 文档完整闭环，Git 分支工作流，处理真实脏数据的防御性编程。