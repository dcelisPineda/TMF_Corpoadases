D:
cd D:\Maestria\TFM\Datos\INPUT\CargaDatos
echo on
for /f "skip=1" %%x in ('wmic os get localdatetime') do if not defined MyDate set MyDate=%%x
set today=%MyDate:~0,4%-%MyDate:~4,2%-%MyDate:~6,2%
set "_year=%MyDate:~0,4%"
set "_month=%MyDate:~4,2%"
set "_day=%MyDate:~6,2%"
set cnt=0
dir /b BASE_*.xlsx /s 2> nul | find "" /v /c > tmp && set /p count=<tmp && del tmp && echo %count%
REN  BASE_*.xlsx  BASE_PROCESAMIENTO.xlsx 
