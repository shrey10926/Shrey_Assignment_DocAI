import os
from paddleocr import TableCellsDetection

img_name = os.path.join("Images", "Table.JPG")
models = ["RT-DETR-L_wireless_table_cell_det", "RT-DETR-L_wired_table_cell_det"]

def count_cells(img_name, model_name):
    try:
        if not os.path.exists(img_name):
            raise FileNotFoundError(f"Image not found: {img_name}")

        model = TableCellsDetection(model_name = model_name, device = "cpu", precision = "fp32")
        output = model.predict(img_name, threshold = 0.81, batch_size = 1)

        for res in output:
            res.print(json_format = False)
            res.save_to_img("./output/", )
            res.save_to_json(f"./output/res_{img_name}.json")

        print(f"Number of cells are:\n{len(output[0]['boxes'])}")

    except Exception as e:
        print(f"Error processing {img_name}: {str(e)}")
        return None

result = count_cells(img_name, models[1])