#This module is named annotation_helpers
#Ankekat1000
#March 2019

def Textfiles_from_df(df_ID_message):
    for index, row in df_ID_message.iterrows():
        # write a text file.
        # Define file name - should be the comment-ID:
        filename = str(row["Comment_ID"])

        # Define file content - should be the comment message:
        text_to_be_written = str(row["message"])

        file_object = open(filename + ".txt", "w")
        file_object.write(str(text_to_be_written))
        # close file, don't forget!
        file_object.close()