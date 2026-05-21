"""


D:\CursorProject\.venv\Scripts\python.exe D:\CursorProject\Python\获取产品信息.py
正在启动自动化浏览器...
正在访问目标网页:
https://device.panasonic.cn/ac/c/dl_center/cad/index.jsp?c=search
正在自动执行分类筛选...
  第 1 级: 已选择 [传感器]
  第 2 级: 已选择 [接近传感器]
  第 3 级: 已选择 [圆柱型接近传感器 GX-200]
正在点击检索按钮...
等待检索结果加载...
列表加载完毕，开始解析底层 HTML...

========================================================
提取完成！底层共解析到 20 个独立产品。
========================================================
【所有产品数据完整清单】如下：
  [1] 网页显示: CN-23A-CC2      | name: cn-23a-cc2      | f_cd: 4238499
  [2] 网页显示: CN-23AL-CC2     | name: cn-23al-cc2     | f_cd: 4238507
  [3] 网页显示: CN-24-CC2       | name: cn-24-cc2       | f_cd: 4238515
  [4] 网页显示: CN-24L-CC2      | name: cn-24l-cc2      | f_cd: 4238523
  [5] 网页显示: GX-204SK□       | name: gx-204sk        | f_cd: 4238475
  [6] 网页显示: GX-205MK□       | name: gx-205mk        | f_cd: 4238491
  [7] 网页显示: GX-205SK□       | name: gx-205sk        | f_cd: 4238483
  [8] 网页显示: GX-208MK□       | name: gx-208mk        | f_cd: 4238335
  [9] 网页显示: GX-208MK□-Z     | name: gx-208mk-z      | f_cd: 4238411
  [10] 网页显示: GX-208MLK□      | name: gx-208mlk       | f_cd: 4238343
  [11] 网页显示: GX-208MLK□-Z    | name: gx-208mlk-z     | f_cd: 4238419
  [12] 网页显示: GX-212MK□       | name: gx-212mk        | f_cd: 4238351
  [13] 网页显示: GX-212MK□-Z     | name: gx-212mk-z      | f_cd: 4238427
  [14] 网页显示: GX-212MLK□      | name: gx-212mlk       | f_cd: 4238359
  [15] 网页显示: GX-212MLK□-Z    | name: gx-212mlk-z     | f_cd: 4238435
  [16] 网页显示: GX-218MK□       | name: gx-218mk        | f_cd: 4238367
  [17] 网页显示: GX-218MK□-Z     | name: gx-218mk-z      | f_cd: 4238443
  [18] 网页显示: GX-218MLK□      | name: gx-218mlk       | f_cd: 4238375
  [19] 网页显示: GX-218MLK□-Z    | name: gx-218mlk-z     | f_cd: 4238451
  [20] 网页显示: GX-230MK□       | name: gx-230mk        | f_cd: 4238383

========================================================
正在根据 MAX_EXPORT_COUNT = 5 截取数据...
请直接复制以下代码，替换到下载程序的 product_list 变量中：

product_list = [
    {"name": "cn-23a-cc2", "f_cd": "4238499"},  # CN-23A-CC2 (原始 HTML: <a href="/ac/c_download/fasys/sensor/proximity/cad/2d_dxf/cn-23a-cc2.dxf?f_cd=4238499" target="mewdownload"><img src="/ac/c/dl_center/images/cad/dl_button_2d_dxf.png" alt="2D-DXF" width="70" height="20"></a>)
    {"name": "cn-23al-cc2", "f_cd": "4238507"},  # CN-23AL-CC2 (原始 HTML: <a href="/ac/c_download/fasys/sensor/proximity/cad/2d_dxf/cn-23al-cc2.dxf?f_cd=4238507" target="mewdownload"><img src="/ac/c/dl_center/images/cad/dl_button_2d_dxf.png" alt="2D-DXF" width="70" height="20"></a>)
    {"name": "cn-24-cc2", "f_cd": "4238515"},  # CN-24-CC2 (原始 HTML: <a href="/ac/c_download/fasys/sensor/proximity/cad/2d_dxf/cn-24-cc2.dxf?f_cd=4238515" target="mewdownload"><img src="/ac/c/dl_center/images/cad/dl_button_2d_dxf.png" alt="2D-DXF" width="70" height="20"></a>)
    {"name": "cn-24l-cc2", "f_cd": "4238523"},  # CN-24L-CC2 (原始 HTML: <a href="/ac/c_download/fasys/sensor/proximity/cad/2d_dxf/cn-24l-cc2.dxf?f_cd=4238523" target="mewdownload"><img src="/ac/c/dl_center/images/cad/dl_button_2d_dxf.png" alt="2D-DXF" width="70" height="20"></a>)
    {"name": "gx-204sk", "f_cd": "4238475"},  # GX-204SK□ (原始 HTML: <a href="/ac/c_download/fasys/sensor/proximity/cad/2d_dxf/gx-204sk.dxf?f_cd=4238475" target="mewdownload"><img src="/ac/c/dl_center/images/cad/dl_button_2d_dxf.png" alt="2D-DXF" width="70" height="20"></a>)
]

进程已结束，退出代码为 0




"""