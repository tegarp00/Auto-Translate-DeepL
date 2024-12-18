import keyboard
import pyperclip
import pyautogui
import deepl
import time
from dotenv import load_dotenv
import os

# Muat .env file
load_dotenv()

DEEPL_API_KEY = os.getenv("DEEPL_API_KEY")

def translate_with_deepl(text):
    """Menerjemahkan teks menggunakan DeepL API."""
    translator = deepl.Translator(DEEPL_API_KEY)
    
    try:
        # Mentranslate teks dari bahasa Indonesia ke bahasa Inggris (gunakan EN-GB atau EN-US)
        result = translator.translate_text(text, source_lang="ID", target_lang="EN-US")
        return result.text
    except deepl.exceptions.DeepLException as e:
        print(f"Terjadi error: {e}")
        return None

def capture_and_translate_all():
    """Blok semua teks atau terjemahkan teks yang diblokir."""
    # Tekan Ctrl + A untuk memilih seluruh teks jika tidak ada teks yang diblokir
    pyautogui.hotkey("ctrl", "a")
    time.sleep(0.5)  # Memberi waktu untuk teks terblokir dengan baik

    # Salin teks yang dipilih (Ctrl + C)
    pyautogui.hotkey("ctrl", "c")
    time.sleep(1)  # Menunggu lebih lama untuk memastikan clipboard terisi
    text = pyperclip.paste()

    if not text or text == "":
        print("Tidak ada teks yang dipilih atau teks kosong.")
        return

    print(f"Teks untuk diterjemahkan: {text}")
    translated_text = translate_with_deepl(text)

    if translated_text:
        # Ganti teks di input dengan hasil terjemahan
        pyperclip.copy(translated_text)
        pyautogui.hotkey("ctrl", "v")
        print(f"Hasil terjemahan: {translated_text}")
    else:
        print("Gagal menerjemahkan teks.")

def capture_and_translate_selected():
    """Terjemahkan hanya teks yang sedang diblokir."""
    # Salin teks yang dipilih (Ctrl + C)
    pyautogui.hotkey("ctrl", "c")
    time.sleep(1)  # Menunggu lebih lama untuk memastikan clipboard terisi
    text = pyperclip.paste()

    if not text or text == "":
        print("Tidak ada teks yang dipilih atau teks kosong.")
        return

    print(f"Teks untuk diterjemahkan: {text}")
    translated_text = translate_with_deepl(text)

    if translated_text:
        # Ganti teks yang terblokir dengan hasil terjemahan
        pyperclip.copy(translated_text)
        pyautogui.hotkey("ctrl", "v")
        print(f"Hasil terjemahan: {translated_text}")
    else:
        print("Gagal menerjemahkan teks.")

# Daftarkan shortcut key
keyboard.add_hotkey("ctrl+y", capture_and_translate_all)  # Ctrl + Y untuk blok semua atau terjemahkan yang diblokir
keyboard.add_hotkey("ctrl+m", capture_and_translate_selected)  # Ctrl + M untuk terjemahkan yang diblokir saja

print("Shortcut aktif! Tekan Ctrl + Y untuk memilih semua teks atau Ctrl + M untuk menerjemahkan yang diblokir.")
keyboard.wait()  # Aplikasi Mati (Ctrl + C)