@echo off
setlocal enabledelayedexpansion

rem Create a temporary file for error logging
set "tempfile=temp_error.log"
del "%tempfile%" 2>nul

for %%f in (..\codigosMiniB\*.bas) do (
    python Main.py "%%f" -m cve > nul 2>> "%tempfile%"
    if errorlevel 1 (
        echo Error processing file: %%f
        echo Detalles del error:
        type "%tempfile%"
        del "%tempfile%" 2>nul
    ) else (
        echo %%f ha sido procesado correctamente
    )
)

rem Check if the temp file has any content indicating a VerifyError
findstr /C:"VerifyError" "%tempfile%" > nul
if !errorlevel! == 0 (
    echo Se encontró un error de verificación en uno de los archivos procesados.
)

rem Clean up the temporary file
del "%tempfile%" 2>nul

echo Procesamiento completado.
endlocal
