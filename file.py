from functools import wraps


def greeter(func):
    @wraps(func)
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        result = f"Aloha {result.title()}"
        return result

    return inner


def sums_of_str_elements_are_equal(func):
    @wraps(func)
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        left_number = 0
        right_number = 0
        numbers = result.split(" ")
        left_numbers = list(numbers[0])
        right_numbers = list(numbers[1])
        if left_numbers[0] == "-":
            left_sign = "-"
            left_numbers.remove("-")
        else:
            left_sign = ""
        if right_numbers[0] == "-":
            right_sign = "-"
            right_numbers.remove("-")
        else:
            right_sign = ""
        try:
            for i in left_numbers:
                left_number += int(i)
            for i in right_numbers:
                right_number += int(i)
        except ValueError as e:
            print("W podanym stringu muszą być tylko liczby")
        if left_sign == "-":
            left_number = -abs(left_number)
        if right_sign == "-":
            right_number = -abs(right_number)
        if left_number == right_number:
            result = f"{left_number} == {right_number}"
        else:
            result = f"{left_number} != {right_number}"
        return result

    return inner


def format_output(*required_keys):
    def outer_wrapper(func):
        def wrapper(*args, **kwargs):
            keys = required_keys
            func_dict = func(*args, **kwargs)
            func_keys = set(func_dict.keys())
            given_keys = set()
            keys_to_build = []
            for param in keys:
                if "__" in param:
                    given_keys.update(set(param.split("__")))
                    keys_to_build.append(param.split("__"))
                else:
                    given_keys.add(param)
                    keys_to_build.append(param)
            for key in given_keys:
                if key not in func_keys:
                    raise ValueError("Given arguments are not in function dict")
            result = dict()
            for key in keys_to_build:
                if type(key) == list:
                    long_key = "__".join(key)
                    response = []
                    for sub_key in key:
                        value = func_dict.get(sub_key)
                        if value == "":
                            response.append("Empty value")
                        else:
                            response.append(value)
                    result[long_key] = " ".join(response)
                else:
                    value = func_dict.get(key)
                    result[key] = func_dict.get(key)
                    if value == "":
                        result[key] = "Empty value"
                    else:
                        result[key] = value
            return result

        return wrapper

    return outer_wrapper


def add_method_to_instance(klass):
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args):
            result = func(*args)
            return result

        setattr(klass, func.__name__, wrapper)
        return func

    return decorator
