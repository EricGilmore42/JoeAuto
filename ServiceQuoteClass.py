class ServiceQuote:

    def __init__(self,pcharge,lcharge):
        self.__part_charges = pcharge 
        self.__labor_charges = lcharge

    def set_pcharge(self,pcharge):
        self.__part_charges = pcharge
    def set_lcharge(self,lcharge):
        self.__labor_charges = lcharge
    def set_tax(self):
        self.__tax = 1.08

    def get_pcharge(self):
        return self.__part_charges
    def get_lcharge(self):
        return self.__labor_charges

    def get_total_charges(self): 
        return ((self.__part_charges + self.__labor_charges)*(1.08))