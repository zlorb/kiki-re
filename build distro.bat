@ECHO OFF

del kiki.zip
del kiki.tar
del kiki.tar.gz

ECHO Removing distroXX directory and contents...
del distroXX\*.* /q
del distroXX\docs\*.* /q
rd distroXX\docs /q
rd distroXX /q

ECHO Making distroXX directory and copying python files...
md distroXX
copy kiki.py distroXX\
copy __init__.py distroXX\
copy kiki.wxg distroXX\
copy readme.txt distroXX\
copy history.txt distroXX\

ECHO Making docs dir and copying docs...
md distroXX\docs
copy docs\*.* distroXX\docs\*.*

ECHO Copying auxiliary files...
copy Kiki.bat distroXX\
copy *.spec distroXX\

@ECHO Copying resources...

@ECHO Making docs dir and copying docs...

@ECHO Making library dir and copying library...

@ECHO Updating version...
build_kiki.py

@ECHO Copying resources and docs which might otherwise 
@ECHO have been corrupted by update process...
copy kiki.ico distroXX\

@ECHO Building distro...
cd distroXX
c:\Archivers\7-Zip\7z.exe a -tzip ..\kiki.zip * -r
REM c:\Archivers\7-Zip\7z.exe a -ttar ..\kiki.tar * -r
cd..
REM c:\Archivers\7-Zip\7z.exe a -tgzip kiki.tar.gz kiki.tar -r
REM del kiki.tar

ECHO Cleaning own dir...
del *.pyo /q
del *.pyc /q