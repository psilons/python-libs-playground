# https://www.toutiao.com/article/7089747658608624162/
# https://github.com/danielgatis/rembg

# pip install rembg
# pip install rembg[gpu] - GPU version

# cmd: rembg i path/to/input.png path/to/output.png
# web: rembg s

# Python - it downloads u2net data to local

from rembg import remove

input_path = 'mercedes_lake.jpg'
output_path = 'output.png'

with open(input_path, 'rb') as i:
    with open(output_path, 'wb') as o:
        input = i.read()
        output = remove(input)
        o.write(output)
