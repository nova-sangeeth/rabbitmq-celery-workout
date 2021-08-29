input_file_name = ""
output_file_name = ""


def edit_dump_file(input_file_name, output_file_name):
    with open(input_file_name, "r") as file:
        filedata = file.read()
    file_data = filedata.replace(
        "pg_catalog.setval('public.", "pg_catalog.setval('reference_data."
    )
    data = file_data.replace("public.", "reference_data.")
    with open(output_file_name, "w") as output:
        output.write(data)


edit_dump_file(input_file_name="", output_file_name="")
