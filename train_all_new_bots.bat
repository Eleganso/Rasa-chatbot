@echo off
echo ========================================
echo    ТРЕНИРАНЕ НА ВСИЧКИ НОВИ БОТОВЕ
echo ========================================
echo.
echo 💡 Уверете се, че Docker Desktop е стартиран!
echo.
pause
echo.
echo 🚀 Стартиране на трениране...
echo.

echo 📚 Трениране на Салон 'Златна коса'...
call train_zlatna_kosa.bat
if %errorlevel% neq 0 (
    echo ❌ Грешка при трениране на Салон 'Златна коса'
    pause
    exit /b 1
)

echo.
echo 📚 Трениране на Ресторант 'Златна вилица'...
call train_zlatna_vilitsa.bat
if %errorlevel% neq 0 (
    echo ❌ Грешка при трениране на Ресторант 'Златна вилица'
    pause
    exit /b 1
)

echo.
echo 📚 Трениране на Хотел 'Гранд София'...
call train_grand_sofia.bat
if %errorlevel% neq 0 (
    echo ❌ Грешка при трениране на Хотел 'Гранд София'
    pause
    exit /b 1
)

echo.
echo 📚 Трениране на Медицински център 'Здраве+'...
call train_zdrave_medical.bat
if %errorlevel% neq 0 (
    echo ❌ Грешка при трениране на Медицински център 'Здраве+'
    pause
    exit /b 1
)

echo.
echo 📚 Трениране на Автосервиз 'Мото Експерт'...
call train_moto_expert.bat
if %errorlevel% neq 0 (
    echo ❌ Грешка при трениране на Автосервиз 'Мото Експерт'
    pause
    exit /b 1
)

echo.
echo 🎉 Всички ботове са тренирани успешно!
echo.
echo 📤 Следваща стъпка: Качване на моделите на VPS
echo 💡 Изпълнете: python upload_models_to_vps.py
echo.
pause
