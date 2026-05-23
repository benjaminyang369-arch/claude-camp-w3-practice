import json
import csv

# 读取 CSV，把每一行变成一个字典
students = []
with open("students.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        students.append(row)

# 总人数
print("总人数：", len(students))

# 各国家人数
country_count = {}
for student in students:
    country = student["country"].capitalize()
    if country in country_count:
        country_count[country] += 1
    else:
        country_count[country] = 1

print("各国家人数：", country_count)

# 对赌完成率
completed_count = 0
for student in students:
    if student["bet_status"] == "completed":
        completed_count += 1

completion_rate = completed_count / len(students)
print("对赌完成人数：", completed_count)
print("对赌完成率：", round(completion_rate * 100, 1), "%")

# 把统计结果整理成一个字典
report = {
    "total_students": len(students),
    "country_count": country_count,
    "completed_count": completed_count,
    "completion_rate": round(completion_rate * 100, 1)
}

# 写进 report.json
with open("report.json", "w", encoding="utf-8") as f:
    json.dump(report, f, ensure_ascii=False, indent=2)

print("报告已保存到 report.json")