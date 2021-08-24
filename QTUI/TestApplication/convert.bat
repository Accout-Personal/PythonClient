
for %%f in (*.ui) do (

    if "%%~xf"==".ui" pyuic5 form.ui > formpython.py
	set mypath=%cd%
@echo %mypath%
Pause
    echo %%f
)
