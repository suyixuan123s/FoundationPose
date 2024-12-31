'''
conda install boost=1.83.0

cmeel-boost               1.83.0                   pypi_0    pypi 保持一致

(foundationpose1) suyixuan@suyixuan-ASUS-TUF-Gaming-F16-FX607JVR-FX607JVR:~/AI/Pose_Estimation/FoundationPose$ conda list boost
# packages in environment at /home/suyixuan/anaconda3/envs/foundationpose1:
#
# Name                    Version                   Build  Channel
boost                     1.83.0               h8003fee_0    conda-forge
cmeel-boost               1.83.0                   pypi_0    pypi
libboost                  1.83.0               h6fcfa73_0    conda-forge
libboost-devel            1.83.0               h00ab1b0_0    conda-forge
libboost-headers          1.83.0               ha770c72_0    conda-forge
libboost-python           1.83.0           py39hda80f44_0    conda-forge
libboost-python-devel     1.83.0           py39h8003fee_0    conda-forge
(foundationpose1) suyixuan@suyixuan-ASUS-TUF-Gaming-F16-FX607JVR-FX607JVR:~/AI/Pose_Estimation/FoundationPose$


4. 完整的 CMake 配置示例
你可以将上述路径设置添加到 CMakeLists.txt 中或在终端中手动设置环境变量。示例如下：

bash
复制代码
export BOOST_INCLUDEDIR=$CONDA_PREFIX/include/boost
export BOOST_LIBRARYDIR=$CONDA_PREFIX/lib
export CMAKE_PREFIX_PATH=$CMAKE_PREFIX_PATH:$CONDA_PREFIX

export CMAKE_PREFIX_PATH=$CMAKE_PREFIX_PATH:/home/suyixuan/anaconda3/envs/foundationpose1:/home/suyixuan/anaconda3/envs/foundationpose1/lib:/home/suyixuan/anaconda3/envs/foundationpose1/include:/home/suyixuan/anaconda3/envs/foundationpose1/include/boost


export CMAKE_PREFIX_PATH="$CMAKE_PREFIX_PATH:$CONDA_PREFIX:$CONDA_PREFIX/lib:$CONDA_PREFIX/include:$CONDA_PREFIX/include/boost:$CONDA_PREFIX/include/eigen3/Eigen"



echo $CMAKE_PREFIX_PATH

export BOOST_INCLUDEDIR=$CONDA_PREFIX/include/boost
export BOOST_LIBRARYDIR=$CONDA_PREFIX/lib
export CMAKE_PREFIX_PATH=$CMAKE_PREFIX_PATH:$CONDA_PREFIX


export CMAKE_PREFIX_PATH="$CMAKE_PREFIX_PATH:$CONDA_PREFIX:$CONDA_PREFIX/lib:$CONDA_PREFIX/include:$CONDA_PREFIX/include/boost:$CONDA_PREFIX/include/eigen3/Eigen:$CONDA_PREFIX/lib/python3.9/site-packages/pybind11/share/cmake/pybind11"


'''