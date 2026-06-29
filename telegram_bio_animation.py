import asyncio
from telethon import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest
import os
import time

# Конфигурация
API_ID = int(os.getenv('API_ID', '0'))
API_HASH = os.getenv('API_HASH', '')
PHONE = os.getenv('PHONE', '')

# Параметры анимации
PREFIX = 'Lewis'
ANIMATE = 'Hamilton'
SUFFIX = '| KZT'
ERROR_CHARS = 'nnn'
SPEED = 0.08  # секунды между символами
CYCLE_PAUSE = 3  # пауза между циклами (секунды)

# Инициализация клиента
client = TelegramClient('session_name', API_ID, API_HASH, phone_number=PHONE)

async def update_bio(text):
    """Обновляет биографию"""
    try:
        await client(UpdateProfileRequest(about=text))
        print(f'✅ Bio updated: "{text}"')
    except Exception as e:
        print(f'❌ Error updating bio: {e}')

async def animate_bio():
    """Основная анимация биографии"""
    full_text = f'{PREFIX} {ANIMATE} {SUFFIX}'
    error_text = f'{PREFIX} {ANIMATE}{ERROR_CHARS} {SUFFIX}'
    
    print(f'🎬 Starting animation...')
    print(f'Full text: {full_text}')
    print(f'Error text: {error_text}')
    
    while True:
        try:
            # === ЭТАП 1: Печать с ошибкой ===
            print('\n📝 Step 1: Typing with error...')
            for i in range(len(error_text) + 1):
                await update_bio(error_text[:i])
                await asyncio.sleep(SPEED)
            
            await asyncio.sleep(0.5)
            
            # === ЭТАП 2: Удаление до середины ===
            print('🗑️ Step 2: Deleting to middle...')
            target_length = len(error_text) // 2
            current_bio = error_text
            
            while len(current_bio) > target_length:
                current_bio = current_bio[:-1]
                await update_bio(current_bio)
                await asyncio.sleep(0.05)
            
            await asyncio.sleep(0.3)
            
            # === ЭТАП 3: Исправление ===
            print('✏️ Step 3: Correcting...')
            current_bio = error_text[:target_length]
            
            for i in range(target_length, len(full_text) + 1):
                await update_bio(full_text[:i])
                await asyncio.sleep(SPEED)
            
            print('✅ Animation cycle complete!')
            
            # Пауза перед следующим циклом
            await asyncio.sleep(CYCLE_PAUSE)
            
        except Exception as e:
            print(f'❌ Animation error: {e}')
            await asyncio.sleep(5)

async def main():
    """Главная функция"""
    print('🚀 Starting Telegram Bio Animation Bot...')
    
    # Проверка учётных данных
    if not API_ID or not API_HASH or not PHONE:
        print('❌ Missing credentials! Set API_ID, API_HASH, PHONE as environment variables')
        print('   Get them from: https://my.telegram.org/apps')
        return
    
    async with client:
        try:
            # Подключение
            await client.connect()
            print(f'✅ Connected to Telegram')
            
            # Проверка авторизации
            if not await client.is_user_authorized():
                print(f'📱 Requesting authorization for {PHONE}...')
                await client.send_code_request(PHONE)
                
                # Запрос кода
                code = input('Enter the code you received: ')
                try:
                    await client.sign_in(PHONE, code)
                except Exception as e:
                    print(f'❌ Authorization failed: {e}')
                    return
            
            print('✅ Authorization successful!')
            
            # Получение информации о пользователе
            me = await client.get_me()
            print(f'👤 Logged in as: {me.first_name}')
            
            # Запуск анимации
            await animate_bio()
            
        except Exception as e:
            print(f'❌ Fatal error: {e}')
        finally:
            await client.disconnect()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('\n⏹️ Animation stopped by user')
