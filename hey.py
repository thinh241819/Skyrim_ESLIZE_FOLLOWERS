import os

# Ask for users path and relevant information to do the work
print("Please enter your file path: ")
file_path = input()
print("Please enter your previous form-ID: ")
prev_formID = str(input())
print("Please enter your new form-ID: ")
new_formID = str(input())

nif_path = os.path.join(file_path, "meshes\Actors\Character\FaceGenData\FaceGeom\amelia_rose_v3.esp")

string = b""
Flag = 0
with open(os.path.join(file_path, prev_formID + ".nif"), 'rb+') as file:
    # Read the content of the file character by character
    # Use this to initialize the loop
    data = string = file.read(1)

    # Loop till the end of file is reached
    while data:
        # Advance the loop
        data = file.read(1)
        # Check if we have an 'n' to denote a file extension
        if data == b".":
            # Read the next 3 bytes to check it's extension
            data = string = file.read(3)
            # If the extension is "dds", we are on the right track
            if string == b"dds":
                Flag = 1
                file.seek(file.tell() - 12)
                data = string = file.read(12)
                # Check if the string match the previous formID provided by user
                if string == (prev_formID + ".dds").encode():
                    print(string)
                    # So apparently, when writing in python, we are actually overwriting the old data, then add more data to it
                    # Move the file pointer back to the first '0' where we need to overwrite
                    file.seek(file.tell() - 12)
                    # Overwrite it
                    file.write(new_formID.encode())


    if Flag:
        print("Found and replaced")
    else:
        print("not found!")
