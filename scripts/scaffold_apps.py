import os

# Root path (relative to this script)
base_path = os.path.join("..", "apps")

apps = [
    "loyalty_engine",
    "franchise_finance",
    "franchise_crm",
    "ecommerce_router",
    "hr_payroll",
    "franchise_admin_portal",
    "saas_platform_admin"
]

subfolders = ["doctype", "api", "hooks", "utils", "tests"]

for app in apps:
    app_path = os.path.join(base_path, app)
    os.makedirs(app_path, exist_ok=True)

    for sub in subfolders:
        os.makedirs(os.path.join(app_path, sub), exist_ok=True)

    # Create an __init__.py to make it a Python package
    with open(os.path.join(app_path, "__init__.py"), "w") as f:
        f.write(f"\"\"\"{app} module\"\"\"\n")

print("✅ All custom Bizaiv apps scaffolded successfully.")
