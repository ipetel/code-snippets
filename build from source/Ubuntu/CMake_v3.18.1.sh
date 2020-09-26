# When compiling packages from source, some times you will need CMake version to be higher than the latest version that available in the "apt install"

# 1) delete the current version 
	cmake --version # check the exising version
	sudo apt remove --purge --auto-remove cmake # remove it 

# 2) download the source code + unzip it
	wget https://cmake.org/files/v3.18/cmake-3.18.1.tar.gz
	tar -xzvf cmake-3.18.1.tar.gz
	cd cmake-3.18.1/

# 3) install prerequisites + compile 
  sudo apt-get install -y libblas-dev liblapack-dev libssl-dev
  ./bootstrap
  make -j4 # the value "4" after "-j" is the count of CPU in the machine you are running the compile process on
  sudo make install
  PATH=$PATH:/usr/local/bin # add CMake to the PATH
  
