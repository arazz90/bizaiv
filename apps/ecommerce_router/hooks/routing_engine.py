import frappe

@frappe.whitelist()
def assign_nearest_outlet(order_id, delivery_pincode):
    warehouses = frappe.get_all("Warehouse", filters={"pincode": delivery_pincode}, limit=1)
    if not warehouses:
        frappe.throw("No warehouse found for given pincode")

    assigned_warehouse = warehouses[0].name
    order = frappe.get_doc("Online Order", order_id)
    order.assigned_warehouse = assigned_warehouse
    order.save()

    return assigned_warehouse
