class Print:
    def __init__(self) -> None:
        pass

    def replace_error(self, text: str) -> str:
        return text.replace("ERROR", "SERGII")

    def pretty_print(self, text: str) -> str:
        """
        Function adds sufix Pretty to the end of the line

        Returns prettified string
        """
        text += " Pretty"
        # text = text.replace("ERROR", "SERGII")

        return text


# pretty_print = Print()

# original_msg = "ERROR test"
# dest_msg = pretty_print.replace_error(original_msg)
# dest_msg = pretty_print.pretty_print(dest_msg)
# print(dest_msg)