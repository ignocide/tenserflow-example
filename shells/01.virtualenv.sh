
# install a tensorflow 
virtualenv --system-site-packages ~/tensorflow

source ~/tensorflow/bin/activate

# sudo pip install --upgrade https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-1.3.0rc0-cp27-none-linux_x86_64.whl
sudo pip install --upgrade --pre tensorflow
sudo easy_install --upgrade six
