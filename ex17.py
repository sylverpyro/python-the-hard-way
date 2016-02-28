from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("Copying from {} to {}".format(from_file, to_file))

# we could do these two on one line.  How?
in_file = open(from_file)
indata = in_file.read()
# In one line, it would be
# indata = open(from_file).read()
## But this will cause the file handle to stay open beyound it's
## intended lifetime as it won't get cleaned until later in program
## execution.  Fine for single files, but in a loop or larger program
## potentially dangerous

print("The input file is {:d} bytes long".format(len(indata))) 

print("Does the output file exist? {}".format(exists(to_file)))
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()
