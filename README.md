# DataScienceTask

#clone Daten/Skripte
git clone https://github.com/KWAYER66/DataScienceTask/
#Load Image
docker pull heatonresearch/jupyter-python-r
cd DataScienceTask
Python combine_csv.py
Python unzip.py
#local path to folder DataScienceTask
docker run -it --rm -p 8888:8888 -v [local path]:/root/mount/ docker-jupyter-python-r:latest
