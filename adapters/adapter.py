class DBAdapter(object):
    def get_report(self, report_id, **filters):
        raise NotImplemented()
    
    def create_report(self, data_dict):
        raise NotImplemented()
