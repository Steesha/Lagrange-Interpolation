# Lagrange
from sympy import *
function_group = []

if __name__ == "__main__":
    print("[Lagrange插值算法]")
    while True:
        print("----------------------")
        fx = input("请输入自变量x%d值[输入非数字退出]:" % len(function_group))
        try:
            fx = int(fx)
        except ValueError:
            break
        fy = input("请输入要映射的y%d值[输入非数字退出]:" % len(function_group))
        try:
            fy = int(fy)
        except ValueError:
            break
        eqlFlag = False
        for gp in function_group:
            if(gp['x'] == fx):
                eqlFlag = True
                break
        if eqlFlag:
            print("已经有了一组自变量为 %d 的数据，无法重复添加" % fx)
            continue
        # 无重复 开始添加
        eql = {'x': fx, 'y': fy}
        function_group.append(eql.copy())
        # 添加完毕
        print("添加完毕")
    print("输入完毕，共%d组数据" % len(function_group))
    # 开始生成

    # 定义自变量x符号
    x = symbols('x')
    allpart = 0
    for eqls in function_group:
        this_fx = eqls['x']
        parts = eqls['y']
        divNum = 1
        for eqls_1 in function_group:
            # 排除自己本身的
            if not eqls_1['x'] == this_fx:
                # 分子部分
                parts *= (x - eqls_1['x'])
                # 分母部分
                divNum *= (this_fx - eqls_1['x'])
        parts /= divNum
        # 得到多项式
        allpart += expand(parts)
    # 输出
    result_tip = ""
    for eqls in function_group:
        result_tip += "(%d,%d)" % (eqls['x'], eqls['y'])
    print("生成完毕，函数过点 %s " % result_tip)
    print("输出的函数: f(x) = %s" % allpart)
    print("LaTex语法: %s" % latex(allpart))
