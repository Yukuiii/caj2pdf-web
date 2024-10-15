## 使用方法

1. 安装依赖
```
pip install -r requirements.txt
```

2. 运行
```
python app.py
```

3. 访问
```
http://127.0.0.1:5000/api/convert
```

## 说明
基于caj2pdf的CAJ文件转换为PDF文件，更改了源代码中的使用mutool进行修复xref，改变为使用PyMuPDF库进行修复而无需额外安装mutool
