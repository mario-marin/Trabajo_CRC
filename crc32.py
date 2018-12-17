import zlib
import os
import io

file_name = 'path/to/some/file' # Path to some file

buffer_size = io.DEFAULT_BUFFER_SIZE # 4096

file_size = os.stat(file_name).st_size

percentage_per_iter = buffer_size / file_size # *100 Not needed 'cause the .format does the job
current_percent = 0
last_percent = 0


print('\rCalculating... {percentage:.5%}'.format(percentage=current_percent), end='')

with open(file_name, 'rb') as f:
    crc = 0 # Seed value
    for chunk in iter(lambda: f.read(buffer_size), b''):
        crc = zlib.crc32(chunk, crc) # Update the CRC with the contents of the file
        current_percent += percentage_per_iter
        if current_percent - last_percent >= 1/100:
            last_percent = current_percent
            print('\rCalculating... {percentage:.5%}'.format(percentage=current_percent), end='')

print('\rAll done!!!... {percentage:.5%}'.format(percentage=1))

print('Calculated CRC32: ', crc)
print('Calculated CRC32 (hex): ', hex(crc))

# os.stat('somefile').st_size returns size in bytes
