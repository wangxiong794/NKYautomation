import os
from get_root_path import root_dir


# 这个程序主目录
BASE_PATH = root_dir

# 存放yaml文件的路径
DATA_PATH = os.path.join(BASE_PATH, 'yamlCase')

# 测试用例的目录
CASE_PATH = os.path.join(BASE_PATH, 'test_case')

# 日志的路径
LOG_PATH = os.path.join(BASE_PATH, 'logs')

# 报告的路径
REPORT_PATH = os.path.join(BASE_PATH, 'report')

# 模板的路径
CASE_TEMPLATE = os.path.join(BASE_PATH,'case_template')


if __name__ == "__main__":
    print(BASE_PATH)