# Python Dropbox uploader app PR101

# Importing dropbox
import dropbox

# transferdata class
class TransferData:

    # __init__ function
    def __init__(self, access_token):
        self.access_token = access_token
     
    # creating upload_file function for uploading files
    def upload_file(self, file_from, file_to): 
        dbx = dropbox.Dropbox(self.access_token) #Getting dbx token


        f = open(file_from, 'rb') # Reading boolean
        dbx.files_upload(f.read(), file_to) # Uploading files to dbx

def main():
    access_token = '#Enter your dropbox access token here'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path you want to transfer : -") # File path to transfer
    file_to = input("enter the full path to upload to dropbox:- ")  # This is the full path to upload the file to, including name that you wish the file to be called once uploaded.

    # API v2
    transferData.upload_file(file_from, file_to)
    print("file has been moved succesfully !!!")


# Calling function
main()


# By Satvik
