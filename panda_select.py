import pandas as pd

chunksize = 1000000
chunk_index = 77
chunks = []
chunk_counter = 0

for i, chunk in enumerate(pd.read_csv("s3://tfg-upload-2023-05-10/large-data-file.csv", chunksize=chunksize, header=None)):
    chunk_counter += 1
    if i == chunk_index:
        for row in chunk.itertuples(index=False, name=None):
            chunks.append(row)
        break

df = pd.DataFrame(chunks, columns=None)
print(df.to_string(header=False, index=False))
print("Total number of chunks in file:", chunk_counter)
