import frappe

# def print_data():
#     print(frappe.utils.getdate())

def before_save(doc, method=None):
    if doc.variant_of:
        for att in doc.attributes:
            if att.attribute.lower() == "width":
                doc.width = float(att.attribute_value)
            elif att.attribute.lower() == "height":
                doc.height = float(att.attribute_value)
            elif "yield" == att.attribute.lower():
                doc.item_yield = float(att.attribute_value)

        for i in doc.uoms:
            if i.formula:
                i.conversion_factor = eval(i.formula)