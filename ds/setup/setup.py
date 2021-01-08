"""
Module này hướng dãn cách cài đặt và chuẩn bị hệ thống python cơ bản.
Cài đặt trên MacOS
Cài đặt trên Windows
Cài đặt trên Linux
Setup environment

Cài đặt Pip

Cài đặt modules
"""

class mac_os():
    """
    Tải về python 3.7 tại https://www.python.org/downloads/release/python-379/ bản ”macOS 64-bit/32-
bit installer” và cài đặt như bất kỳ phần mềm nào khác.
    Tải Visual Studio Code tại https://code.visualstudio.com/download/ . Cài đặt như mọi phần mềm khác và bật lên, bấm [Command+Shift+X] hoặc bấm vào Extensions bar, search "Python" extension và cài cho Visual Studio Code.
    Trong cửa sổ Visual Studio Code, bật Terminal cho working directory hiện tại bằng cách bấm vào "Terminal > New Terminal" hoặc dùng phím tắt [Command+Shift+`]
    Nhập vào terminal command sau: ```python3 --version``` hoặc ```python3.7 --version``` Nếu xuất hiện output như vầy là đã cài python thành công:
    ```
    Python 3.7.9 (default, Jul 25 2020, 13:03:44)
    [GCC x.x.x] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>>
    ```
    Nhập tiếp vào terminal ```quit()``` để thoát python3 console.
    """

class windows():
    """
    Tải về python 3.7 tại https://www.python.org/downloads/release/python-379/ bản ”Windows x86-64 embeddable zip file” và cài đặt như bất kỳ phần mềm nào khác, tốt nhất nên cài ở ổ đĩa khác ổ đĩa hệ thống (khác C:\\ hoặc C:\Program....\\ vì nó thường đòi quyền Administrator, phiền lắm!). Lưu ý lúc cài nếu thấy hỏi có cài Pip module không thì nhớ tick vào nó nhé.
    Tải Visual Studio Code tại https://code.visualstudio.com/download/ . Cài đặt như mọi phần mềm khác và bật lên, bấm [Command+Shift+X] hoặc bấm vào Extensions bar, search "Python" extension và cài cho Visual Studio Code.
    Trong cửa sổ Visual Studio Code, bật Terminal cho working directory hiện tại bằng cách bấm vào "Terminal > New Terminal" hoặc dùng phím tắt [Command+Shift+`]
    Nhập vào terminal command sau: ```python3 --version``` hoặc ```python3.7 --version``` Nếu xuất hiện output như vầy là đã cài python thành công:
    ```
    Python 3.7.9 (default, Jul 25 2020, 13:03:44)
    [GCC x.x.x] on Windows
    Type "help", "copyright", "credits" or "license" for more information.
    >>>
    ```
    Nhập tiếp vào terminal ```quit()``` để thoát python3 console.
    Trong trường hợp gọi python bằng terminal không thành công, khả năng cao là khi cài đặt, python executable files không được đưa vào Path.
    Bật Start > Run (hoặc Ctrl+X) rồi chạy ```sysdm.cpl``` để bật System Properties. Chọn tab Advanced và bâm vào Environment Variables.
    Dưới mục System Variables, chọn ```Path``` variable và Edit nó.
    Thêm vào đường dẫn chứa thư mục đã cài python (ví dụ ```D:\\ Python37``` chẳng hạn).
    Tắt hết các terminal/cmd/powershell đi và bật lại để check python được cài chưa.
    """

class Linux():
    """
    Tải về python 3.7 tại https://www.python.org/downloads/release/python-379/ bản ”Windows x86-64 embeddable zip file” và cài đặt như bất kỳ phần mềm nào khác.
    Tải Visual Studio Code tại https://code.visualstudio.com/download/ . Cài đặt như mọi phần mềm khác và bật lên, bấm [Command+Shift+X] hoặc bấm vào Extensions bar, search "Python" extension và cài cho Visual Studio Code.
    Trong cửa sổ Visual Studio Code, bật Terminal cho working directory hiện tại bằng cách bấm vào "Terminal > New Terminal" hoặc dùng phím tắt [Command+Shift+`]
    Nhập vào terminal command sau: ```python3 --version``` hoặc ```python3.7 --version``` Nếu xuất hiện output như vầy là đã cài python thành công:
    ```
    Python 3.7.9 (default, Jul 25 2020, 13:03:44)
    [GCC x.x.x] on Debian
    Type "help", "copyright", "credits" or "license" for more information.
    >>>
    ```
    Nhập tiếp vào terminal ```quit()``` để thoát python3 console.
    """

class pip():
    """
    python-pip (pip, PyPip) là một module manager được xây dựng để quản lý các modules tích hợp cho python.
    Trên MacOS, mặc định có thể cài pip từ việc cài python3 (quá lời, vừa có python vừa khuyến mãi pip luôn!):
    ```
    sudo brew install python3
    ```
    Trên Linux (Ubuntu/Debian chẳng hạn) phải cài thêm, sau khi cài python3:
    ```
    sudo apt-get install python3-pip
    ```
    Trên Windows (10), đôi khi cũng phải cài thêm. Tải file này về: https://bootstrap.pypa.io/get-pip.py thư mục cài python rồi bật cmd lên, sử dụng lệnh ```cd``` để di chuyển đến thư mục vừa tải file đó về  (ví dụ ```cd D:\\ Python37```) rồi nhập vào terminal
    ```
    python get-pip.py
    ```
    """

class modules():
    """
    Sau khi đã cài hết python3, pip thì mới dùng pip để cài các modules. Có 4 modules thường xuyên dùng trong ngành data science: ```pandas, numpy, matplotlib, scipy```.
    Để cài cat bốn, nhập vào terminal (terminal của MacOS, linux, visual studio code hoặc cmd, powershell đều được):
    ```
    pip install pandas numpy scipy matplotlib
    ```
    Enjoy!
    Nếu có trục trặc, check lại python3 đã cài chưa, pip đã cài chưa, path đã được setup chưa, hoặc các modules này đều đã được cài từ trước.
    """