#termary operation

is_frined = True
can_message = "message allowed" if is_frined else "not allowed to message"

print(can_message)

#short circuiting

is_friend  = True
is_user = True

if is_friend and is_user:
  print('best friend forever')


