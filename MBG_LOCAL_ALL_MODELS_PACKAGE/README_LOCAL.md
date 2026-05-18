# MBG Local All Models V4

Versi ini adalah konversi lokal dari pipeline V4. Semua model transformer dari V4 tetap ada, tetapi batch size, max length, dan gradient accumulation otomatis disesuaikan dengan profil lokal.

## Isi Paket

```text
notebooks/MBG_LOCAL_ALL_MODELS_V4.ipynb
data/case_1_labeled_data.xlsx
data/case_1_text_to_predict.xlsx
data/case_1_template_sheet.xlsx
requirements_local.txt
scripts/check_env.py
scripts/run_jupyter_local.bat
scripts/run_jupyter_local.sh
scripts/install_torch_cuda121.bat
scripts/install_torch_cuda121.sh
```

## Profil Lokal

Notebook membaca environment variable `MBG_LOCAL_PROFILE`.

| Profil | Target | Model |
|---|---|---|
| `AUTO` | Deteksi otomatis VRAM | Semua model |
| `LOCAL_SAFE` | GPU 6–8 GB / sangat aman | Semua model dengan batch kecil + grad accumulation |
| `LOCAL_12GB` | GPU sekitar 10–16 GB | Semua model dengan batch menengah |
| `LOCAL_24GB` | GPU sekitar 20–24 GB | Semua model lebih cepat |
| `LOCAL_MAX` | GPU 32 GB ke atas / server | Hampir sama dengan A100 style |

Default:
```text
MBG_LOCAL_PROFILE=AUTO
MBG_LOCAL_ALL_MODELS=1
```

Artinya semua model tetap dijalankan selama tidak gagal OOM. Kalau satu model OOM, notebook akan retry dengan batch lebih kecil. Kalau tetap gagal, model itu dilewati dan pipeline tetap lanjut.

## Instalasi Windows

Buka PowerShell/CMD dari folder paket.

```bat
python -m venv .venv
.venv\Scripts\activate
python -m pip install -U pip
```

Install PyTorch GPU sesuai versi CUDA driver kamu melalui selector resmi PyTorch. Untuk CUDA 12.1, kamu bisa memakai script:

```bat
scripts\install_torch_cuda121.bat
```

Lalu install dependency lain:

```bat
pip install -r requirements_local.txt
```

Cek environment:

```bat
python scripts\check_env.py
```

Jalankan Jupyter:

```bat
scripts\run_jupyter_local.bat
```

## Instalasi Linux/macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
```

Untuk CUDA 12.1:

```bash
bash scripts/install_torch_cuda121.sh
```

Lalu:

```bash
pip install -r requirements_local.txt
python scripts/check_env.py
bash scripts/run_jupyter_local.sh
```

## Cara Menjalankan Notebook

1. Buka `notebooks/MBG_LOCAL_ALL_MODELS_V4.ipynb`.
2. Ganti:
   ```python
   TEAM_NAME = "nama_tim"
   ```
   menjadi nama tim kamu.
3. Jalankan cell dari atas sampai bawah.
4. Output utama akan dibuat di:
   ```text
   mbg_bdc_local_work/outputs/
   ```
5. File submission utama juga akan dicopy ke root notebook sebagai:
   ```text
   nama_tim.xlsx
   ```

## Mengubah Profil

Windows:

```bat
set MBG_LOCAL_PROFILE=LOCAL_12GB
set MBG_LOCAL_ALL_MODELS=1
jupyter lab
```

Linux/macOS:

```bash
export MBG_LOCAL_PROFILE=LOCAL_12GB
export MBG_LOCAL_ALL_MODELS=1
jupyter lab
```

## Catatan Penting

- `TAPT_USE_TEST_TEXT = False` tetap dipertahankan agar konservatif terhadap aturan kompetisi.
- Tidak ada data eksternal.
- Tidak ada manual labeling.
- Tidak ada LLM/generative AI untuk prediksi, anotasi, pseudo-labeling, atau augmentasi label data uji.
- Jika VRAM kecil, runtime akan lama karena semua model tetap dikonversi untuk lokal, bukan dihapus.
- Jika ingin cepat, set `MBG_LOCAL_ALL_MODELS=0`; notebook hanya mengambil subset awal model.
