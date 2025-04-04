def doc_du_lieu(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        ma_tran = [list(map(int, line.split())) for line in file.readlines()]
    return ma_tran

def gts1(ma_tran):
    n = len(ma_tran)  # Số lượng thành phố
    da_tham = [False] * n  # Mảng đánh dấu thành phố đã được thăm
    lo_trinh = [0]  # Bắt đầu từ thành phố đầu tiên
    da_tham[0] = True  # Đánh dấu thành phố đầu tiên đã thăm
    tong_chi_phi = 0  # Tổng chi phí ban đầu
    
    thanh_pho_hien_tai = 0  # Thành phố hiện tại bắt đầu từ thành phố 0
    while len(lo_trinh) < n:
        chi_phi_min = float('inf')  # Chi phí nhỏ nhất ban đầu
        thanh_pho_tiep_theo = -1  # Thành phố tiếp theo (chưa xác định)
        
        # Tìm thành phố chưa thăm và có chi phí di chuyển thấp nhất
        for thanh_pho in range(n):
            if not da_tham[thanh_pho] and ma_tran[thanh_pho_hien_tai][thanh_pho] < chi_phi_min:
                chi_phi_min = ma_tran[thanh_pho_hien_tai][thanh_pho]
                thanh_pho_tiep_theo = thanh_pho
        
        # Thêm thành phố tiếp theo vào lộ trình và đánh dấu đã thăm
        lo_trinh.append(thanh_pho_tiep_theo)
        da_tham[thanh_pho_tiep_theo] = True
        tong_chi_phi += chi_phi_min  # Cộng thêm chi phí vào tổng chi phí
        thanh_pho_hien_tai = thanh_pho_tiep_theo  # Cập nhật thành phố hiện tại
    
    # Quay lại thành phố xuất phát
    tong_chi_phi += ma_tran[thanh_pho_hien_tai][lo_trinh[0]]
    lo_trinh.append(lo_trinh[0])  # Thêm thành phố xuất phát vào cuối lộ trình
    
    return lo_trinh, tong_chi_phi

def ghi_ket_qua(file_path, lo_trinh, tong_chi_phi):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write("Kết quả lộ trình của bài toán TSP sử dụng thuật toán GTS1:\n")
        file.write("Lộ trình: " + " -> ".join(map(str, lo_trinh)) + "\n")
        file.write(f"Tổng chi phí: {tong_chi_phi}\n")

# Đọc dữ liệu từ file input.txt
file_vao = 'input.txt'
ma_tran = doc_du_lieu(file_vao)

# Áp dụng thuật toán GTS1
lo_trinh, tong_chi_phi = gts1(ma_tran)

# Ghi kết quả vào file output.txt
file_ra = 'output.txt'
ghi_ket_qua(file_ra, lo_trinh, tong_chi_phi)
