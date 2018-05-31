## ------------------------- ##
##
## get_and_unpack.py
## Script to download and unzip data.
##
## ------------------------- ##

import wget, argparse, zipfile, os

def get_and_unpack(url, location='.'):

	#Download file
	print('\033[1m' + ' Downloading...this might take a little while...' + '\033[0m')
	filename = wget.download(url, out=location)

	#Unzip
	print('\n' +  '\033[1m' + ' Unzipping...' + '\033[0m')
	zip_ref = zipfile.ZipFile(filename, 'r')
	zip_ref.extractall(path=location)
	zip_ref.close()

	#Remove zip file
	os.remove(filename)


	print('\033[1m' + 'Done!' + '\033[0m')




### --------------------------------- ###
if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='(python get_and_unpack.py -url web_address')

	parser.add_argument("-url", dest='url', required=True, help='web_address')
	args = parser.parse_args()

	get_and_unpack(args.url)



