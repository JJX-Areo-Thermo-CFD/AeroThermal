print(">>>欢迎使用AreoThermal求解器，使用条件一维定常可压缩<<<")
print("请按照提示输入边界条件（按回车键确认）：\n")
rho1=float(input("请输入进口处的密度rho1(kg/m^3):"))
v1=float(input("请输入进口处的速度v1(m/s):"))
a1=float(input("请输入进口处的面积a1(m^2):"))
rho2=float(input("请输入出口处的密度rho2(kg/m^3):"))
a2=float(input("请输入出口处的面积a2(m^2):"))
m_dot=rho1*v1*a1
v2=m_dot/(rho2*a2)
print("/n"+"=*40")
print("areothermal计算结果")
print("="*40)
print(f"[结果]系统质量流量{m_dot:.4f}kg/s")
print(f"[结果]预计出口流速{v2:.2f}m/s")


