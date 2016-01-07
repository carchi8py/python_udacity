import os
def rename_files():
	file_list = os.listdir("/Users/carchi/code/Full stack/python/prank")
	for file_name in file_list:
		print file_name
		cwd = os.getcwd()
		os.chdir("/Users/carchi/code/Full stack/python/prank")
		os.rename(file_name, file_name.translate(None, "0123456789"))
		os.chdir(cwd)

rename_files()