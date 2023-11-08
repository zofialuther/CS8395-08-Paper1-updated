from concurrent.futures import ProcessPoolExecutor

executor = ProcessPoolExecutor()

_ = list(executor.map(print, 'Enjoy Rosetta Code'.split()))