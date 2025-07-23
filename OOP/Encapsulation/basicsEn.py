# hides internal data of obj details and restricts direct access to that
# protect internal state, provide controlled access & improve code modularity
# accessible by getter setter methods
# public --> self.var_name
# protected --> self._varName
# private -->self.__varName


# ---getter setter method
class student:
    def set_val(self,name,marks):
        self.__name=name
        self.__marks=marks

    def get_marks(self):
        return self.__marks
    
    def get_name(self):
        return self.__name
    
s=student()
s.set_val("krishna",89)
print("name : ",s.get_name())
print("marks : ",s.get_marks())
