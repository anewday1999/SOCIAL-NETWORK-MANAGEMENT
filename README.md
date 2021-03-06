# SOCIAL-NETWORK-MANAGEMENT.
## I.	Youtube API:
### 1.	Credentials:
-	API key: For public request. 
-	Oauth: For private request.  
Public, private phụ thuộc vào loại thông tin cần truy xuất. (Ví dụ, lấy danh sách các video của một kênh, chỉ cần sử dụng apikey. Để lấy danh sách subcribers thì phải sử dụng Oauth2).  
API key và Oauth được tạo trên google console -> APIs and services.  
![image](https://github.com/anewday1999/SOCIAL-NETWORK-MANAGEMENT./blob/main/youtubeAPI/Screenshot%202021-07-12%20at%2017.49.04.png)
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
>Ứng dụng: Direct marketing, ví dụ lấy danh sách của người đã theo dõi kênh của mình và các kênh họ đang theo dõi, thực hiện quảng cáo kênh trên các kênh đó để tăng views và subscribers.

-	Likes: Không thể truy xuất danh sách người đã thích vì chính sách quyền riêng tư của youtube.
### 3. Thực hiện:
- Chi tiết các truy vấn và code: https://developers.google.com/youtube/v3/docs/subscriptions/list.  
- Demo: Python code.  
  
[1. Ví dụ về nhận danh sách subcribers với Oauth2](https://github.com/anewday1999/SOCIAL-NETWORK-MANAGEMENT./blob/main/youtubeAPI/oauth_example.py)  
Result: ![image](https://github.com/anewday1999/SOCIAL-NETWORK-MANAGEMENT./blob/main/youtubeAPI/Screenshot%202021-07-12%20at%2018.04.14.png). 
> Yêu cầu client_secrets_file, được tạo và tải về từ apis and services (google cloud platform).  
  
[2. Ví dụ về nhận thông tin kênh với api_key](https://github.com/anewday1999/SOCIAL-NETWORK-MANAGEMENT./blob/main/youtubeAPI/apikey.py)  
Result: ![image](https://github.com/anewday1999/SOCIAL-NETWORK-MANAGEMENT./blob/main/youtubeAPI/Screenshot%202021-07-12%20at%2018.05.26.png).  
> Yêu cầu api_key, được tạo từ apis and services (google cloud platform).  
  
## II.	Facebook API:
### 1. Credentials:
- Create an application : https://developers.facebook.com/.  
- Use appid & appsecret to request an access token.  
- Các bước access: Tạo app, sử dụng id và secret để nhận access token user, sử dụng access token user và id page để nhận access token page, nhận id page, send request.  
### 2. Truy xuất:
- Không thể truy xuất số người theo dõi hoặc like page dưới bất kì hình thức nào.  
- Test truy vấn: https://developers.facebook.com/tools/explorer/?method=GET&path=107310934648059%2Fsubscribers&version=v11.0.  
- Danh sách các truy vấn có thể thực hiện: https://developers.facebook.com/docs/graph-api/reference/user/  
- Không có sẵn thư viện.  
### 3.  Thực hiện:
[Simple class request](https://github.com/anewday1999/SOCIAL-NETWORK-MANAGEMENT/blob/main/facebookAPI/fb_api.py)  
### 4. Vấn đề:
Để nhận access token cho user: 1. người dùng tự lấy, 2. tạo server api để nhận tự động.  

