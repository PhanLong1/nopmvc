import sinhvien_db

class SinhvienController(object):
    #Phương thức khởi tạo
    def __init__(self, model, view):
        self.model = model
        self.view = view

    #Phương thức hiển thị tất cả dữ liệu của bảng sinhvien
    def show_all_sinhvien(self):
        items = self.model.get_all_sinhvien()
        self.view.display_all_sinhvien(items)

    #Phương thức insert
    def them_sinhvien(self, names):
        resultID = self.model.them_sinhvien(names)
        self.view.ket_qua_insert(resultID)
    #Phương thức update
    def update_sinhvien(self, names, idsv):
        self.model.update_sinhvien(names, idsv)
        self.view.ket_qua_update()

    #Phương thức delete
    def delete_sinhvien(self, idsv):
        self.model.delete_sinhvien(idsv)
        self.view.ket_qua_delete()