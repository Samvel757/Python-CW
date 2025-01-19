class MainClass:
    def init(self, text=""):
        self.text = text

    def set_text(self, new_text):
        self.text = new_text

    def display_text(self):
        print(f"Текст в MainClass: {self.text}")


class SubClass(MainClass):
    def set_text(self, new_text):
        modified_text = f"Модифицированный текст: {new_text}"
        super().set_text(modified_text)


if __name__ == "__main__":
    
    main_obj = MainClass()
    main_obj.set_text("Это текст для MainClass")
    main_obj.display_text()

    
    sub_obj = SubClass()
    sub_obj.set_text("Это текст для SubClass")
    sub_obj.display_text()