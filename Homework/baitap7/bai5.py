# Bài 5. Datetime
# Trong Python, module datetime hỗ trợ các xử lý trên ngày tháng.
# Ví dụ, để lấy thời gian hiện tại trong hệ thống, ta viết:
# from datetime import datetime
# now = datetime.now()
# print(now)

# Biến now là một đối tượng datetime, lưu thông tin về một thời điểm cụ thể. Để thay đổi định dạng in ra mặc định, ta viết định dạng mong muốn vào phương thức strftime() có sẵn trong module datetime.
#   print(now.strftime('%Y/%m/%d'))
#   print(now.strftime('%H:%M:%S %Y-%m-%d'))

# Hãy chạy các đoạn code trên để xem kết quả, sau đó chỉnh sửa để chương trình in ra nội dung sau, tương ứng với ngày hiện tại trong hệ thống:
#   Today is 21/07/2021
#   Time right now: 13:36:10

from datetime import datetime

now = datetime.now()

print("Today is:",now.strftime('%d/%m/%Y'))
print("Time right now:",now.strftime('%H:%M:%S'))

