# T-R-Sports-Daily-data-update
update the preorder data
# Daily Data Script - Pre-sale Quantity Update

## Contents
- [Cin7 Data](#cin7-data)
- [Leafliving File from Shopify](#leafliving-file-from-shopify)
- [预售.csv File](#预售csv-file)

### Cin7 Data
```
# Navigate to Cin7 and login
open "https://www.cin7.com/"

# Set the date range and filters
# URL for direct access
open "https://go.cin7.com/Cloud/ShoppingCartAdmin/Orders/OrdersList.aspx?idWebSite=12877&idCustomerAppsLink=526109"
```
# Steps:
 1. Select sales order tab.
 2. Set date range: 1-01-2022 to current.
 3. Exclude stages: Awaiting Payment, Cancelled.
 4. Set Date as Created.
 5. Sales Orders Status -> Search All.
 6. Click on 'Actions' -> 'Export Sales Orders details'.
 7. Headers: Include BOM Load, create date, Invoice date.
 8. Click on 'Export Data' -> 'Export'.

