a = Analysis([os.path.join(HOMEPATH,'support\\_mountzlib.py'), os.path.join(HOMEPATH,'support\\useUnicode.py'), 'I:\\Programming\\kiki\\kiki.py'],
             pathex=['I:\\Programming\\kiki'])
pyz = PYZ(a.pure)
exe = EXE( pyz,
          a.scripts,
          a.binaries,
          name='kiki.exe',
          debug=0,
          strip=0,
          upx=1,
          console=0 , icon='I:\\Programming\\kiki\\kiki.ico')
