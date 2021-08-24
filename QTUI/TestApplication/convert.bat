echo off
set mypath=%cd%

@echo "path is: "
@echo %mypath%
for %%f in (*.ui) do (

    if "%%~xf"==".ui" (	
		call pyuic5 %%f > %%~nf.py
		@echo %%f converted
	)
)
Pause