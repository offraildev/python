# calling external commands using the subprocess module.
import subprocess

# running this returns an output and completed process object
# the output is returned if run on terminal, not in an ide,
# else only the object is returned
subprocess.run("ls -la", shell=True)

# can run windows commands as well using the shell kwarg and windows 
# specific command

# shell=True enables to pass a whole command and not as a list 
# but only do it if you are passing the input, can be a security hazard

# if want to run without shell security hazard, pass command as a list
subprocess.run("ls -la".split())

# here the output is not being captured and goes wherever the stdout is 
# going, we need to catch that
p1 = subprocess.run("ls -la".split())

print(p1)

help(p1)

# in-order to capture the stdout, use subprocess.PIPE, get the output as bytes 
# to get in in str use decode 
p1 = subprocess.run("ls -la".split(), stdout=subprocess.PIPE)
print(p1.stdout)

p1 = subprocess.run("ls -la".split(), stdout=subprocess.PIPE)
print(p1.stdout.decode())

# direct the output to a file
# with open("output.txt", "r") as file:
#     p1 = subprocess.run("ls -la".split(), stdout=file)

# to capture error use the stderr kwarg to direct it to some file or PIPE (console)
p1 = subprocess.run("ls -la dne".split(), stderr=subprocess.PIPE)
print(p1.stderr.decode())

# python doesn't raise exception but on gives error code as non-zero 
# to raise exception use check=True
p1 = subprocess.run("ls -la dne".split(), stderr=subprocess.PIPE, check=True)
print(p1.stderr.decode())

# to ignore the error direct it to subprocess devnull
p1 = subprocess.run("ls -la dne".split(), stderr=subprocess.DEVNULL)
print(p1.stderr)

p1 = subprocess.run("ls -la", shell=True, stdout=subprocess.PIPE)
print(p1.stdout.decode())

# redirecting the output of subprocess to another
p1 = subprocess.run("cat subprocess_test.txt".split(), stdout=subprocess.PIPE)
p2 = subprocess.run("grep -n test".split(), stdout=subprocess.PIPE, input=p1.stdout)
print(p2.stdout.decode())