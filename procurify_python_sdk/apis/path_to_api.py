import typing_extensions

from procurify_python_sdk.paths import PathValues
from procurify_python_sdk.apis.paths.oauth_token import OauthToken
from procurify_python_sdk.apis.paths.api_v2_ap_bills_id import ApiV2ApBillsId
from procurify_python_sdk.apis.paths.api_v2_ap_company_payment_methods import ApiV2ApCompanyPaymentMethods
from procurify_python_sdk.apis.paths.api_v2_ap_items import ApiV2ApItems
from procurify_python_sdk.apis.paths.api_v2_ap_payments import ApiV2ApPayments
from procurify_python_sdk.apis.paths.api_v2_ap_payments_id_approver_choices import ApiV2ApPaymentsIdApproverChoices
from procurify_python_sdk.apis.paths.api_v2_ap_vendor_payment_methods import ApiV2ApVendorPaymentMethods
from procurify_python_sdk.apis.paths.api_v2_currencies import ApiV2Currencies
from procurify_python_sdk.apis.paths.api_v2_global_order_items import ApiV2GlobalOrderItems
from procurify_python_sdk.apis.paths.api_v2_global_orders import ApiV2GlobalOrders
from procurify_python_sdk.apis.paths.api_v2_locations import ApiV2Locations
from procurify_python_sdk.apis.paths.api_v2_locations_id import ApiV2LocationsId
from procurify_python_sdk.apis.paths.api_v2_purchase_order_revise_procurify_po import ApiV2PurchaseOrderReviseProcurifyPO
from procurify_python_sdk.apis.paths.api_v2_purchase_orders_id import ApiV2PurchaseOrdersId
from procurify_python_sdk.apis.paths.api_v2_purchase_orders_role_status import ApiV2PurchaseOrdersRoleStatus
from procurify_python_sdk.apis.paths.api_v3_account_codes import ApiV3AccountCodes
from procurify_python_sdk.apis.paths.api_v3_account_codes_id import ApiV3AccountCodesId
from procurify_python_sdk.apis.paths.api_v3_accounts import ApiV3Accounts
from procurify_python_sdk.apis.paths.api_v3_ap_bills import ApiV3ApBills
from procurify_python_sdk.apis.paths.api_v3_catalog_bundles import ApiV3CatalogBundles
from procurify_python_sdk.apis.paths.api_v3_catalog_items import ApiV3CatalogItems
from procurify_python_sdk.apis.paths.api_v3_catalog_items_id import ApiV3CatalogItemsId
from procurify_python_sdk.apis.paths.api_v3_custom_fields_id import ApiV3CustomFieldsId
from procurify_python_sdk.apis.paths.api_v3_custom_fields_order_items import ApiV3CustomFieldsOrderItems
from procurify_python_sdk.apis.paths.api_v3_departments import ApiV3Departments
from procurify_python_sdk.apis.paths.api_v3_departments_id import ApiV3DepartmentsId
from procurify_python_sdk.apis.paths.api_v3_order_items import ApiV3OrderItems
from procurify_python_sdk.apis.paths.api_v3_permissions import ApiV3Permissions
from procurify_python_sdk.apis.paths.api_v3_permissions_groups import ApiV3PermissionsGroups
from procurify_python_sdk.apis.paths.api_v3_purchase_orders_procurify_po import ApiV3PurchaseOrdersProcurifyPO
from procurify_python_sdk.apis.paths.api_v3_purchase_orders_procurify_po_close import ApiV3PurchaseOrdersProcurifyPOClose
from procurify_python_sdk.apis.paths.api_v3_purchase_orders_procurify_po_reopen import ApiV3PurchaseOrdersProcurifyPOReopen
from procurify_python_sdk.apis.paths.api_v3_purchase_orders_billing_history import ApiV3PurchaseOrdersBillingHistory
from procurify_python_sdk.apis.paths.api_v3_requisitions import ApiV3Requisitions
from procurify_python_sdk.apis.paths.api_v3_users import ApiV3Users
from procurify_python_sdk.apis.paths.api_v3_users_id import ApiV3UsersId
from procurify_python_sdk.apis.paths.api_v3_users_me import ApiV3UsersMe
from procurify_python_sdk.apis.paths.api_v3_vendors import ApiV3Vendors
from procurify_python_sdk.apis.paths.api_v3_vendors_id import ApiV3VendorsId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.OAUTH_TOKEN: OauthToken,
        PathValues.API_V2_AP_BILLS_ID: ApiV2ApBillsId,
        PathValues.API_V2_AP_COMPANYPAYMENTMETHODS: ApiV2ApCompanyPaymentMethods,
        PathValues.API_V2_AP_ITEMS: ApiV2ApItems,
        PathValues.API_V2_AP_PAYMENTS: ApiV2ApPayments,
        PathValues.API_V2_AP_PAYMENTS_ID_APPROVERCHOICES: ApiV2ApPaymentsIdApproverChoices,
        PathValues.API_V2_AP_VENDORPAYMENTMETHODS: ApiV2ApVendorPaymentMethods,
        PathValues.API_V2_CURRENCIES: ApiV2Currencies,
        PathValues.API_V2_GLOBAL_ORDER_ITEMS: ApiV2GlobalOrderItems,
        PathValues.API_V2_GLOBAL_ORDERS: ApiV2GlobalOrders,
        PathValues.API_V2_LOCATIONS: ApiV2Locations,
        PathValues.API_V2_LOCATIONS_ID: ApiV2LocationsId,
        PathValues.API_V2_PURCHASE_ORDER_REVISE_PROCURIFY_PO: ApiV2PurchaseOrderReviseProcurifyPO,
        PathValues.API_V2_PURCHASE_ORDERS_ID: ApiV2PurchaseOrdersId,
        PathValues.API_V2_PURCHASE_ORDERS_ROLE_STATUS: ApiV2PurchaseOrdersRoleStatus,
        PathValues.API_V3_ACCOUNTCODES: ApiV3AccountCodes,
        PathValues.API_V3_ACCOUNTCODES_ID: ApiV3AccountCodesId,
        PathValues.API_V3_ACCOUNTS: ApiV3Accounts,
        PathValues.API_V3_AP_BILLS: ApiV3ApBills,
        PathValues.API_V3_CATALOGBUNDLES: ApiV3CatalogBundles,
        PathValues.API_V3_CATALOGITEMS: ApiV3CatalogItems,
        PathValues.API_V3_CATALOGITEMS_ID: ApiV3CatalogItemsId,
        PathValues.API_V3_CUSTOMFIELDS_ID: ApiV3CustomFieldsId,
        PathValues.API_V3_CUSTOMFIELDS_ORDERITEMS: ApiV3CustomFieldsOrderItems,
        PathValues.API_V3_DEPARTMENTS: ApiV3Departments,
        PathValues.API_V3_DEPARTMENTS_ID: ApiV3DepartmentsId,
        PathValues.API_V3_ORDERITEMS: ApiV3OrderItems,
        PathValues.API_V3_PERMISSIONS: ApiV3Permissions,
        PathValues.API_V3_PERMISSIONS_GROUPS: ApiV3PermissionsGroups,
        PathValues.API_V3_PURCHASEORDERS_PROCURIFY_PO: ApiV3PurchaseOrdersProcurifyPO,
        PathValues.API_V3_PURCHASEORDERS_PROCURIFY_PO_CLOSE: ApiV3PurchaseOrdersProcurifyPOClose,
        PathValues.API_V3_PURCHASEORDERS_PROCURIFY_PO_REOPEN: ApiV3PurchaseOrdersProcurifyPOReopen,
        PathValues.API_V3_PURCHASEORDERS_BILLINGHISTORY: ApiV3PurchaseOrdersBillingHistory,
        PathValues.API_V3_REQUISITIONS: ApiV3Requisitions,
        PathValues.API_V3_USERS: ApiV3Users,
        PathValues.API_V3_USERS_ID: ApiV3UsersId,
        PathValues.API_V3_USERS_ME: ApiV3UsersMe,
        PathValues.API_V3_VENDORS: ApiV3Vendors,
        PathValues.API_V3_VENDORS_ID: ApiV3VendorsId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.OAUTH_TOKEN: OauthToken,
        PathValues.API_V2_AP_BILLS_ID: ApiV2ApBillsId,
        PathValues.API_V2_AP_COMPANYPAYMENTMETHODS: ApiV2ApCompanyPaymentMethods,
        PathValues.API_V2_AP_ITEMS: ApiV2ApItems,
        PathValues.API_V2_AP_PAYMENTS: ApiV2ApPayments,
        PathValues.API_V2_AP_PAYMENTS_ID_APPROVERCHOICES: ApiV2ApPaymentsIdApproverChoices,
        PathValues.API_V2_AP_VENDORPAYMENTMETHODS: ApiV2ApVendorPaymentMethods,
        PathValues.API_V2_CURRENCIES: ApiV2Currencies,
        PathValues.API_V2_GLOBAL_ORDER_ITEMS: ApiV2GlobalOrderItems,
        PathValues.API_V2_GLOBAL_ORDERS: ApiV2GlobalOrders,
        PathValues.API_V2_LOCATIONS: ApiV2Locations,
        PathValues.API_V2_LOCATIONS_ID: ApiV2LocationsId,
        PathValues.API_V2_PURCHASE_ORDER_REVISE_PROCURIFY_PO: ApiV2PurchaseOrderReviseProcurifyPO,
        PathValues.API_V2_PURCHASE_ORDERS_ID: ApiV2PurchaseOrdersId,
        PathValues.API_V2_PURCHASE_ORDERS_ROLE_STATUS: ApiV2PurchaseOrdersRoleStatus,
        PathValues.API_V3_ACCOUNTCODES: ApiV3AccountCodes,
        PathValues.API_V3_ACCOUNTCODES_ID: ApiV3AccountCodesId,
        PathValues.API_V3_ACCOUNTS: ApiV3Accounts,
        PathValues.API_V3_AP_BILLS: ApiV3ApBills,
        PathValues.API_V3_CATALOGBUNDLES: ApiV3CatalogBundles,
        PathValues.API_V3_CATALOGITEMS: ApiV3CatalogItems,
        PathValues.API_V3_CATALOGITEMS_ID: ApiV3CatalogItemsId,
        PathValues.API_V3_CUSTOMFIELDS_ID: ApiV3CustomFieldsId,
        PathValues.API_V3_CUSTOMFIELDS_ORDERITEMS: ApiV3CustomFieldsOrderItems,
        PathValues.API_V3_DEPARTMENTS: ApiV3Departments,
        PathValues.API_V3_DEPARTMENTS_ID: ApiV3DepartmentsId,
        PathValues.API_V3_ORDERITEMS: ApiV3OrderItems,
        PathValues.API_V3_PERMISSIONS: ApiV3Permissions,
        PathValues.API_V3_PERMISSIONS_GROUPS: ApiV3PermissionsGroups,
        PathValues.API_V3_PURCHASEORDERS_PROCURIFY_PO: ApiV3PurchaseOrdersProcurifyPO,
        PathValues.API_V3_PURCHASEORDERS_PROCURIFY_PO_CLOSE: ApiV3PurchaseOrdersProcurifyPOClose,
        PathValues.API_V3_PURCHASEORDERS_PROCURIFY_PO_REOPEN: ApiV3PurchaseOrdersProcurifyPOReopen,
        PathValues.API_V3_PURCHASEORDERS_BILLINGHISTORY: ApiV3PurchaseOrdersBillingHistory,
        PathValues.API_V3_REQUISITIONS: ApiV3Requisitions,
        PathValues.API_V3_USERS: ApiV3Users,
        PathValues.API_V3_USERS_ID: ApiV3UsersId,
        PathValues.API_V3_USERS_ME: ApiV3UsersMe,
        PathValues.API_V3_VENDORS: ApiV3Vendors,
        PathValues.API_V3_VENDORS_ID: ApiV3VendorsId,
    }
)
