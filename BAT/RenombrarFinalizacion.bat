D:
cd D:\Maestria\TFM\Datos\INPUT\CargaDatos
echo on
for /f "skip=1" %%x in ('wmic os get localdatetime') do if not defined MyDate set MyDate=%%x
set today=%MyDate:~0,4%-%MyDate:~4,2%-%MyDate:~6,2%
set "_year=%MyDate:~0,4%"
set "_month=%MyDate:~4,2%"
set "_day=%MyDate:~6,2%"
set "_hra=%MyDate:~8,2%"
set "_min=%MyDate:~10,2%"
set cnt=0
dir /b BASE_PROCESAMIENTO.xlsx  /s 2> nul | find "" /v /c > tmp && set /p count=<tmp && del tmp 
REN  BASE_PROCESAMIENTO.xlsx  BASE_%_year%%_month%%_day%%_hra%%_min%.xlsx
