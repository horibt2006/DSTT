#Võ Ngọc Duy - 2474802010071
danhsach1 = [1, 3]
danhsach2 = [5, 7]
danhsach = danhsach1 + danhsach2
print("danh sach la:", danhsach) 
danhsach_gapdoi = 2 * danhsach
print("danh sach gap doi la: ", danhsach_gapdoi)  
print(danhsach * 2)  
mon_hoc = ["ToanCC", "DSTT", "ToanRR", "LaptrinhCB"]
thu_tu = [2, 3, 4, 1]
diem_so = [10, 9, 8, 7]
anh_xa = zip(thu_tu, mon_hoc, diem_so)
anh_xa = list(anh_xa) 
print("anh xa la: ", anh_xa)
tap_hop = set(tuple(row) for row in anh_xa)  
print("tap hop: ", tap_hop)
lay_TT, lay_monhoc, lay_diem = zip(*anh_xa)
print("lay mon hoc: ", lay_monhoc)  
import itertools
tap_sinh = list(itertools.chain(range(4), range(5, 10), range(15, 20)))
print("tap sinh: ", tap_sinh)
result = list(zip(range(4), range(7, 12), reversed(range(11))))
print("ket qua la: ", result)
