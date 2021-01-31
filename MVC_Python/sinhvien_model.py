import sinhvien_db

class SinhVienModel(object):
    #Phương thức khởi tạo
    def __init__(self, database_server, username, password, database):
        self.connection, self.metadata, self.engine = sinhvien_db.ket_noi_den_csdl(database_server,
                                                                                   username,
                                                                                   password,
                                                                                   database)

    #Phương thức lấy dữ liệu
    def get_all_sinhvien(self):
        results = sinhvien_db.lay_tat_ca_du_lieu_bang_sinhvien(self.connection,
                                                               self.metadata,
                                                               self.engine)
        return results

    #Phương thức insert
    def them_sinhvien(self, names):
        resultID = sinhvien_db.them_sinhvien(self.connection,
                                             self.metadata,
                                             self.engine,
                                             names)
        return resultID

    #Phương thức update
    def update_sinhvien(self, names,idsv):
        resultID = sinhvien_db.update_sv(self.connection,
                                         self.metadata,
                                         self.engine,
                                         names, idsv)
        return resultID
    #Phương thức delete
    def delete_sinhvien(self, idsv):
        resultID = sinhvien_db.delete_sv(self.connection,
                                         self.metadata,
                                         self.engine, idsv)
        return resultID
