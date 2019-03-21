câu 1 :Why should we use functions at all?
chúng ta dùng hàm vì nó có tính reusable khi chúng ta khai báo 1 function thì cta có thể dùng đi dùng lại nó ở các đoạn code khác
câu 2 :How to define/declare a function?
cú pháp:
    def <tên hàm>(tham số):
        câu lệnh
câu 3: How to call/use a function?
Chúng ta chỉ cần viết tên hàm mà cta đã định nghĩa nó vào trong chương trình cần dùng 
cú pháp :
    <tên hàm>(tham số cần gọi)
câu 4:What is return, why and how do we use it?
Câu lệnh return khiến hàm của bạn thoát ra và trả lại giá trị cho dùng.
Điểm nổi bật của chức năng nói chung là nhận đầu vào và trả lại một cái gì đó.
Câu lệnh return được sử dụng khi hàm sẵn sàng trả về giá trị cho người gọi
câu 5: Do we have to use return in every function?
chỉ dùng return khi thực sự cần phải trả lại 1 giá trị nào đó 
câu 6:What are function arguments/parameters, why and how we use it?
Hầu hết các hàm yêu tham sô: các đối số cung cấp cho sự khái quát hóa. Ví dụ: nếu chúng ta muốn tìm giá trị tuyệt đối của một số, 
chúng ta phải chỉ ra số đó là gì thì chương trình mới có thể hiểu được là cta muốn làm gì 
câu 7:How to use function from a different file other than our currently working file?
để dùng các hàm ở các tệp khác, ta sẽ phải truy suất tên tệp chứa 1 hoặc nhiều hàm cần dùng
*cú pháp:
    import <tên tệp chứa hàm>
    <tên tệp chứa hàm>.func()
hoặc
    from <tên tệp chứa hàm> import <hàm>
    <hàm>

