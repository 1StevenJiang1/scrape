import os
import PyPDF2


def nested_pdf_conversion(folder_path):
    """Recursively convert each pdf file in the folder to txt file of the same name.
    The folder either only contains pdf or it only contains folders
    """
    # If the first file under the current directory is not a folder, then we have reached
    # the leaves of the file tree. No need to recurse.
    files = os.listdir(folder_path)
    first_file = os.path.join(folder_path, files[0])
    if not os.path.isdir(first_file):
        output_folder = os.path.join(folder_path, 'txt_files')
        if output_folder not in os.listdir(folder_path):
            single_pdf_conversion(folder_path, output_folder)

    else:
        # If the first file under the current directory is a folder, then we recursively call the function
        # on each element of the list of files until we reach the second last bottom layer.
        for file in files:
            nested_pdf_conversion(os.path.join(folder_path, file))


def single_pdf_conversion(folder_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(folder_path, filename)
            text_content = pdf_to_text(pdf_path)

            # Generate output filename by replacing ".pdf" with ".txt"
            output_filename = os.path.splitext(filename)[0] + ".txt"
            output_path = os.path.join(output_folder, output_filename)

            with open(output_path, 'w', encoding='utf-8') as text_file:
                text_file.write(text_content)

            print(f"Conversion complete: {filename} -> {output_filename}")
def pdf_to_text(pdf_path):
    text = ""
    with open(pdf_path, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)

        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()

    return text


if __name__ == '__main__':
    # Replace 'input_folder' with the path to your folder containing PDFs
    src_dir = os.getcwd()
    src_dir = os.path.join(src_dir, 'Journals')
    # Replace 'output_folder' with the path where you want to save the text files
    print(src_dir)
    nested_pdf_conversion(src_dir)
