# -*- mode: python -*-

added_data = [('xau_libs\\lib.py', 'xau_libs\\lib.py'),
              ('xau_libs\\QuikPy\\QuikPy.py', 'xau_libs\\QuikPy\\QuikPy.py')]

a = Analysis(['xau.py'],
             binaries=[],
             datas=added_data,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data)
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    name='xau',
    debug=False,
    strip=False,
    upx=True,
    console=True
)
