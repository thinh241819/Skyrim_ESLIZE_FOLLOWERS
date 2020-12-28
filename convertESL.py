import os

def convert_esl(new_formID, file_path):
    prev_formID = ""
    # Look in the directory for files with ".esp" extension
    # With the help of this guide
    # https://stackoverflow.com/questions/3964681/find-all-files-in-a-directory-with-extension-txt-in-python
    for file in os.listdir(file_path):
        if file.endswith(".esp"):
            esp_file = file

    # Look in the directory for ".nif" file to quickly determine the Previous form ID
    for file in os.listdir(os.path.join(file_path, "meshes\Actors\Character\FaceGenData\FaceGeom", esp_file)):
        if file.endswith(".nif"):
            prev_formID = file.replace('.nif', '')
        if file.endswith(".NIF"):
            prev_formID = file.replace('.NIF', '')

    # Create file path for the necessary files
    old_nif_path = os.path.join(file_path, "meshes\Actors\Character\FaceGenData\FaceGeom", esp_file, prev_formID + ".nif")
    old_tga_path = os.path.join(file_path, "textures\Actors\Character\FaceGenData\FaceTint", esp_file, prev_formID + ".tga")
    old_dds_path = os.path.join(file_path, "textures\Actors\Character\FaceGenData\FaceTint", esp_file, prev_formID + ".dds")

    new_nif_path = os.path.join(file_path, "meshes\Actors\Character\FaceGenData\FaceGeom", esp_file, new_formID + ".nif")
    new_tga_path = os.path.join(file_path, "textures\Actors\Character\FaceGenData\FaceTint", esp_file, new_formID + ".tga")
    new_dds_path = os.path.join(file_path, "textures\Actors\Character\FaceGenData\FaceTint", esp_file, new_formID + ".dds")

    # Check if the file exists and rename the files
    # With the help of this guide
    # https://www.tutorialspoint.com/python/os_rename.htm
    if os.path.exists(old_dds_path):
        os.rename(old_dds_path, new_dds_path)
    if os.path.exists(old_tga_path):
        os.rename(old_tga_path, new_tga_path)
    if os.path.exists(old_nif_path):
        os.rename(old_nif_path, new_nif_path)

    # *************** START_SECTION 1 ***************
    # Open and write characters to "nif" binary files with normal characters
    # With the help of this guide
    # https://www.geeksforgeeks.org/python-program-to-modify-the-content-of-a-binary-file/
    # https://www.tutorialsteacher.com/python/python-read-write-file
    string = b""
    Flag = 0
    with open(new_nif_path, 'rb+') as file:
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
# XXXXXXXXXXXXXXX START_SECTION 1 XXXXXXXXXXXXXXX
