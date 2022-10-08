import os

#base_dir = "vis_voc07"
base_dir = "vis_coco14"
html_str = ""
for file_name in os.listdir(base_dir):
    html_str +="<center><img src=\"{}\" width=\"1000\"></center>\n".format(os.path.join("images",base_dir,file_name))
print(html_str)

