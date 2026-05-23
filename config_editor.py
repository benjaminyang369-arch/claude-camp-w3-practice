import json

# 读取配置文件
with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

# 显示当前所有设置
print("当前配置：")
for key, value in config.items():
    print(f"  {key}: {value}")

    # 让用户选择要修改的设置
key = input("\n你想修改哪个设置？(theme/language/font_size): ")

# 检查这个设置是否存在
if key not in config:
    print(f"没有 '{key}' 这个设置项。")
if key == "font_size":
        # font_size 需要特殊验证
        while True:
            raw = input(f"把 {key} 改成什么？(8-32 之间): ")
            try:
                new_value = int(raw)          # 尝试转成整数
            except ValueError:
                print("  请输入一个数字！")    # 不是数字 → 重来
                continue
            if 8 <= new_value <= 32:
                break                          # 合法 → 跳出循环
            else:
                print("  必须在 8 到 32 之间！")  # 超范围 → 重来
        config[key] = new_value
else:
        # 其他设置不需要验证
        new_value = input(f"把 {key} 改成什么？当前是 {config[key]}: ")
        config[key] = new_value

print(f"已更新：{key} = {config[key]}")

# 把更新后的配置写回文件
with open("config.json", "w", encoding="utf-8") as f:
        json.dump(config, f, ensure_ascii=False, indent=2)
print("已保存到 config.json")