def Check(string):
  if string[-14:] == "@ashoka.edu.in" and string[0].isalpha():
    print("Valid Email")
  else:
    print("invalid")
email = "manish.yadav_ug22@ashoka.edu.in"
Check(email)
