=================================
打印机
=================================

课题组共有两台打印机:


a.一台彩色打印机在韩文标老师的办公室(1009)


b.一台黑白打印机在研究生办公室(1008)，目前该打印机连在了台式机上，并已经在网络上共享，打印机网络地址为:

> http://202.127.24.94:631/printers/HP-LaserJet-Pro-MFP-M226dw-2


一、Windows 系统连接办法: 可利用添加打印机向导，利用上面的网络地址连接

二、Mac连接办法:

(1)在浏览器中输入 ``localhost:631``，打不开的话可以根据提示在终端中输入:
``service cups start``

(2)在打开的页面，点击 ``Add Printer``， 在弹出的页面 Other Network Printers 中选择 **互联网打印协议(ipp)**

(3)在弹出的页面 ``Connection`` 选项里将上面的地址输入打印机的信息(Description 为显示的打印机名称)，点击 Continue 继续

(4)在 ``make`` 选项中选择 **Generic**，点击 Continue 后选择 **Generic PostSCript Printer**，最后点击 **Add Printer**

(5)进行一些打印机的默认设置，最后点击 **Set Default Options** ，即成功连接1008的打印机