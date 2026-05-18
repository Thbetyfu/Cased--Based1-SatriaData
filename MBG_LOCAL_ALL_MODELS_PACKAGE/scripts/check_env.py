import sys
print("Python:", sys.version)
mods = ["numpy", "pandas", "sklearn", "scipy", "transformers", "accelerate", "lightgbm", "openpyxl", "torch"]
for m in mods:
    try:
        mod = __import__(m)
        print(f"{m}: OK", getattr(mod, "__version__", ""))
    except Exception as e:
        print(f"{m}: ERROR", repr(e))

try:
    import torch
    print("CUDA available:", torch.cuda.is_available())
    if torch.cuda.is_available():
        print("GPU:", torch.cuda.get_device_name(0))
        print("CUDA build:", torch.version.cuda)
        print("BF16 supported:", torch.cuda.is_bf16_supported())
        print("VRAM GB:", round(torch.cuda.get_device_properties(0).total_memory / (1024**3), 2))
except Exception as e:
    print("Torch check failed:", repr(e))
