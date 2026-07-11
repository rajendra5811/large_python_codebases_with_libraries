class MyCustomNameError(NameError):
    pass
print(MyCustomNameError)
print(MyCustomNameError.mro())
try:
  raise MyCustomNameError("My Custom error")
  print("good")
except:
   print("My Custom made error works")
class preconditionError(ValueError):
   pass
class SSLError(OSError):
   pass
class EmptyDataSetError(RuntimeError):
   pass
class BadLoginError(KeyError):
   pass
#raise BadloginError("missing password")
#raise NameError("Why hello!")
"""try:
    raise BadLoginError("No username :(")
except BadLoginError:  # Respond only to `BadLoginError`s, not other types of `KeyError`s.
    pass"""
#raise	A keyword to raise an Exception subclass or an instance of an Exception subclass.