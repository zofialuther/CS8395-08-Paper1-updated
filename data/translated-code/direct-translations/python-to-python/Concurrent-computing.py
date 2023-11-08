import concurrent.futures

with concurrent.futures.ProcessPoolExecutor() as executor:
    _ = list(executor.map(print, 'Enjoy Rosetta Code'.split()))