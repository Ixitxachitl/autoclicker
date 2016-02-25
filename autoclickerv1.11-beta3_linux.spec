# -*- mode: python -*-

block_cipher = None


a = Analysis(['autoclickerv1.11-beta4.py'],
             pathex=['/home/noah/autoclicker'],
             binaries=None,
             datas=None,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
a.datas += [('resources/bar.png', '/home/noah/autoclicker/resources/bar.png', 'DATA')]
a.datas += [('resources/close.png', '/home/noah/autoclicker/resources/close.png', 'DATA')]
a.datas += [('resources/closehover.png', '/home/noah/autoclicker/resources/closehover.png', 'DATA')]
a.datas += [('resources/leftclick.png', '/home/noah/autoclicker/resources/leftclick.png', 'DATA')]
a.datas += [('resources/leftclickdown.png', '/home/noah/autoclicker/resources/leftclickdown.png', 'DATA')]
a.datas += [('resources/middleclick.png', '/home/noah/autoclicker/resources/middleclick.png', 'DATA')]
a.datas += [('resources/middleclickdown.png', '/home/noah/autoclicker/resources/middleclickdown.png', 'DATA')]
a.datas += [('resources/rightclick.png', '/home/noah/autoclicker/resources/rightclick.png', 'DATA')]
a.datas += [('resources/rightclickdown.png', '/home/noah/autoclicker/resources/rightclickdown.png', 'DATA')]
a.datas += [('resources/running.png', '/home/noah/autoclicker/resources/running.png', 'DATA')]
a.datas += [('resources/stopped.png', '/home/noah/autoclicker/resources/stopped.png', 'DATA')]
a.datas += [('resources/ledoff.png', '/home/noah/autoclicker/resources/ledoff.png', 'DATA')]
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='autoclickerv1.11-beta4',
          debug=False,
          strip=False,
          upx=True,
          console=True )
