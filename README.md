# Bizaiv ERP SaaS

This repository contains the scaffold for the Bizaiv ERP SaaS platform based on ERPNext v15.  The project is structured for development with Docker Desktop on Windows and Visual Studio Code.

## Project Structure

```
apps/
  loyalty_engine/
  franchise_finance/
  franchise_crm/
  ecommerce_router/
  hr_payroll/
  franchise_admin_portal/
  saas_platform_admin/

deployment/
  docker-compose.yml
  backup_scripts/

scripts/
  scaffold_apps.py

monitoring/
  prometheus/
  grafana/

sites/               # ERPNext site data volume
logs/                # ERPNext logs volume
```

The directories `sites/` and `logs/` are required for ERPNext v15 containers to store data and logs.

## Local Development

1. **Prerequisites**
   - Docker Desktop with WSL2
   - VSCode
   - Python 3.10+

2. **Start the stack**

   ```powershell
   cd deployment
   docker-compose up -d
   ```

   ERPNext will be available at [http://localhost:8080](http://localhost:8080).

3. **Create a site** (if not automatically created)

   ```powershell
   docker-compose run --rm create-site
   ```

   Default admin password is `admin`.

4. **Load fixtures**

   ```powershell
   docker exec -it <backend-container-id> bash
   bench --site bizaiv.local import-fixtures
   ```

5. **Stop the stack**

   ```powershell
   docker-compose down
   ```

For convenience, `scripts/scaffold_apps.py` can be used to regenerate the app folder structure if required.

