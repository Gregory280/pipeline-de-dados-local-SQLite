@echo off
setlocal

cd /d "%~dp0"

echo ================================================
echo Academia X - Pipeline de Dados
echo ================================================
echo .
echo Iniciando pipeline...
echo .


if not exist "logs" mkdir "logs"

set "LOG=logs\ultima_execucao.log"

> "%LOG%" echo Inicio: %date% %time%

python -u src\orchestrator.py >> "%LOG%" 2>&1

set "resultado=%errorlevel%"

>> "%LOG%" echo.
>> "%LOG%" echo Fim: %date% %time%
>> "%LOG%" echo Codigo de saida: %resultado%

if "%resultado%"=="0" (
    echo Pipeline concluido com sucesso.
) else (
    echo ERRO: o pipeline falhou.
    echo.
    type "%LOG%"
)

echo.
echo Log salvo em: "%CD%\%LOG%"

REM Na execucao manual, aguarda uma tecla.
if /i not "%~1"=="agendado" pause

timeout /t 3 /nobreak >nul

exit /b %resultado%