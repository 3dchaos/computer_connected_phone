import tkinter as tk
from searchMyPhone import DeviceManager

class DeviceCheckerApp:
    def __init__(self, master):
        self.master = master
        master.title("Device Check")
        master.geometry("150x200")
        master.resizable(False, False)  # 设置主窗口大小不可调整
        master.attributes('-topmost', True)  # 置顶窗口

        # 创建 DeviceManager 实例
        self.device_manager = DeviceManager()

        # 设备名称
        self.DeviceName = "Apple iPhone"

        # 设置全局变量来控制循环
        self.keep_checking = False

        # 添加标题控件，并设置默认文字和颜色
        self.title_label = tk.Label(master, text="等待检测", font=("Helvetica", 15), fg="gray")
        self.title_label.pack(pady=10)

        # 添加按钮，并直接绑定 start_checking() 函数
        self.btn_check = tk.Button(master, text="开始检测", command=self.start_checking)
        self.btn_check.pack(pady=10)

        # 添加设备名称标签
        self.device_label = tk.Label(master, text="检测："+self.DeviceName)
        self.device_label.pack(pady=10)

    def check_device(self):
        # 判断是否有设备连接到计算机
        result = self.device_manager.contains_device(self.DeviceName)
        print("Result:", result)
        # 设置标题文字和颜色
        if result:
            self.title_label.config(text="正常连接", fg="green")
        else:
            self.title_label.config(text="连接失败", fg="red")
            # 当检测到连接失败时，停止循环并延迟3秒后锁定屏幕
            self.keep_checking = False
            self.master.after(3000, self.device_manager.lock_screen)
        # 每5秒执行一次 check_device()
        if self.keep_checking:
            self.master.after(5000, self.check_device)

    def start_checking(self):
        self.keep_checking = True
        self.check_device()

if __name__ == "__main__":
    root = tk.Tk()
    app = DeviceCheckerApp(root)
    root.mainloop()
