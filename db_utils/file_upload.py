generated_path = []
try:
    with open(local_path, 'rb') as data:
        if data:
            data.seek(0, 2)
            data_file_size = data.tell()
            data.seek(0, 0)
            if not data == 0:
                # upload file
                data_location = ref_data_filestore.upload_fileobj(data, file_path, data_file_size, file_name,  content_type="text/sql")
                logger.debug("uploaded_file_path --> " + data_location)
                generated_path.append(data_location)
            else:
                raise HTTPException(HTTP_422_UNPROCESSABLE_ENTITY, detail="uploading empty file not allowed")

except Exception as e:
    raise HTTPException(HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))   