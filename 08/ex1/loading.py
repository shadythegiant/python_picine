import os 
import sys 
import importlib.metadata

def environment_check() -> bool:
    print("LOADING STATUS : loading Programs ... ")
    required = ['numpy', 'pandas', 'matplotlib']
    missing = False
    print("checking dependencies ...")
    for pkg in required :
        try:
          version = importlib.metadata.version(pkg)
          print(f"[OK] {pkg} {version} READY!!")
        except importlib.metadata.PackageNotFoundError:
           print(f"[MISSING] {pkg} - Not installed")
           missing = True
    if missing :
        print("\nError: Missing required programs.")
        print("Install using pip: pip install -r requirements.txt")
        print("Install using Poetry: poetry install")
        return False       
    
    return True


def run_matrix_analysis()-> None:
   import numpy as np 
   import pandas as pd 
   import matplotlib.pyplot as plt 
   print("\nAnalyzing Matrix data...")
   #1 numpy:
   data = np.random.rand(1000)
   #2 pandas :
   pdata = pd.DataFrame(data, columns=['Signal'])
   print(f"Processing {len(pdata)} data points...")
   #3 matplotlib
   plt.figure(figsize=(9 , 5))
   plt.hist(pdata["Signal"], bins=30, color='#00FF41', edgecolor='black')
   plt.title("Matrix Node Signal Distribution")
   plt.savefig("matrix_analysis.png")
   print("Analysis complete! Results saved to: matrix_analysis.png")

def main() -> None:
   if environment_check() :
      run_matrix_analysis()

if __name__ == "__main__":
   main()
        

