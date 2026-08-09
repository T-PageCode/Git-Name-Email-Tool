# --- © 2026 T-PageCode, Dev. ---
# Your Nocan Delete LICENSE
import os
print("Git Name Email工具 v1.0.0")
print("我们不收集任何数据,纯个人自制程序")
print("警告:输入错误可能会导致Git提交失败!如果输错了,请重新运行此程序并输入正确的信息!")
print("-------------------------------------------------------------------------------")
print("请输入您的用户名")
name = input(">>>")
print(f"成功:用户名是{name}")
print("请输入您的邮箱")
email = input(">>>")
if "@" not in email:
    print("警告:邮箱格式看起来不太对(缺少 @)，请确认是否输入正确!")
else:
    print(f"成功:用户名是{email}")
print("请输入您要配置的路径")
path = input(">>>")
if not os.path.exists(path):
    print(f"警告:找不到路径“{path}”!请检查路径是否正确!")
else:
    print(f"成功:路径是{path}")
print("是否继续?(yes=继续,no=取消)")
warning = input(">>>")
if warning == "yes":
    print("正在切换路径...")
    os.chdir(path.strip('"'))
    print(f"成功:已切换路径({path})")
    print("正在配置用户名...")
    os.system(f'git config user.name "{name}"')
    print(f"成功:已配置用户名({name})")
    print("正在配置邮箱...")
    os.system(f'git config user.email "{email}"')
    print(f"成功:已配置邮箱({email})")
    print("程序执行完毕,可关闭窗口")
elif warning == "no":
    print("已取消,正在退出...")
    exit("退出成功!")
else:
    print(f"未找到命令“{warning}”")