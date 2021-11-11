服务器的使用
=================================


服务器登录
----------------------------
- mac或Linux系统

使用终端，输入

.. code-block:: console

		$ ssh your_user_name@119.78.226.66
		

根据提示输入密码即可登录。

- windows系统

推荐使用xshell和xftp软件



服务器创建新用户(Root用户)
----------------------------
创建用户名为user_name的用户:

.. code-block:: console

          $ useradd user_name


设置密码

.. code-block:: console

          $ passwd user_name


根据提示设置好密码即可。

 
ifort编译器配置
----------------------------

在终端中输入 ``vi ~/.bashrc`` 按 **i** 进入编辑模式， 复制粘贴以下代码

``source /opt/intel/oneapi/setvars.sh``

按 **ESC** 退出编辑模式，按 **:** 进入命令模式，输入 **wq** 退出vim编辑

在终端中输入 ``source ~/.bashrc``

即配置好ifort编译器环境。



服务器远程运行jupyter Notebook
------------------------------------

服务器可远程运行jupyter Notebook，方法如下:





