@echo off
SET JLINK_PATH=C:\Path\To\JLink.exe
SET JLINK_SCRIPT=C:\Path\To\UnlockScript.jlink

:START
echo Unlocking Kinetic...
echo unlock Kinetic > %JLINK_SCRIPT%
echo q >> %JLINK_SCRIPT%
%JLINK_PATH% -CommanderScript %JLINK_SCRIPT%

echo Halting device...
echo h > %JLINK_SCRIPT%
echo q >> %JLINK_SCRIPT%
%JLINK_PATH% -CommanderScript %JLINK_SCRIPT%

echo Checking if the device is halted...
echo IsHalted > %JLINK_SCRIPT%
echo q >> %JLINK_SCRIPT%
%JLINK_PATH% -CommanderScript %JLINK_SCRIPT% > halt_status.txt

findstr /C:"halted" halt_status.txt > nul
if %errorlevel%==1 (
    echo Device is not halted, retrying...
    goto START
) else (
    echo Device is successfully halted.
)

echo Process completed!


REM Trong script này:

REM %JLINK_PATH% được sử dụng để chỉ đường dẫn tới JLink Commander.
REM %JLINK_SCRIPT% là đường dẫn tới tệp script chứa các lệnh JLink cần thiết để unlock Kinetic.
REM Lệnh goto START được sử dụng để lặp lại quy trình nếu kết nối không thành công.

REM Vui lòng thay thế C:\Path\To\JLink.exe và C:\Path\To\JLinkCommands.jlink bằng đường dẫn chính xác tới JLink Commander và tệp script lệnh JLink của bạn. Cũng cần lưu ý rằng, tùy thuộc vào các lệnh cụ thể trong JLink và cách thiết bị phản hồi, bạn có thể cần chỉnh sửa phần lệnh kiểm tra kết nối để phù hợp với thiết lập cụ thể của bạn.