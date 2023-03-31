from prometheus_client import start_http_server, Gauge
import mysql.connector
from time import sleep

# Tạo một đối tượng Gauge để theo dõi trạng thái kết nối
mysql_connection_status = Gauge('mysql_connection_status', 'MySQL connection status')

def check_mysql_connection():
    try:
        # Thực hiện kết nối đến MySQL
        cnx = mysql.connector.connect(user='username', password='password', host='localhost', database='dbname')
        cnx.close()
        # Đặt giá trị Gauge thành 1 để đại diện cho kết nối thành công
        mysql_connection_status.set(1)
        
    except mysql.connector.Error as err:
        # Nếu có lỗi khi kết nối đến MySQL, đặt giá trị Gauge thành 0 để đại diện cho kết nối thất bại
        mysql_connection_status.set(0)

# Bắt đầu một web server Prometheus trên cổng 8000 để theo dõi các metric
start_http_server(8000)

# Vòng lặp vô hạn để kiểm tra kết nối của MySQL và cập nhật metric
while True:
    check_mysql_connection()
  
