#This is just a walkthough of commands you can run on MSI's login node to easily install mutation motif
# https://bitbucket.org/pycogent3/mutationmotif



#If you don't have mercurial installed ("hg" command)
wget https://www.mercurial-scm.org/release/mercurial-4.4.tar.gz
tar -xvzf mercurial-4.4.tar.gz
cd mercurial-4.4
make local

#export mercurial path in your .bashrc to this DIR
#Something like this at the end of the file (use "pwd -P" if you don't know the full path)
export PATH=/home/<USER>/Software/mercurial-4.4

cd ..
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
#follow the prompts and say yes to adding local path to .bashrc

#source .bashrc to take .bashrc changes into effect
source ~/.bashrc


#create env, this one is called MutMot using python3
conda create --name MutMot python=3.6
source activate MutMot

#conda prefers using it's own install, plus MutationMotif rpy2 pip install will break later in the install
#if we conda install rpy2 before hand, it will be correct and it won't be overridden. 
conda install numpy rpy2
#cogent also won't install with mutation motif
DONT_USE_CYTHON=1 pip install hg+https://bitbucket.org/pycogent3/cogent3

#You can then pip install mutation motif with will have no problem pulling the other pacakges
#    even though it is pip install and not conda
pip install hg+https://bitbucket.org/pycogent3/mutationmotif
