# -*- mode: python -*-

added_data = [('lib_dir_1\\lib_1.lib', 'lib_dir_1\\lib_1.lib'),
              ('lib_dir_2\\lib_2.lib', 'lib_dir_2\\lib_2.lib')]

a = Analysis(['submodule_public.py'],
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
    name='lib',
    debug=False,
    strip=False,
    upx=True,
    console=True,
    version='..\\ms_version_1.txt', # Specify version info file for metadata
)
