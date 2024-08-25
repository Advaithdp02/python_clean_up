import os
import collections
from pprint import pprint
import shutil

ext_img=['jpg','jpeg','png','Screenshot']
ext_vid=['mp4','mkv','avi']
ext_doc=['pdf','docx','ppt']
ext_comp=['zip','tar']
ext_inst=['dmg','iso','exe']

dir_item=['movie','image',"module",'Compression','installation']
downloads_path = os.path.expanduser('~/Downloads')+'/'

files=os.listdir(downloads_path)
for dir in dir_item:
    if not os.path.exists(downloads_path+dir):
        os.mkdir(downloads_path+dir)

file_mapping=collections.defaultdict(list)

for file_name in files:
    if file_name[0] != '.':
        file_ext=file_name.split('.')[-1]
        file_mapping[file_ext].append(file_name)


for f_ext,f_list in file_mapping.items():
    if f_ext in ext_comp:
        for file in f_list:
            shutil.move(downloads_path+file , downloads_path+"Compression")
    if f_ext in ext_img:
        for file in f_list:
            shutil.move(downloads_path+file , downloads_path+"image")
    if f_ext in ext_vid:
        for file in f_list:
            shutil.move(downloads_path+file , downloads_path+"movie")
    if f_ext in ext_doc:
        for file in f_list:
            shutil.move(downloads_path+file , downloads_path+"module")
    if f_ext in ext_inst:
        for file in f_list:
            shutil.move(downloads_path+file , downloads_path+"installation")
    