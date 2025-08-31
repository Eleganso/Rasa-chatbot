# МУЛТИ-БОТ СИСТЕМА - ТЕСТОВЕ
# PowerShell скрипт за тестване на всички ботове

Write-Host "========================================" -ForegroundColor Green
Write-Host "    МУЛТИ-БОТ СИСТЕМА - ТЕСТОВЕ" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""

# Функция за тестване на бот
function Test-Bot {
    param(
        [string]$BotName,
        [string]$Port,
        [string]$TestMessage
    )
    
    Write-Host "Тестване на $BotName (Порт $Port)..." -ForegroundColor Yellow
    Write-Host "Съобщение: '$TestMessage'" -ForegroundColor Cyan
    
    try {
        $body = @{
            sender = "test"
            message = $TestMessage
        } | ConvertTo-Json
        
        $response = Invoke-RestMethod -Uri "http://localhost:$Port/webhooks/rest/webhook" -Method POST -ContentType "application/json" -Body $body -TimeoutSec 10
        
        Write-Host "✅ УСПЕХ!" -ForegroundColor Green
        Write-Host "Отговор: $($response.text)" -ForegroundColor White
        Write-Host ""
        return $true
    }
    catch {
        Write-Host "❌ ГРЕШКА!" -ForegroundColor Red
        Write-Host "Проблем: $($_.Exception.Message)" -ForegroundColor Red
        Write-Host ""
        return $false
    }
}

# Проверка дали има активни контейнери
Write-Host "Проверка на активни контейнери..." -ForegroundColor Yellow
$containers = docker ps --format "table {{.Names}}\t{{.Ports}}" 2>$null

if ($containers -and $containers.Length -gt 1) {
    Write-Host "Намерени активни контейнери:" -ForegroundColor Green
    Write-Host $containers -ForegroundColor White
    Write-Host ""
} else {
    Write-Host "❌ Няма активни контейнери!" -ForegroundColor Red
    Write-Host "Стартирайте първо бот с MULTI_BOT_MENU.bat" -ForegroundColor Yellow
    Write-Host ""
    Read-Host "Натиснете Enter за изход"
    exit
}

# Меню за избор на бот за тестване
Write-Host "Изберете бот за тестване:" -ForegroundColor Cyan
Write-Host "[1] DragonForgedDreams V2 (Порт 5005)" -ForegroundColor White
Write-Host "[2] Салон 'Златна коса' (Порт 5006)" -ForegroundColor White
Write-Host "[3] Ресторант 'Златна вилица' (Порт 5007)" -ForegroundColor White
Write-Host "[4] Хотел 'Гранд София' (Порт 5008)" -ForegroundColor White
Write-Host "[5] Медицински център 'Здраве+' (Порт 5009)" -ForegroundColor White
Write-Host "[6] Автосервиз 'Мото Експерт' (Порт 5010)" -ForegroundColor White
Write-Host "[A] Тестване на всички ботове" -ForegroundColor White
Write-Host "[Q] Изход" -ForegroundColor White
Write-Host ""

$choice = Read-Host "Въведете избор"

switch ($choice) {
    "1" {
        $testMessage = Read-Host "Въведете съобщение за тестване (или натиснете Enter за 'здравей')"
        if (-not $testMessage) { $testMessage = "здравей" }
        Test-Bot -BotName "DragonForgedDreams V2" -Port "5005" -TestMessage $testMessage
    }
    "2" {
        $testMessage = Read-Host "Въведете съобщение за тестване (или натиснете Enter за 'имате ли свободно време')"
        if (-not $testMessage) { $testMessage = "имате ли свободно време" }
        Test-Bot -BotName "Салон 'Златна коса'" -Port "5006" -TestMessage $testMessage
    }
    "3" {
        $testMessage = Read-Host "Въведете съобщение за тестване (или натиснете Enter за 'какво има в менюто')"
        if (-not $testMessage) { $testMessage = "какво има в менюто" }
        Test-Bot -BotName "Ресторант 'Златна вилица'" -Port "5007" -TestMessage $testMessage
    }
    "4" {
        $testMessage = Read-Host "Въведете съобщение за тестване (или натиснете Enter за 'имате ли свободни стаи')"
        if (-not $testMessage) { $testMessage = "имате ли свободни стаи" }
        Test-Bot -BotName "Хотел 'Гранд София'" -Port "5008" -TestMessage $testMessage
    }
    "5" {
        $testMessage = Read-Host "Въведете съобщение за тестване (или натиснете Enter за 'кога мога да се запиша')"
        if (-not $testMessage) { $testMessage = "кога мога да се запиша" }
        Test-Bot -BotName "Медицински център 'Здраве+'" -Port "5009" -TestMessage $testMessage
    }
    "6" {
        $testMessage = Read-Host "Въведете съобщение за тестване (или натиснете Enter за 'имате ли свободно време за ремонт')"
        if (-not $testMessage) { $testMessage = "имате ли свободно време за ремонт" }
        Test-Bot -BotName "Автосервиз 'Мото Експерт'" -Port "5010" -TestMessage $testMessage
    }
    "A" {
        Write-Host "Тестване на всички ботове..." -ForegroundColor Yellow
        Write-Host ""
        
        $bots = @(
            @{Name="DragonForgedDreams V2"; Port="5005"; Message="здравей"},
            @{Name="Салон 'Златна коса'"; Port="5006"; Message="имате ли свободно време"},
            @{Name="Ресторант 'Златна вилица'"; Port="5007"; Message="какво има в менюто"},
            @{Name="Хотел 'Гранд София'"; Port="5008"; Message="имате ли свободни стаи"},
            @{Name="Медицински център 'Здраве+'"; Port="5009"; Message="кога мога да се запиша"},
            @{Name="Автосервиз 'Мото Експерт'"; Port="5010"; Message="имате ли свободно време за ремонт"}
        )
        
        $successCount = 0
        foreach ($bot in $bots) {
            $result = Test-Bot -BotName $bot.Name -Port $bot.Port -TestMessage $bot.Message
            if ($result) { $successCount++ }
            Start-Sleep -Seconds 1
        }
        
        Write-Host "========================================" -ForegroundColor Green
        Write-Host "РЕЗУЛТАТИ ОТ ТЕСТОВЕТЕ:" -ForegroundColor Green
        Write-Host "Успешни: $successCount от $($bots.Count)" -ForegroundColor White
        Write-Host "========================================" -ForegroundColor Green
    }
    "Q" {
        Write-Host "Изход от тестовете..." -ForegroundColor Yellow
        exit
    }
    default {
        Write-Host "Невалиден избор!" -ForegroundColor Red
    }
}

Write-Host ""
Read-Host "Натиснете Enter за изход"
