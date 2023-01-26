class Element:
    _name: str
    _year: int

    def __init__(self,  name: str = None, year: int = 1970) -> None:
        self._name = name
        self._year = year
        if year < 1970 & year > 2023:
            year = 1970

    def set_name(self, value):
        if value is str:
            self._name = value
        else:
            print("nieprawidłowa wartość")

    def set_year(self, value):
        if value is int:
            if value < 1970 & value > 2023:
                self._year = value
            else:
                print("nie z przedzialu 1970 2023")
        else:
            print("nieprawidlowa wartosc")

    def get_name(self):
        return self._name

    def get_year(self):
        return self._year

    def __str__(self):
        return f'Nazwa %s. Utworzony %s' %(self._name, self._year)




class File(Element):
    _size: int

    def __init__(self, name: str, year, size: int = 0) -> None:
        super(Element, self).__init__(name, year)
        self._size = size
        if size < 0:
            size = 0

    def set_size(self, value):
        if value is int:
            if value < 0:
                self._size = value

    def get_size(self):
        return self._size















