def main():
    file_name=input("File name: ")
    if len(file_name.split(".")) == 2:
        print(file_type(file_name))
    else:
        print("application/octet-stream")


def file_type(full):
    parts=full.lower().split(".")
    match parts[1].strip():
        case "gif":
            return "image/gif"
        case "jpg":
            return "image/jpeg"
        case "jpeg":
            return "image/jpeg"
        case "png":
            return "image/png"
        case "pdf":
            return "application/pdf"
        case "txt":
            return "text/plain"
        case "zip":
            return "application/zip"
        case _:
            return "application/octet-stream"
    

if __name__ == "__main__":
    main()