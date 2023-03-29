"""pandas_csv丢失部分行的问题
"""

import pandas as pd
from io import StringIO


# csv出现 quoting 异常的数据

csv_content = """aaa  bbb
111,222
333,444
555,666
"777"",888
999,asdf"
"""
# quoting 0 会导致行缺失
df = pd.read_csv(StringIO(csv_content), engine="python", quoting=0)

# quoting 3 显示正常
df = pd.read_csv(StringIO(csv_content), engine="python", quoting=3)
