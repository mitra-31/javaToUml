import token
import PlantumlTxt

sourceCode = []  # Appending the source code to the sourceCode variable.


print("Enter/Paste your code.Ctrl+d (or) Ctrl+Z ( windows ) to save it.")    # when we hit Ctrl+z it will invoke except and it stops taking input from user. 
while True:
  try:
    sourceCode.append(input(">> ").strip())
  except EOFError:
    break


sourceCode = "\n".join(sourceCode)

PlantumlTxt.writeUml(sourceCode).run()





#print(dir(sourceCode))