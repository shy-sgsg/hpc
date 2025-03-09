import matplotlib.pyplot as plt
import numpy as np

# 编译选项
compile_options = ['-O0', '-O1', '-O2', '-O3']

# 运行时间数据
vecadd_times = [10705, 8552, 9641, 9404]
matrix_multiply_times = [4146469, 3024733, 3021091, 3030870]
overall_times = [7.480, 3.833, 3.874, 3.871]

# 设置图片清晰度
plt.rcParams['figure.dpi'] = 300

# 设置全局字体，这里更换为 SimHei 字体
# plt.rcParams['font.family'] = 'SimHei'

# 定义颜色
bar_colors = ['#66b3ff', '#99ff99', '#ff6666']
line_colors = ['#0077b6', '#009688', '#d62828']

# 函数用于绘制柱状图和折线图并添加数据标签
def plot_bar_and_line_chart(data, title, ylabel, bar_color, line_color):
    x = np.arange(len(compile_options))
    width = 0.35
    plt.figure(figsize=(8, 6))
    # 绘制柱状图
    bars = plt.bar(x, data, width, color=bar_color)
    # 绘制折线图
    plt.plot(x, data, color=line_color, marker='o')
    plt.xticks(x, compile_options)
    plt.ylabel(ylabel, fontsize=12)
    plt.title(title, fontsize=14, fontweight='bold')
    # 添加数据标签
    for bar in bars:
        height = bar.get_height()
        plt.annotate(f'{height}',
                     xy=(bar.get_x() + bar.get_width() / 2, height),
                     xytext=(0, 3),  # 3 points vertical offset
                     textcoords="offset points",
                     ha='center', va='bottom', fontsize=10)
    # 去除上边框和右边框
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    # plt.tight_layout()
    plt.subplots_adjust(left=0.2, right=0.8, bottom=0.2, top=0.8)
    plt.show()

# 绘制 Vecadd 运行时间图
plot_bar_and_line_chart(vecadd_times, 'Vecadd Running Time', 'Vecadd Running Time (us)', bar_colors[0], line_colors[0])

# 绘制 Matrix Multiply 运行时间图
plot_bar_and_line_chart(matrix_multiply_times, 'Matrix Multiply Running Time', 'Matrix Multiply Running Time (us)', bar_colors[1], line_colors[1])

# 绘制整体运行时间图
plot_bar_and_line_chart(overall_times, 'Overall Running Time', 'Overall Running Time (s)', bar_colors[2], line_colors[2])
