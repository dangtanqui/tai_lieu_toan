#!/usr/bin/env python3
"""Move files from nam_X/hkY structure to nhom_* structure."""
import os
import shutil
from pathlib import Path

BASE = Path(__file__).parent

# Mapping: (source_path, dest_folder, dest_filename)
# dest_filename None = keep original name
MOVES = [
    # Nhóm 1 - Đại số
    ("nam_1/hk1/dai_so_dai_cuong_(co_so)/ly_thuyet.tex", "nhom_1_dai_so_logic/dai_so_dai_cuong_co_so", "ly_thuyet.tex"),
    ("nam_1/hk1/dai_so_so_cap/ly_thuyet.tex", "nhom_1_dai_so_logic/dai_so_so_cap", "ly_thuyet.tex"),
    ("nam_1/hk1/toan_cao_cap_1/ly_thuyet.tex", "nhom_1_dai_so_logic/dai_so_tuyen_tinh", "ly_thuyet.tex"),
    ("nam_1/hk2/dai_so_tuyen_tinh_nang_cao/ly_thuyet.tex", "nhom_1_dai_so_logic/dai_so_tuyen_tinh", "ly_thuyet_nang_cao.tex"),
    ("nam_2/hk2/dai_so_tuyen_tinh_nang_cao_2/ly_thuyet.tex", "nhom_1_dai_so_logic/dai_so_tuyen_tinh", "ly_thuyet_nang_cao_2.tex"),
    ("nam_3/hk1/dai_so_dai_cuong/ly_thuyet.tex", "nhom_1_dai_so_logic/dai_so_dai_cuong_vanh_modun", "ly_thuyet.tex"),
    ("nam_4/hk1/ly_thuyet_nhom/ly_thuyet.tex", "nhom_1_dai_so_logic/ly_thuyet_nhom", "ly_thuyet.tex"),
    # Nhóm 2 - Giải tích
    ("nam_1/hk1/giai_tich_1/ly_thuyet.tex", "nhom_2_giai_tich/giai_tich_1", "ly_thuyet.tex"),
    ("nam_1/hk2/giai_tich_2/ly_thuyet.tex", "nhom_2_giai_tich/giai_tich_2", "ly_thuyet.tex"),
    ("nam_1/hk2/toan_cao_cap_2/ly_thuyet.tex", "nhom_2_giai_tich/giai_tich_2", "ly_thuyet_toan_cao_cap_2.tex"),
    ("nam_2/hk1/giai_tich_3/ly_thuyet.tex", "nhom_2_giai_tich/giai_tich_3", "ly_thuyet.tex"),
    ("nam_2/hk1/co_so_giai_tich/ly_thuyet.tex", "nhom_2_giai_tich/co_so_giai_tich", "ly_thuyet.tex"),
    ("nam_3/hk2/ly_thuyet_do_do_va_tich_phan/ly_thuyet.tex", "nhom_2_giai_tich/ly_thuyet_do_do_va_tich_phan", "ly_thuyet.tex"),
    ("nam_3/hk2/giai_tich_phuc/ly_thuyet.tex", "nhom_2_giai_tich/giai_tich_phuc", "ly_thuyet.tex"),
    ("nam_3/hk1/giai_tich_ham/ly_thuyet.tex", "nhom_2_giai_tich/giai_tich_ham", "ly_thuyet.tex"),
    ("nam_4/hk1/giai_tich_ham_nang_cao/ly_thuyet.tex", "nhom_2_giai_tich/giai_tich_ham", "ly_thuyet_nang_cao.tex"),
    # Nhóm 3 - Hình học
    ("nam_1/hk2/hinh_hoc_giai_tich/ly_thuyet.tex", "nhom_3_hinh_hoc/hinh_hoc_giai_tich", "ly_thuyet.tex"),
    ("nam_3/hk1/hinh_hoc_vi_phan/ly_thuyet.tex", "nhom_3_hinh_hoc/hinh_hoc_vi_phan", "ly_thuyet.tex"),
    ("nam_4/hk1/hinh_hoc_dai_so/ly_thuyet.tex", "nhom_3_hinh_hoc/hinh_hoc_dai_so", "ly_thuyet.tex"),
    # Nhóm 4 - Phương trình
    ("nam_2/hk1/phuong_trinh_vi_phan/ly_thuyet.tex", "nhom_4_phuong_trinh/phuong_trinh_vi_phan", "ly_thuyet.tex"),
    ("nam_2/hk2/phuong_trinh_dao_ham_rieng/ly_thuyet.tex", "nhom_4_phuong_trinh/phuong_trinh_dao_ham_rieng", "ly_thuyet.tex"),
    ("nam_3/hk2/phuong_trinh_dao_ham_rieng_nang_cao/ly_thuyet.tex", "nhom_4_phuong_trinh/phuong_trinh_dao_ham_rieng", "ly_thuyet_nang_cao.tex"),
    ("nam_4/hk1/phuong_trinh_vi_phan_nang_cao/ly_thuyet.tex", "nhom_9_khac/phuong_trinh_vi_phan_nang_cao", "ly_thuyet.tex"),
    # Nhóm 5 - Xác suất thống kê
    ("nam_2/hk1/xac_suat_1/ly_thuyet.tex", "nhom_5_xac_suat_thong_ke/xac_suat", "ly_thuyet.tex"),
    ("nam_2/hk2/xac_suat_2/ly_thuyet.tex", "nhom_5_xac_suat_thong_ke/thong_ke_toan", "ly_thuyet.tex"),
    ("nam_2/hk2/thong_ke_ung_dung/ly_thuyet.tex", "nhom_5_xac_suat_thong_ke/thong_ke_ung_dung", "ly_thuyet.tex"),
    ("nam_3/hk1/xac_suat_va_do_do/ly_thuyet.tex", "nhom_5_xac_suat_thong_ke/xac_suat_va_do_do", "ly_thuyet.tex"),
    ("nam_3/hk2/xac_suat_thong_ke_nang_cao/ly_thuyet.tex", "nhom_5_xac_suat_thong_ke/xac_suat_thong_ke_nang_cao", "ly_thuyet.tex"),
    ("nam_3/hk1/thong_ke_da_bien/ly_thuyet.tex", "nhom_5_xac_suat_thong_ke/thong_ke_da_bien", "ly_thuyet.tex"),
    ("nam_4/hk1/thong_ke_bayes/ly_thuyet.tex", "nhom_5_xac_suat_thong_ke/thong_ke_bayes", "ly_thuyet.tex"),
    ("nam_4/hk1/qua_trinh_ngau_nhien/ly_thuyet.tex", "nhom_5_xac_suat_thong_ke/qua_trinh_ngau_nhien", "ly_thuyet.tex"),
    # Nhóm 6 - Toán rời rạc
    ("nam_2/hk1/toan_roi_rac/ly_thuyet.tex", "nhom_6_toan_roi_rac_tin/toan_roi_rac", "ly_thuyet.tex"),
    ("nam_3/hk2/toan_roi_rac_nang_cao/ly_thuyet.tex", "nhom_6_toan_roi_rac_tin/toan_roi_rac_nang_cao", "ly_thuyet.tex"),
    ("nam_3/hk1/ly_thuyet_so/ly_thuyet.tex", "nhom_6_toan_roi_rac_tin/ly_thuyet_so", "ly_thuyet.tex"),
    ("nam_4/hk2/ly_thuyet_mat_ma/ly_thuyet.tex", "nhom_6_toan_roi_rac_tin/ly_thuyet_mat_ma", "ly_thuyet.tex"),
    ("nam_4/hk2/toan_hoc_tinh_toan/ly_thuyet.tex", "nhom_6_toan_roi_rac_tin/toan_hoc_tinh_toan", "ly_thuyet.tex"),
    # Nhóm 7 - Tối ưu
    ("nam_2/hk2/quy_hoach_tuyen_tinh/ly_thuyet.tex", "nhom_7_toi_uu_ung_dung/quy_hoach_tuyen_tinh", "ly_thuyet.tex"),
    ("nam_3/hk2/toi_uu/ly_thuyet.tex", "nhom_7_toi_uu_ung_dung/toi_uu_quy_hoach_phi_tuyen", "ly_thuyet.tex"),
    ("nam_2/hk2/phuong_phap_so/ly_thuyet.tex", "nhom_7_toi_uu_ung_dung/phuong_phap_so", "ly_thuyet.tex"),
    ("nam_4/hk2/phuong_phap_phan_tu_huu_han/ly_thuyet.tex", "nhom_7_toi_uu_ung_dung/phuong_phap_phan_tu_huu_han", "ly_thuyet.tex"),
    ("nam_4/hk2/dieu_khien_toi_uu/ly_thuyet.tex", "nhom_7_toi_uu_ung_dung/dieu_khien_toi_uu", "ly_thuyet.tex"),
    # Nhóm 8 - Toán kinh tế
    ("nam_1/hk1/toan_kinh_te_1/ly_thuyet.tex", "nhom_8_toan_kinh_te_tai_chinh/toan_kinh_te_1", "ly_thuyet.tex"),
    ("nam_1/hk2/toan_kinh_te_2/ly_thuyet.tex", "nhom_8_toan_kinh_te_tai_chinh/toan_kinh_te_2", "ly_thuyet.tex"),
    ("nam_2/hk1/toan_kinh_te_3/ly_thuyet.tex", "nhom_8_toan_kinh_te_tai_chinh/toan_kinh_te_3", "ly_thuyet.tex"),
    ("nam_3/hk1/kinh_te_luong/ly_thuyet.tex", "nhom_8_toan_kinh_te_tai_chinh/kinh_te_luong", "ly_thuyet.tex"),
    ("nam_3/hk1/toan_tai_chinh/ly_thuyet.tex", "nhom_8_toan_kinh_te_tai_chinh/toan_tai_chinh", "ly_thuyet.tex"),
    ("nam_4/hk2/toan_tai_chinh_dinh_luong/ly_thuyet.tex", "nhom_8_toan_kinh_te_tai_chinh/toan_tai_chinh_dinh_luong", "ly_thuyet.tex"),
    ("nam_3/hk2/toan_bao_hiem/ly_thuyet.tex", "nhom_8_toan_kinh_te_tai_chinh/toan_bao_hiem", "ly_thuyet.tex"),
    ("nam_3/hk2/toan_y_sinh/ly_thuyet.tex", "nhom_8_toan_kinh_te_tai_chinh/toan_y_sinh", "ly_thuyet.tex"),
    # Nhóm 9 - Khác
    ("nam_1/hk1/toan_cho_khoa_hoc_xa_hoi/ly_thuyet.tex", "nhom_9_khac/toan_cho_khoa_hoc_xa_hoi", "ly_thuyet.tex"),
    ("nam_3/hk1/topo/ly_thuyet.tex", "nhom_9_khac/topo", "ly_thuyet.tex"),
    ("nam_4/hk2/hoc_may/ly_thuyet.tex", "nhom_9_khac/hoc_may", "ly_thuyet.tex"),
]

def main():
    moved = 0
    for src_rel, dest_folder, dest_name in MOVES:
        src = BASE / src_rel
        dest_dir = BASE / dest_folder
        dest = dest_dir / dest_name
        if src.exists():
            dest_dir.mkdir(parents=True, exist_ok=True)
            shutil.move(str(src), str(dest))
            print(f"Moved: {src_rel} -> {dest_folder}/{dest_name}")
            moved += 1
        else:
            print(f"Skip (not found): {src_rel}")
    print(f"\nDone. Moved {moved} files.")

if __name__ == "__main__":
    main()
