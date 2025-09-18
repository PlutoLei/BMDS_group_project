def analyze_course_selection():
    """分析学生选课情况"""
    # 课程数据
    courses = {
        'history': {'小明', '张三', '李四', '王五', 'Lily', 'Bob'},
        'politics': {'小明', '小花', '小红', '二狗'},
        'english': {'小明', 'Lily', 'Bob', 'David', '李四'}
    }
    
    # 通过序列解包，将字典中的三个集合分别赋值给对应的变量
    history, politics, english = courses.values()
    
    # 计算各种统计数据
    all_students = history | politics | english
    total_count = len(all_students)
    
    # 只选一门课的学生
    only_history = history - politics - english
    only_politics = politics - history - english  
    only_english = english - politics - history
    only_one_course = only_history | only_politics | only_english
    
    # 选了三门课的学生
    all_three_courses = history & politics & english
    
    # 输出结果
    print(f"选课学生总共有: {total_count} 人")
    print(f"只选历史课的有 {len(only_history)} 人，他们是: {only_history}")
    print(f"只选一门课的有 {len(only_one_course)} 人，他们是: {only_one_course}")
    print(f"选了三门学科的学生有 {len(all_three_courses)} 人，他们是: {all_three_courses}")
    
    return {
        'total': total_count,
        'only_one': len(only_one_course),
        'all_three': len(all_three_courses)
    }

if __name__ == "__main__":
    stats = analyze_course_selection()

