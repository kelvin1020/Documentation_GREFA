=================================
服务器的使用
=================================

----------------------------
登录
----------------------------
- ssh 



----------------------------
conda 环境配置
----------------------------




在终端中输入 ``vi ~/.bashrc`` 按 **i** 进入编辑模式， 复制粘贴以下代码

``export PATH="/bin/anaconda3/bin:$PATH"``

按 **ESC** 退出编辑模式，按 **:** 进入命令模式，输入 **wq** 退出vim编辑

在终端中输入 ``source ~/.bashrc``
即配置了conda的路径，输入 ``conda init`` 会显示：

no change     /bin/anaconda3/condabin/conda
no change     /bin/anaconda3/bin/conda
no change     /bin/anaconda3/bin/conda-env
no change     /bin/anaconda3/bin/activate
no change     /bin/anaconda3/bin/deactivate
no change     /bin/anaconda3/etc/profile.d/conda.sh
no change     /bin/anaconda3/etc/fish/conf.d/conda.fish
no change     /bin/anaconda3/shell/condabin/Conda.psm1
no change     /bin/anaconda3/shell/condabin/conda-hook.ps1
no change     /bin/anaconda3/lib/python3.7/site-packages/xontrib/conda.xsh
no change     /bin/anaconda3/etc/profile.d/conda.csh
modified      /home/test/.bashrc

==> For changes to take effect, close and re-open your current shell. <==

根据提示关闭并重启终端，即配置好了conda环境，可以用于创建不同的python环境。

重新登录后，命令提示变为 ``(base) [[username]@HPz820 ~]$`` ，默认的python版本为python3， 安装了pycbc 和lal


执行
``conda deactivate`` 即可进入python2 环境， 使用python2 (但是用不了lal)

执行
``conda activate`` 即可再次进入python3 环境， 使用python3

