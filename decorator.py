# def decorator_func(func):
# 	def printer(name):
# 		print("első")
# 		print(func(name))
# 		print("harmadik")
# 	return printer

# @decorator_func
# def function_to_decorate(text):
# 	return "duma " + text

# function_to_decorate("Kati")

def commentaire(func):
    def func_wrapper():
        print("Doing stuff!")
        return func()
    return func_wrapper

def commentaire2(func):
	print("ez")
	return func

@commentaire
def create_hello_world():
    return "Hello World!"

@commentaire
def print_hello_world():
    #print(input)
    print(create_hello_world())

print_hello_world()


