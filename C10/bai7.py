x=str(input("nhập chuỗi s: "))
y=str(input("nhập chuỗi con s_sub: "))
z=str(input("nhập chuỗi tìm s_find: "))
t=str(input("nhập chuỗi thay thế s_replace: "))
print("chuỗi sau khi bỏ khoảng trắng ở đầu và cuối chuỗi: ",x)
print("số lần s_sub xuất hiện trong s: ",x.find(y))
print("chuỗi s sau khi tìm kiếm và thay thế: ",x.replace(z,t))