# find which default args were used

import inspect as ins

def decorate(func):
    all_args = ins.getfullargspec(func).args
    quantity_all_args = len(all_args)
    if ins.getfullargspec(func).defaults != None:
        quantity_default_args = len(ins.getfullargspec(func).defaults)
    else:
        quantity_default_args = 0

    quantity_non_default_args = quantity_all_args - quantity_default_args

    signature = ins.signature(func)

    default_args_dict = {
        k: v.default
        for k, v in signature.parameters.items()
        if v.default is not ins.Parameter.empty
    }

    def wrapper(*args, **kwargs):
        quantity_used_args = len(args) + len(kwargs)

        quantity_used_default_args = quantity_default_args - (quantity_all_args - quantity_used_args) - len(kwargs)

        all_args_dict = ins.getcallargs(func, *args, **kwargs)

        used_default_args = []

        for key in default_args_dict.keys():
            if default_args_dict.get(key) != all_args_dict.get(key):
                used_default_args.append(key)

        for key in default_args_dict.keys():
            if key in kwargs and key not in used_default_args:
                used_default_args.append(key)

        for key in default_args_dict.keys():
            if key in all_args[
                      quantity_non_default_args: quantity_non_default_args + quantity_used_default_args] and key not in used_default_args:
                used_default_args.append(key)
        return func(*args, **kwargs, default_params=tuple(used_default_args))
    return wrapper


@decorate
def function2(a, b, c=1, *args, k1=2, k2=2, **kwargs):
    q=1
    print(kwargs["default_params"])


function2(1, 2)
function2(1, 2, 3)
function2(1, 2, 3, 4)
function2(1, 2, k1=0, qq=5)
function2(1, 2, 3, 4, k2=0, qq=5)
