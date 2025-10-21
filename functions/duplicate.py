import shutil
import os
def duplicate(srcfile, dstdir):
    os.makedirs(dstdir, exist_ok=True)
    try:
        shutil.copy(srcfile, dstdir)
    except FileNotFoundError:
        print(f"Error: Source file '{srcfile}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

duplicate("fastafiles/p53.fasta", "duplicates/")