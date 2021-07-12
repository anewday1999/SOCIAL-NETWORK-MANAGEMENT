# SOCIAL-NETWORK-MANAGEMENT.
## I.	Youtube API:
### 1.	Credentials:
-	API key: For public request. 
-	Oauth: For private request.  
Public, private phụ thuộc vào loại thông tin cần truy xuất. (Ví dụ, lấy danh sách các video của một kênh, chỉ cần sử dụng apikey. Để lấy danh sách subcribers thì phải sử dụng Oauth2).  
API key và Oauth được tạo trên google console -> APIs and services.  
![image](files/Users/jzhang/Desktop/Isolated.png)
### 2.	Các truy xuất có thể thực hiện:  
-	Channels:  
+Số lượng video  
+Số lượng subscribers  
+… (Các thông tin public khác có thể nhìn thấy đều có thể truy xuất).  
> Ứng dụng: Theo dõi trạng thái hiện tại của kênh.  
  
-	Comments:   
+Trả về danh sách các bình luận.  
+Trả lời bình luận cho một comment.  
+Đánh dấu spam.  
> Ứng dụng: Direct marketing.

-	Membership:  
Youtube hiện tại có chức năng người ủng hộ.  
+Xem danh sách các memberships.  

-	Membershipslevel:
Người ủng hộ sẽ có các level khác nhau, tuỳ số tiền mà họ đóng góp.  
+Xem danh sách memberships và level.  

-	Playlists:

-	Search:
Tìm kiếm các nội dung theo: location(location radius), videoCaption,  videoType,…

-	Subscriptions:
+Xem danh sách những người theo dõi.
+Xem danh sách các kênh đã theo giỏi của người dùng chỉ định
>Ứng dụng: Direct marketing, ví dụ lấy danh sách của người đã theo dõi kênh của mình và các kênh họ đang theo dõi, thực hiện quảng cáo kênh trên các kênh đó để tăng view và subscribers.

-	Likes: Không thể truy xuất danh sách người đã thích vì chính sách quyền riêng tư của youtube.
### 3. Thực hiện:
- Chi tiết các truy vấn và code: https://developers.google.com/youtube/v3/docs/subscriptions/list.  
- Demo: Python code.  
- [https://github.com/anewday1999/SOCIAL-NETWORK-MANAGEMENT./blob/main/oauth_example.py][PlGh]  



