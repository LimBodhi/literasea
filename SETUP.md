# Setup Literasea - Panduan Instalasi dan Deployment

## 🚀 Setup untuk Development Lokal

### 1. Persiapan Environment

```bash
# Clone repository (jika belum)
git clone <repository-url>
cd literasea

# Buat virtual environment
python -m venv venv

# Aktivasi virtual environment
# Di macOS/Linux:
source venv/bin/activate
# Di Windows:
# venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Konfigurasi Environment Variables

Buat file `.env` di root directory dengan isi berikut:

```env
# Django Configuration
SECRET_KEY=django-insecure-your-secret-key-here-change-this-in-production
DEBUG=True
DEVELOPMENT_MODE=True

# Database Configuration (untuk development lokal menggunakan SQLite)
# DATABASE_URL tidak diperlukan untuk development mode karena menggunakan SQLite

# Production Database (uncomment dan isi untuk production)
# DATABASE_URL=postgresql://username:password@host:port/database_name

# Allowed Hosts (tambahkan host lain jika diperlukan)
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1,.vercel.app

# CORS Settings
CORS_ALLOWED_ORIGINS=http://127.0.0.1:8000,http://localhost:8000

# Security Settings (untuk development)
CSRF_COOKIE_SECURE=False
SESSION_COOKIE_SECURE=False
```

### 3. Inisialisasi Database

```bash
# Buat dan jalankan migrasi
python manage.py makemigrations
python manage.py migrate

# Buat superuser (opsional)
python manage.py createsuperuser
```

### 4. Jalankan Server Development

```bash
# Jalankan server
python manage.py runserver

# Server akan berjalan di: http://127.0.0.1:8000/
```

## 🌐 Deployment ke Vercel

### 1. Persiapan untuk Production

#### Update file `.env` untuk production (atau buat environment variables di Vercel):

```env
# Django Configuration
SECRET_KEY=your-production-secret-key-very-long-and-secure
DEBUG=False
DEVELOPMENT_MODE=False

# Database Configuration (gunakan PostgreSQL untuk production)
DATABASE_URL=postgresql://username:password@host:port/database_name

# Allowed Hosts
DJANGO_ALLOWED_HOSTS=your-domain.vercel.app,localhost,127.0.0.1

# CORS Settings (sesuaikan dengan domain production)
CORS_ALLOWED_ORIGINS=https://your-domain.vercel.app

# Security Settings (untuk production)
CSRF_COOKIE_SECURE=True
SESSION_COOKIE_SECURE=True
```

### 2. Setup Database Production

**Option 1: PostgreSQL di Vercel**
- Buka Vercel Dashboard
- Pilih tab "Storage"
- Buat Postgres database baru
- Copy connection string ke `DATABASE_URL`

**Option 2: External PostgreSQL (Neon, Supabase, dll)**
- Daftar di provider pilihan
- Buat database baru
- Copy connection string ke `DATABASE_URL`

### 3. Environment Variables di Vercel

Di Vercel Dashboard > Settings > Environment Variables, tambahkan:

```
SECRET_KEY=your-production-secret-key
DEBUG=False
DEVELOPMENT_MODE=False
DATABASE_URL=postgresql://...
DJANGO_ALLOWED_HOSTS=your-domain.vercel.app
CORS_ALLOWED_ORIGINS=https://your-domain.vercel.app
CSRF_COOKIE_SECURE=True
SESSION_COOKIE_SECURE=True
```

### 4. Deploy ke Vercel

#### Via Vercel CLI:
```bash
# Install Vercel CLI
npm i -g vercel

# Login ke Vercel
vercel login

# Deploy
vercel --prod
```

#### Via Git Integration:
1. Push code ke GitHub/GitLab
2. Connect repository di Vercel Dashboard
3. Vercel akan auto-deploy setiap push ke main branch

### 5. Jalankan Migrasi di Production

Setelah deployment pertama:

```bash
# Via Vercel CLI
vercel exec -- python manage.py migrate

# Atau buat superuser
vercel exec -- python manage.py createsuperuser
```

## 🔧 Troubleshooting

### Masalah Umum:

1. **Error: ModuleNotFoundError**
   - Pastikan semua dependencies di `requirements.txt`
   - Jalankan `pip install -r requirements.txt`

2. **Database Error**
   - Periksa `DATABASE_URL` di environment variables
   - Pastikan database accessible dari Vercel

3. **Static Files tidak muncul**
   - Jalankan `python manage.py collectstatic`
   - Periksa konfigurasi `STATIC_URL` dan `STATIC_ROOT`

4. **CORS Error**
   - Periksa `CORS_ALLOWED_ORIGINS` sesuai dengan domain
   - Pastikan domain production sudah ditambahkan

### Environment Variables yang Diperlukan:

| Variable | Development | Production | Deskripsi |
|----------|-------------|------------|-----------|
| `SECRET_KEY` | ✅ | ✅ | Django secret key |
| `DEBUG` | `True` | `False` | Debug mode |
| `DEVELOPMENT_MODE` | `True` | `False` | Development mode |
| `DATABASE_URL` | ❌ | ✅ | PostgreSQL connection string |
| `DJANGO_ALLOWED_HOSTS` | ✅ | ✅ | Allowed hosts |
| `CORS_ALLOWED_ORIGINS` | ✅ | ✅ | CORS origins |
| `CSRF_COOKIE_SECURE` | `False` | `True` | CSRF cookie security |
| `SESSION_COOKIE_SECURE` | `False` | `True` | Session cookie security |

## 📝 Notes

- Untuk development lokal, gunakan `DEVELOPMENT_MODE=True` untuk SQLite
- Untuk production, gunakan `DEVELOPMENT_MODE=False` dan `DATABASE_URL` PostgreSQL
- Secret key production harus berbeda dan aman
- Pastikan domain production sudah ditambahkan ke `ALLOWED_HOSTS` dan `CORS_ALLOWED_ORIGINS` 