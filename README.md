# Auto Translate (DeepL)

Ini adalah aplikasi untuk menerjemahkan teks menggunakan DeepL API. Aplikasi ini dapat mendeteksi teks yang terblok dan menerjemahkannya, baik seluruh teks yang dipilih atau hanya teks yang terblok.

## Fitur

- Terjemahkan teks yang diblok dengan shortcut.
- Pilih seluruh teks dengan shortcut dan terjemahkan.
- Gunakan DeepL API untuk menerjemahkan teks dari bahasa Indonesia ke bahasa Inggris.

## Persyaratan

Sebelum mulai, pastikan kamu telah menginstall alat-alat berikut:
- Python 3.10 atau versi lebih baru
- `pip` (Python package manager)

## Langkah-langkah Penggunaan

Ikuti langkah-langkah berikut untuk menjalankan aplikasi ini di lokal setelah meng-clone repository.

### 1. Clone Repository

Clone project ini ke komputer kamu menggunakan perintah berikut:

```bash
git clone https://github.com/tegarp00/Auto-Translate-DeepL.git

cd auto-translate

cp .env.example .env

python -m venv venv

venv\Scripts\activate || Windows

source venv/bin/activate || Linux

pip install -r requirements.txt

python main.py
```