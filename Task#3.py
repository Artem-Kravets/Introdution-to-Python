def html_decorator(arg1, arg2):
    def inner_function(function):
        def wrapper(text):
            my_list = []
            for i in range(arg2):
                my_list.append(f"<{arg1}> {function(text)} {i + 1} </{arg1}>")
            return my_list
        return wrapper

    return inner_function


@html_decorator("li", 3)
def html_element(text):
    my_text = text.replace("@", " ").replace("#", " ").replace("%", " ").replace("&", " ") \
        .replace("$", " ").replace("^", " ").replace("*", " ").replace("_", " ") \
        .replace("<", "").replace(">", "").replace("/", "")
    return my_text.capitalize()


print(html_element('>list_item<'))

